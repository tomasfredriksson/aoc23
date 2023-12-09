def main():
    testfile = open("testdata/5a.txt", "r")
    inputfile = open("inputdata/5a.txt", "r")
    lines = inputfile.readlines()

    aParse = False      # seed-to-soil map:
    bParse = False      # soil-to-fertilizer map:
    cParse = False      # fertilizer-to-water map:
    dParse = False      # water-to-light map:
    eParse = False      # light-to-temperature map:
    fParse = False      # temperature-to-humidity map:
    gParse = False      # humidity-to-location map:
    number_of_seeds = 100 # CHANGE THIS IF NEEDED     _DEBUG_
    seed_list = []
    soil_data = []
    fert_data = []
    water_data = []
    light_data = []
    temp_data = []
    humidity_data = []
    location_data = []
    for line in lines:
        sorted_lines = line.strip('\n')
        if 'seeds: ' in sorted_lines:
            unfiltered_seeds = sorted_lines.strip('seeds: ')
            unfiltered_seeds = unfiltered_seeds.split(' ')
            for u in unfiltered_seeds:
                seed_list.append(int(u))
        if 'seed-to-soil' in sorted_lines:
            aParse = True
            continue
        if 'soil-to-fertilizer' in sorted_lines:
            aParse = False
            bParse = True
            continue
        if 'fertilizer-to-water' in sorted_lines:
            bParse = False
            cParse = True
            continue
        if 'water-to-light' in sorted_lines:
            cParse = False
            dParse = True
            continue
        if 'light-to-temperature' in sorted_lines:
            dParse = False
            eParse = True
            continue
        if 'temperature-to-humidity' in sorted_lines:
            eParse = False
            fParse = True
            continue
        if 'humidity-to-location' in sorted_lines:
            fParse = False
            gParse = True
            continue
        if aParse:
            if sorted_lines != '':
                soils = sorted_lines.split(' ')
                d_range = int(soils[0])
                s_range = int(soils[1])
                range_l = int(soils[2])
                #print("Adding Soil Data...", d_range, s_range, range_l)
                soil_data.append([d_range, s_range, range_l])
        if bParse:
            if sorted_lines != '':
                ferts = sorted_lines.split(' ')
                d_range = int(ferts[0])
                s_range = int(ferts[1])
                range_l = int(ferts[2])
                #print("Adding Fertilizer Data...", d_range, s_range, range_l)
                fert_data.append([d_range, s_range, range_l])
        if cParse:
            if sorted_lines != '':
                waters = sorted_lines.split(' ')
                d_range = int(waters[0])
                s_range = int(waters[1])
                range_l = int(waters[2])
                #print("Adding Water Data...", d_range, s_range, range_l)
                water_data.append([d_range, s_range, range_l])
        if dParse:
            if sorted_lines != '':
                lights = sorted_lines.split(' ')
                d_range = int(lights[0])
                s_range = int(lights[1])
                range_l = int(lights[2])
                #print("Adding Light Data...", d_range, s_range, range_l)
                light_data.append([d_range, s_range, range_l])
        if eParse:
            if sorted_lines != '':
                temps = sorted_lines.split(' ')
                d_range = int(temps[0])
                s_range = int(temps[1])
                range_l = int(temps[2])
                #print("Adding Temperature Data...", d_range, s_range, range_l)
                temp_data.append([d_range, s_range, range_l])
        if fParse:
            if sorted_lines != '':
                hums = sorted_lines.split(' ')
                d_range = int(hums[0])
                s_range = int(hums[1])
                range_l = int(hums[2])
                #print("Adding Humidity Data...", d_range, s_range, range_l)
                humidity_data.append([d_range, s_range, range_l])
        if gParse:
            if sorted_lines != '':
                locs = sorted_lines.split(' ')
                d_range = int(locs[0])
                s_range = int(locs[1])
                range_l = int(locs[2])
                #print("Adding Location Data...", d_range, s_range, range_l)
                location_data.append([d_range, s_range, range_l])
    #print(seed_list)
    #print(soil_data)
    #print(fert_data)
    #print(water_data)
    #print(light_data)
    #print(temp_data)
    #print(humidity_data)
    #print(location_data)

    #d  s  r
    #50 98 2
    #98 -> 50
    #99 -> 51
    #s = d + iteration_no
    #52 50 48
    #50 -> 52
    #51 -> 53
    # ...
    #79 -> 81
    # ...
    #96 -> 98
    #97 -> 99
    
    print(seed_list)
    real_seed_list = []
    for i in range(seed_list[1]):
        real_seed_list.append(seed_list[0]+i)
    for i in range(seed_list[3]):
        real_seed_list.append(seed_list[2]+i)
    print(real_seed_list)

    location_numbers = []
    for seed in real_seed_list:
        seed_information = []
        #print(seed)
        seed_information.append(seed)
        for soil in soil_data:
            if seed >= soil[1] and seed < soil[1] + soil[2]:
                x_soil = seed + (soil[0]-soil[1])
                seed_information.append(x_soil)
        if len(seed_information) == 1:
            x_soil = seed
            seed_information.append(x_soil)
        for fert in fert_data:
            if x_soil >= fert[1] and x_soil < fert[1] + fert[2]:
                x_fert = x_soil + (fert[0] - fert[1])
                seed_information.append(x_fert)
        if len(seed_information) == 2:
            x_fert = x_soil
            seed_information.append(x_fert)
        for water in water_data:
            if x_fert >= water[1] and x_fert < water[1] + water[2]:
                x_water = x_fert + (water[0] - water[1])
                seed_information.append(x_water)
        if len(seed_information) == 3:
            x_water = x_fert
            seed_information.append(x_water)
        for light in light_data:
            if x_water >= light[1] and x_water < light[1] + light[2]:
                x_light = x_water + (light[0] - light[1])
                seed_information.append(x_light)
        if len(seed_information) == 4:
            x_light = x_water
            seed_information.append(x_light)
        for temp in temp_data:
            if x_light >= temp[1] and x_light < temp[1] + temp[2]:
                x_temp = x_light + (temp[0] - temp[1])
                seed_information.append(x_temp)
        if len(seed_information) == 5:
            x_temp = x_light
            seed_information.append(x_temp)
        for hum in humidity_data:
            if x_temp >= hum[1] and x_temp < hum[1] + hum[2]:
                x_hum = x_temp + (hum[0] - hum[1])
                seed_information.append(x_hum)
        if len(seed_information) == 6:
            x_hum = x_temp
            seed_information.append(x_hum)
        for loc in location_data:
            if x_hum >= loc[1] and x_hum < loc[1] + loc[2]:
                x_loc = x_hum + (loc[0] - loc[1])
                seed_information.append(x_loc)
        if len(seed_information) == 7:
            x_loc = x_hum
            seed_information.append(x_loc)
        #print(seed_information)
        location_numbers.append(x_loc)
    print(location_numbers)
    print(min(location_numbers))


main()