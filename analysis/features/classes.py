import pandas as pd
import seaborn
from analysis.features.analyzer import FeatureAnalyzer


class ClassDistributionAnalyzer(FeatureAnalyzer):
    # Here, a class named ClassDistributionAnalyzer is defined, and it inherits from the FeatureAnalyzer class. This
    # means that ClassDistributionAnalyzer is a subclass of FeatureAnalyzer, and it inherits all the attributes and
    # methods defined in the parent class.

    def __init__(self, matches_df: pd.DataFrame):
        super().__init__(matches_df=matches_df)
    # The constructor initializes an instance of ClassDistributionAnalyzer. It calls the constructor of the parent
    # class (FeatureAnalyzer) using the super() function. It passes the matches_df DataFrame to the parent class's
    # constructor.

    def plot(self, ax, **kwargs):
        targets = self.targets
        seaborn.barplot(x=['H', 'D', 'A'], y=targets.value_counts(), color=None, ax=ax)
    # This method plot is defined within the ClassDistributionAnalyzer class. It takes an ax argument (presumably a
    # matplotlib axes object) and additional keyword arguments (kwargs). Inside the method: targets is assigned the
    # value of the targets property inherited from the parent class (FeatureAnalyzer). seaborn.barplot is used to
    # create a bar plot. It shows the distribution of target classes ('H', 'D', 'A') based on the counts of each
    # class in the targets series obtained from value_counts(). The plot is added to the specified ax object.

    # In summary, the ClassDistributionAnalyzer class is a subclass of FeatureAnalyzer that specializes in creating a
    # bar plot to analyze the distribution of classes in a dataset. It inherits the constructor and other properties
    # from FeatureAnalyzer and provides its own implementation of the plot method for this specific type of analysis.
