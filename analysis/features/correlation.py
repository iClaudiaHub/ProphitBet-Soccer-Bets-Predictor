from analysis.features.analyzer import FeatureAnalyzer
import numpy as np
import seaborn
import pandas as pd


class CorrelationAnalyzer(FeatureAnalyzer):
    def __init__(self, matches_df: pd.DataFrame):
        super().__init__(matches_df=matches_df)

        self._home_columns = [home_col for home_col in self.inputs.columns if home_col[0] != 'A']
        self._away_columns = [home_col for home_col in self.inputs.columns if home_col[0] != 'H']
    # The constructor initializes an instance of CorrelationAnalyzer. It calls the constructor of the parent class (
    # FeatureAnalyzer) using super(), passing the matches_df DataFrame. Additionally, it does the following: It
    # calculates the columns associated with home teams (_home_columns) by filtering the input columns where the
    # first character is not 'A'. It calculates the columns associated with away teams (_away_columns) by filtering
    # the input columns where the first character is not 'H'

    @property
    def home_columns(self) -> list:
        return self._home_columns

    @property
    def away_columns(self) -> list:
        return self._away_columns
    # These property methods allow access to the calculated _home_columns and _away_columns attributes, effectively
    # providing the columns associated with home and away teams

    def plot(self, columns: np.ndarray or list, color_map: str, hide_upper_triangle: bool, ax, **kwargs):
        d = self._inputs[columns]
        correlations = d.corr()
        mask = np.triu(np.ones_like(correlations, dtype=bool)) if hide_upper_triangle else None
        seaborn.heatmap(correlations, annot=True, cmap=color_map, mask=mask, ax=ax)
    # This method plot is defined within the CorrelationAnalyzer class. It takes several arguments: columns (selected
    # columns for analysis), color_map (color map for heatmap), hide_upper_triangle (whether to hide upper triangle
    # of the heatmap), ax (matplotlib axes object), and additional keyword arguments (kwargs). Inside the method: d
    # is assigned a subset of the input data (_inputs) containing only the selected columns (columns). correlations
    # are calculated using the .corr() method on the subset d. A mask is created based on whether hide_upper_triangle
    # is True, which is used to hide the upper triangle of the heatmap. seaborn.heatmap is used to create a heatmap
    # of correlations, with annotations, using the specified color_map and the calculated mask. The plot is added to
    # the specified ax object.

    # In summary, the CorrelationAnalyzer class is a subclass of FeatureAnalyzer that specializes in calculating and
    # visualizing correlations between features. It inherits properties and methods from the parent class and
    # provides its own implementation of the plot method for correlation analysis. The class also introduces
    # properties to access home and away team-related columns.
