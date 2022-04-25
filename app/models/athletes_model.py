from dataclasses import dataclass
from enum import unique
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class AthletesModel(db.Model):
    # id: int
    name: str
    sex: str
    sport: str
    medal: str
    # team_id: str
    team: object

    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    sport = Column(String, nullable=False)
    medal = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False, unique=True)

    team = relationship("TeamModel", back_populates="athletes")
