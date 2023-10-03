"""
Schemas for sun_results
"""

from pydantic import BaseModel


class Results(BaseModel):
    """
    Sun behavior data for a given location
    """

    sunrise: str
    sunset: str
    first_light: str
    last_light: str
    dawn: str
    dusk: str
    solar_noon: str
    golden_hour: str
    day_length: str
    timezone: str
    utc_offset: int


class SunResults(BaseModel):
    results: Results
    status: str
