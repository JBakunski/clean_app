from sqlalchemy import Table, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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


class Measure(Base):
    __tablename__ = 'measures'

    id = Column(Integer, primary_key=True)
    station_id = Column(String, ForeignKey('stations.station_identifier'))
    date = Column(Date)
    precip = Column(Float)
    tobs = Column(Integer)

    station = relationship("Station", back_populates="measures")

