import pandas as pd

# outputs a frame that shows if counties are in a specific district
def in_district(city_frame, district_num: float):
    temp_district = city_frame[city_frame["Voting District"] == district_num]
    return temp_district

# outputs only the counties in a specific district
def all_counties(city_frame, upper_bound: int):
    for i in range(1, upper_bound):
        print("{0} counties in district {1}".format(in_district(city_frame, i), i))

# gets size of a district
def size_of_district(frame, district_num):
    in_dist_one = frame.apply(lambda x: True if x["Voting District"] == district_num else False, axis = 1)
    num = len(in_dist_one[in_dist_one == True].index)
    return num

# outputs the size of all districts
def all_district_sizes(frame, upper_bound: int):
    for i in range(1, upper_bound):
        current_size = size_of_district(frame, i)
        print("Size of district {0}: {1}".format(i, current_size))

# sorts the districts by how white they are
def sort_by_whiteness(frame):
    pop_frame = frame.sort_values(by=['White'])
    return pop_frame

# returns whether or not a county satisfies a minimum support
def meet_minsup(frame, min_sup):
    min_frame = frame.where(frame['White'] < min_sup)
    return min_frame

# used after meet_minsup to get the number of counties that
# satisfy the minimum support
def count_minsup(frame):
    return frame["City"].count()

# gets the size of the data frame
def count_rows(frame):
    return frame.shape[0]

# calculates the support
def get_sup(frame):
    city_sup = count_minsup(frame) / count_rows(frame)
    return round(city_sup, 2)

# Code in action below
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

cities = pd.read_csv("Modified CSC 426 2020 Population Census - Sheet1.csv")

min_support = 0.55 
increasing_whiteness = cities.sort_values(by=['White'])

white_minority = increasing_whiteness.where(increasing_whiteness['White'] < min_support)

headings_to_print = ["County", "City", "White"]

district_four = in_district(cities, 4.0)
district_filter = sort_by_whiteness(district_four)

print(district_four[headings_to_print])
district_filter = meet_minsup(district_filter, min_support)
print("\n")
print(district_filter[headings_to_print])

percent = count_minsup(district_filter) / count_rows(district_filter)
n = get_sup(district_filter)

print(n)
