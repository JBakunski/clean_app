

def display_stations_with_measures(query, display_limit):
    for station in query.limit(display_limit):
        print(f"{station}:")
        for measure in station.measures:
            print(measure)