from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class TeamModel(db.Model):
    # id: int
    team_name: str
    athletes: list

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable=False)
    # athletes = relationship(
    #     "AthletesModel", backref=backref("team", uselist=False), uselist=True
    # )
    athletes = relationship("AthletesModel", back_populates="team", uselist=True)
