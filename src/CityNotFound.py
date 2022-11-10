"""Custom Error if the city the user searched for is not found."""

class CityNotFound(Exception):
    """Raise a City not found Error."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
