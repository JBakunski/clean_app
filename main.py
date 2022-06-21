import data_access
import presentation
from data_models import Station



session = data_access.Session()

if __name__ == "__main__":
    query_data = session.query(Station).order_by(Station.id) 
    presentation.display_stations_with_measures(query_data, 3)
    
    
    
    