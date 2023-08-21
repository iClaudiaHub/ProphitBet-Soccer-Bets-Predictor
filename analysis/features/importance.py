import numpy as np
import seaborn
import pandas as pd
from analysis.features.analyzer import FeatureAnalyzer
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif
from sklearn.feature_selection import RFE
from xgboost import XGBRFClassifier


class ImportanceAnalyzer(FeatureAnalyzer):
    def __init__(self, matches_df: pd.DataFrame):
        super().__init__(matches_df=matches_df)

        self._class_weights_model = None
        self._rfe_model = None
        self._variance_model = None
        self._best_model = None
    # The constructor initializes an instance of ImportanceAnalyzer. It calls the constructor of the parent class (
    # FeatureAnalyzer) using super(), passing the matches_df DataFrame. Additionally, it initializes several
    # attributes (_class_weights_model, _rfe_model, _variance_model, _best_model) with None.

    def plot_feature_classification_weights(self, ax):
        if self._class_weights_model is None:
            self._class_weights_model = XGBRFClassifier(random_state=0, n_jobs=-1)
            self._class_weights_model.fit(self.inputs, self.targets)

        weights = self._class_weights_model.get_booster().get_score(importance_type='weight')
        self.plot(x=list(weights.values()), y=list(weights.keys()), ax=ax)
    # This method calculates and visualizes feature importance based on classification weights. If the
    # _class_weights_model is not initialized, it creates an instance of XGBRFClassifier and fits it to the input
    # data. Then, it retrieves feature weights from the model and plots them using the plot method.

    def plot_feature_elimination_importance(self, ax):
        if self._rfe_model is None:
            self._rfe_model = RFE(
                estimator=XGBRFClassifier(random_state=0, n_jobs=-1),
                step=1
            )
            self._rfe_model.fit(self._inputs, self.targets)

        self.plot(x=self._rfe_model.ranking_, y=self.columns, ax=ax)
    # This method calculates and visualizes feature importance using recursive feature elimination (RFE). If
    # _rfe_model is not initialized, it creates an instance of RFE with XGBRFClassifier as the estimator and fits it
    # to the input data. It then plots the RFE rankings using the plot method.

    def plot_feature_variances(self, ax):
        if self._variance_model is None:
            self._variance_model = VarianceThreshold()
            self._variance_model.fit(self._inputs)

        self.plot(x=self._variance_model.variances_, y=self.columns, ax=ax)
    # This method calculates and visualizes feature importance based on variances. If _variance_model is not
    # initialized, it creates an instance of VarianceThreshold and fits it to the input data. It then plots the
    # variances using the plot method.

    def plot_univariate_test_importance(self, ax):
        if self._best_model is None:
            self._best_model = SelectKBest(score_func=f_classif, k='all')
            self._best_model.fit(self._inputs, self.targets)

        self.plot(x=self._best_model.scores_, y=self.columns, ax=ax)
    # This method calculates and visualizes feature importance using univariate feature selection. If _best_model is
    # not initialized, it creates an instance of SelectKBest with f_classif as the scoring function and fits it to
    # the input data. It then plots the scores using the plot method.

    def plot(self, x: np.ndarray or list, y: np.ndarray or list, ax, **kwargs):
        seaborn.barplot(x=x, y=y, ax=ax)
    # This method is inherited from the parent class FeatureAnalyzer. It takes x and y data for plotting, as well as
    # an ax object for matplotlib axes. It creates a bar plot using seaborn.barplot

# In summary, the ImportanceAnalyzer class is a subclass of FeatureAnalyzer that specializes in analyzing and
# visualizing feature importances using various techniques. It provides methods to calculate and visualize feature
# importance based on classification weights, recursive feature elimination, variances, and univariate tests. The
# class inherits methods and properties from the parent class and introduces its own methods for importance analysis.
