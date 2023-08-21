import pandas as pd
from abc import ABC, abstractmethod
from datetime import date
from database.entities.league import League


class FootballDataAPI(ABC):
    # It is an abstract base class (ABC) that's meant to serve as a blueprint for other classes implementing the
    # football data downloading and processing logic. The class serves as an abstract base class that defines a
    # common interface and structure for downloading and processing football data. Subclasses that inherit from
    # FootballDataAPI need to implement the _download and _process_features methods, which allows them to provide
    # specific implementations for accessing and structuring the data. This design encourages consistent behavior
    # across different data sources while allowing for customization in the implementation details.

    def download(self, league: League) -> pd.DataFrame:
        matches_df = self._download(league=league)
        matches_df = self._process_features(matches_df=matches_df)
        matches_df = matches_df.drop_duplicates()
        matches_df = matches_df.iloc[::-1].reset_index(drop=True)
        return matches_df
    # This method is not abstract and provides a common downloading and processing workflow for football data. It
    # takes a league argument of the League class and returns a processed pandas DataFrame representing match data.

    # Here's what the method does: Calls the _download method (which must be implemented by subclasses) to download
    # raw match data for the specified league. Calls the _process_features method (also to be implemented by
    # subclasses) to process the raw match data into a more structured format. Drops any duplicate rows from the
    # resulting DataFrame. Reverses the order of rows in the DataFrame using iloc[::-1] and then resets the index to
    # ensure a consistent indexing. Returns the processed DataFrame containing match data.

    @abstractmethod
    def _download(self, league: League) -> pd.DataFrame:
        pass

    @abstractmethod
    def _process_features(self, matches_df: pd.DataFrame) -> pd.DataFrame:
        pass
    # These are abstract methods that must be implemented by any concrete subclass of FootballDataAPI. Subclasses
    # need to provide their own logic for downloading and processing football data. The _download method should take
    # a league parameter and return a DataFrame with raw match data. The _process_features method should take a
    # DataFrame containing raw match data and return a DataFrame with processed and structured match data.

# In summary, the FootballDataAPI class is an abstract base class that defines a common interface and workflow for
# downloading and processing football data. Subclasses that inherit from it are required to implement the _download
# and _process_features methods to provide the specific logic for accessing and structuring the football data from a
# data source (API, database, etc.)
