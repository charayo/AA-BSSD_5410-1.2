##########
# SelectionSort Snippet from: https://big-o.io/algorithms/comparison/selection-sort/
# on 01/22/2023
# License: © 2020 Big-O
# ChangeLog:
# Refactor code
# modify selection sort to sort the distance instead of locations
# Change the array data to a list of tuples containing the destination and calculated distances from origin
##########
import requests
import math

URL_PATH = "https://nominatim.openstreetmap.org/search.php"


def get_lat_lon(location):
    PARAMS = {'q': location, 'format': 'jsonv2'}
    r = requests.get(url=URL_PATH, params=PARAMS)
    data = r.json()
    # print(data)
    latitude = float(data[0]["lat"])
    longitude = float(data[0]["lon"])
    return [latitude, longitude]


# end of get_lat_lon(location)


def calculate_distance(orig, dest):
    dlon = dest[1] - orig[1]
    dlat = dest[0] - orig[0]
    a = (math.sin(math.radians(dlat / 2))) ** 2 + math.cos(math.radians(orig[0])) * math.cos(math.radians(dest[0])) * \
        (math.sin(math.radians(dlon / 2))) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961  # gives miles switch to 6373 for km
    d = R * c
    return d


# end def calculate_distance(orig, dest):


def main():
    places = ["New Mexico Museum of Natural History & Science", "New Mexico Highlands University",
              "Albuquerque International Sunport", "Santa Fe Regional Airport",
              "Carlsbad Caverns National Park", "White Sands National Park"]
    loc_geos = {}
    for index, place in enumerate(places):
        loc_geos["loc{}".format(index)] = get_lat_lon(place)
    # print(loc_geos)
    # Using list comprehension to make the list of distances
    distances = [
        (location, calculate_distance(loc_geos["loc{}".format(0)], loc_geos["loc{}".format(i)]))
        for i, location in enumerate(places) if
        i > 0]  # conditional statement to exclude the zero distance of when comparing the origin with itself
    return distances
# end def(main)


def selection_sort(array):
    # step 1: loop from the beginning of the array to the second to last item
    currentIndex = 0
    while currentIndex < len(array) - 1:
        # step 2: save a copy of the currentIndex
        minIndex = currentIndex
        # step 3: loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while i < len(array):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if array[i][1] < array[minIndex][1]:
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if minIndex != currentIndex:
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1
# end of def selection_sort(array):


if __name__ == '__main__':
    array = main()
    print(array)
    selection_sort(array)
    print(array)
