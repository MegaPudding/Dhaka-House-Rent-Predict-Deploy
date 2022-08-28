import pickle
import json
import numpy as np

__Locations = None
__data_columns = None
__model = None

def get_estimated_price(Location,Area,Bed,Bath):
    try:
        loc_index = __data_columns.index(Location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Area
    x[1] = Bed
    x[2] = Bath
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __Locations

    with open(r'server\artifacts\columns.json','r' ) as f:
        __data_columns = json.load(f)['data_columns']
        __Locations = __data_columns[3:]  # first 3 columns are Area, Bed, Bath

    global __model
    if __model is None:
        with open(r'server\artifacts\dhaka_house_rent_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    #__Locations = __data_columns[3:]
    load_saved_artifacts()
    return __Locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Dhanmondi Dhaka',2100, 3, 3))
    print(get_estimated_price('Badda Dhaka',1000, 2, 2))
    print(get_estimated_price('Gulshan 2 Gulshan Dhaka',2000, 3, 3)) # other location
    print(get_estimated_price('Mirpur Dhaka',1250, 3, 3))  # other location
