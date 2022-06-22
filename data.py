from data_models import Measure, Station
from datetime import date



initial_data = [
    Station(id='USC00519397', latitiude=21.2716, longitude=-157.8168, elevation=3.0, name='WAIKIKI 717.2', country='US', state='HI'),
    Station(id='USC00513117', latitiude=21.4234, longitude=-157.8015, elevation=14.6, name='KANEOHE 838.1', country='US', state='HI'),
    Station(id='USC00514830', latitiude=21.5213, longitude=-157.8374, elevation=7.0, name='KUALOA RANCH HEADQUARTERS 886.9', country='US', state='HI'),
    Station(id='USC00517948', latitiude=21.3934, longitude=-157.9751, elevation=11.9, name='PEARL CITY', country='US', state='HI'),
    Measure(id=1, station_id='USC00519397',  date=date(2010,1,1), precip=0.08, tobs=65),
    Measure(id=2, station_id='USC00519397',  date=date(2010,1,2), precip=0.0, tobs=63),
    Measure(id=3, station_id='USC00519397',  date=date(2010,1,3), precip=0.0, tobs=74),
    Measure(id=4, station_id='USC00519397',  date=date(2010,1,4), precip=0.0, tobs=76),
    Measure(id=5, station_id='USC00519397',  date=date(2010,1,5), precip=0.06, tobs=73),
    Measure(id=6, station_id='USC00519397',  date=date(2010,1,6), precip=0.0, tobs=70),
    Measure(id=7, station_id='USC00519397',  date=date(2010,1,7), precip=0.0, tobs=64),
    Measure(id=8, station_id='USC00519397',  date=date(2010,1,8), precip=0.0, tobs=68),
    Measure(id=9, station_id='USC00513117',  date=date(2011,11,9), precip=0.03, tobs=74),
    Measure(id=10, station_id='USC00513117',  date=date(2011,11,9), precip=0.04, tobs=74),
    Measure(id=11, station_id='USC00513117',  date=date(2011,11,9), precip=0.16, tobs=75),
    Measure(id=12, station_id='USC00513117',  date=date(2011,11,9), precip=0.07, tobs=73),
    Measure(id=13, station_id='USC00514830',  date=date(2013,7,3), precip=0.03, tobs=75),
    Measure(id=14, station_id='USC00514830',  date=date(2013,7,4), precip=0.0, tobs=79)
] 


def populate_db(session, data):
    session.add_all(data)
    session.commit()