class League:
    def __init__(
            self,
            country: str,
            name: str,
            url: str,
            year_start: int,
            league_type: str,
            fixtures_url: str
    ):
        self._country = country
        self._name = name
        self._url = url
        self._year_start = year_start
        self._league_type = league_type
        self._fixtures_url = fixtures_url
    # The constructor (__init__ method) takes several arguments representing attributes of a league: country, name, url, year_start, league_type, and fixtures_url.

    # The constructor initializes an instance of the League class. It takes the following arguments:
    # country: A string representing the country where the league is located.
    # name: A string representing the name of the league.
    # url: A string representing the URL associated with the league.
    # year_start: An integer representing the starting year of the league.
    # league_type: A string representing the type or category of the league.
    # fixtures_url: A string representing the URL for the league's fixtures.
    # Inside the constructor, the provided arguments are used to initialize instance variables that correspond to these attributes.

    @property
    def country(self) -> str:
        return self._country

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def year_start(self) -> int:
        return self._year_start

    @year_start.setter
    def year_start(self, year_start: int):
        self._year_start = year_start

    @property
    def league_type(self) -> str:
        return self._league_type

    @property
    def fixtures_url(self) -> str:
        return self._fixtures_url
    # These property methods define getter methods for accessing the attributes of the League class.
    # The @property decorator is used to mark these methods as properties that can be accessed like attributes (without parentheses).
    # Additionally, a setter method is defined for the year_start attribute using the @year_start.setter decorator.
    # This allows you to modify the year_start attribute while ensuring any necessary validation or processing takes place.

    # In summary, the League class provides a blueprint for creating instances representing sports leagues.
    # It has attributes like country, name, url, year_start, league_type, and fixtures_url.
    # It also includes property methods for easy access to these attributes, including a setter method for year_start to allow modification.
    # This class seems designed to encapsulate information about a sports league in a convenient and structured manner.
