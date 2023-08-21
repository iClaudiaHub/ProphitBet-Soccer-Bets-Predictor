import numpy as np
import pandas as pd
from abc import ABC, abstractmethod   # abstractmethod decorator are imported from the abc module
from enum import Enum


class FeatureAnalyzer(ABC):
    # A class named FeatureAnalyzer is defined, and it inherits from the ABC class.
    # This means that FeatureAnalyzer is meant to be an abstract base class.
    # Abstract base classes provide a way to define a common interface for a set of related classes.

    class ColorMaps(Enum):
        Coolwarm = 'coolwarm'
        Rocket = 'rocket'
        Icefire = 'icefire'
        Crest = 'crest'
        Blues = 'Blues'
        # An inner class named ColorMaps is defined within the FeatureAnalyzer class.
        # It is an Enum class that defines a set of color maps.

    def __init__(self, matches_df: pd.DataFrame):
        self._inputs = matches_df.drop(
            columns=['Season', 'Date', 'Home Team', 'Away Team', 'Result']
        ).astype(np.float32)
        self._targets = matches_df['Result'].replace({'H': 0, 'D': 1, 'A': 2})
        self._columns = self._inputs.columns

    # The constructor initializes an instance of FeatureAnalyzer with a DataFrame named matches_df. (So, when we say
    # that the constructor (__init__ method) of the FeatureAnalyzer class "initializes an instance of
    # FeatureAnalyzer," it means that this constructor is responsible for setting up and configuring a specific
    # instance of the FeatureAnalyzer class. It's like providing a starting point for the instance to hold data and
    # operate according to the class's defined behaviors. In the provided code, the constructor takes a DataFrame (
    # matches_df) as an argument. This DataFrame likely contains data related to feature analysis. When you create an
    # instance of FeatureAnalyzer by calling its constructor, you're essentially creating a unique object that holds
    # the data specified in the matches_df DataFrame and provides access to the defined properties and methods within
    # the FeatureAnalyzer class.)

    # This instance can then be used to perform various feature analysis tasks.
    # It does the following: It calculates the inputs by dropping specific columns from the DataFrame
    # and converting the remaining data to np.float32 type.
    # It extracts the targets from the 'Result' column of the DataFrame,
    # replacing 'H' with 0, 'D' with 1, and 'A' with 2. It stores the column names of the input DataFrame.

    @property
    def inputs(self) -> pd.DataFrame:
        return self._inputs

    @property
    def targets(self) -> pd.DataFrame:
        return self._targets

    @property
    def columns(self) -> list:
        return self._columns

    # These are property methods that provide access to the calculated inputs, targets, and column names.
    # They allow you to access these attributes as if they were attributes of the class.

    @abstractmethod
    def plot(self, x: np.ndarray or list, y: np.ndarray or list, color_map: str, mask: np.ndarray, ax):
        pass
    # This is an abstract method named plot that takes several arguments (x, y, color_map, mask, and ax).
    # It's marked as an abstract method using the @abstractmethod decorator.
    # This means that any subclass of FeatureAnalyzer must provide an implementation for this method.
    # The purpose and behavior of the plot method should be defined in the subclasses.

    # Overall, the provided class seems to be a foundation for building feature analyzers. It initializes data and
    # provides some common properties, including inputs, targets, and columns. It also defines an abstract method
    # plot that subclasses need to implement, potentially for plotting and visualizing features in some specific way.
