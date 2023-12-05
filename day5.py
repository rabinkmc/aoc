import os

data = open("day5.txt").read().strip("\n").split("\n\n")
seeds = data[0].split(":")[-1].split()
seeds = [int(n) for n in seeds]

ranges = []
for i in range(1, len(data)):
    range_data = [
        [int(n) for n in d.split()] for d in data[i].split(":")[-1].strip().split("\n")
    ]
    ranges.append(range_data)

soil, fertilizer, water, light, temperature, humidity, location = ranges


soil_fertilizer = {}
fertilizer_water = {}
water_light = {}
light_temp = {}
temp_humidity = {}
humidity_location = {}


def get_data(source_list, source_range):
    output = {}
    for source in source_list:
        for d, s, r in source_range:
            if s <= source < s + r:
                output[source] = d + (source - s)
        output[source] = output.get(source, source)
    return output


seed_soil = get_data(seeds, ranges[0])
soil_fertilizer = get_data(seed_soil.values(), ranges[1])
fertilizer_water = get_data(soil_fertilizer.values(), ranges[2])
water_light = get_data(fertilizer_water.values(), ranges[3])
light_temperature = get_data(water_light.values(), ranges[4])
temperature_humidity = get_data(light_temperature.values(), ranges[5])
humidity_location = get_data(temperature_humidity.values(), ranges[6])
