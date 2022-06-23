import os
import data
import presentation
from data_models import Station, Measure, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_database(db_file):
    engine = create_engine(f'sqlite:///{db_file}')
    Base.metadata.create_all(engine, checkfirst=True)
    return engine



if __name__ == "__main__":
    db_file_name = "app_db.db"
       
    if os.path.isfile(f"{db_file_name}"):
        engine = create_engine(f'sqlite:///{db_file_name}')
        session = Session(engine)
    else:
        engine = create_database(db_file_name)
        session = Session(engine)    
        data.populate_db(session, data.initial_data)
    
    
    conn = engine.connect()

    query_data = session.query(Station).order_by(Station.id) 
    presentation.display_stations_with_measures(query_data, 3)
    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    print(result)
    
    
    