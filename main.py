import data
import presentation
from data_models import Station, Measure, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///app_db.db')
Base.metadata.create_all(engine, checkfirst=True)
session = Session(engine)
conn = engine.connect()


if __name__ == "__main__":
    # data.populate_db(session, data_access.initial_data)
    query_data = session.query(Station).order_by(Station.id) 
    presentation.display_stations_with_measures(query_data, 3)
    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    print(result)
    
    
    