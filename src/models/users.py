from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class TapStreak(BaseModel):
    streakStart: datetime
    currentStreak: int

class CurrentTapStreak(BaseModel):
    tappedToday: bool
    lastTap: Optional[datetime]
    streakStart: Optional[datetime]
    currentStreak: int

class Taps(BaseModel):
    totalTaps: int
    currentTapStreak: CurrentTapStreak
    tapStreaks: List[TapStreak]


class User(Document):
    id: str = Field(alias="_id")
    name: str
    taps: Taps

    class Settings:
        name = "users"
