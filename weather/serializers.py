from dataclasses import dataclass
from datetime import datetime

@dataclass
class WeatherEntitySerializer:
    temperature: float
    date: datetime
    city: str = ''
    atmosphericPressure: str = ''
    humidity: str = ''
    weather: str = ''

    def __str__(self) -> str:
        return f"Weather <{self.temperature}>"
