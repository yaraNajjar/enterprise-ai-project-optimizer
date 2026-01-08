from sqlalchemy import Column, Integer, Float
from db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    team_size = Column(Integer)
    issues = Column(Integer)
    predicted_duration = Column(Float)
    predicted_cost = Column(Float)
    delay_risk = Column(Integer)
