from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station_identifier = Column(String, unique=True)
    latitiude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)
    
    def __repr__(self):
        return f"ID:{self.station_identifier}, Name:{self.name}, State:{self.state}, Country:{self.country}"
    


class Measure(Base):
    __tablename__ = 'measures'
    id = Column(Integer, primary_key=True)
    station_id = Column(String, ForeignKey('stations.station_identifier'))
    date = Column(Date)
    precip = Column(Float)
    tobs = Column(Integer)

    station = relationship("Station", back_populates="measures")

    def __repr__(self):
        return f"Date:{self.date}, Precip:{self.precip}, Tobs:{self.tobs}"

Station.measures = relationship("Measure", order_by=Measure.id, back_populates="station")
    

