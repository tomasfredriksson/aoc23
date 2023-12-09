def main():
    testfile = open("testdata/5a.txt", "r")
    inputfile = open("inputdata/5a.txt", "r")
    lines = testfile.readlines()

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
            seeds = sorted_lines.strip('seeds: ')
            seeds = seeds.split(' ')
            #number_of_seeds = 999999999
            #print('Seeds:', seeds)
            for i in range(number_of_seeds):
                seed_list.append(i)
            #print(seed_list)
        if 'seed-to-soil' in sorted_lines:
            aParse = True
            for i in range(number_of_seeds):
                soil_data.append(i)
            #print(soil_data)
            continue
        if 'soil-to-fertilizer' in sorted_lines:
            aParse = False
            bParse = True
            fert_data = soil_data.copy()
            continue
        if 'fertilizer-to-water' in sorted_lines:
            bParse = False
            cParse = True
            water_data = fert_data.copy()
            continue
        if 'water-to-light' in sorted_lines:
            cParse = False
            dParse = True
            light_data = water_data.copy()
            continue
        if 'light-to-temperature' in sorted_lines:
            dParse = False
            eParse = True
            temp_data = light_data.copy()
            continue
        if 'temperature-to-humidity' in sorted_lines:
            eParse = False
            fParse = True
            humidity_data = temp_data.copy()
            continue
        if 'humidity-to-location' in sorted_lines:
            fParse = False
            gParse = True
            location_data = humidity_data.copy()
            continue
        if aParse:
            if sorted_lines != '':
                soils = sorted_lines.split(' ')
                d_range = int(soils[0])
                s_range = int(soils[1])
                range_l = int(soils[2])
                print("Adding Soil Data...", d_range, s_range, range_l)
                for r in range(s_range,s_range+range_l):
                    soil_data[seed_list.index(r)] = d_range + r - s_range
                #print("Soil-data:")
                #print(soil_data)
        if bParse:
            if sorted_lines != '':
                ferts = sorted_lines.split(' ')
                d_range = int(ferts[0])
                s_range = int(ferts[1])
                range_l = int(ferts[2])
                print("Adding Fertilizer Data...", d_range, s_range, range_l)
                for r in range(s_range,s_range+range_l):
                    fert_data[soil_data.index(r)] = d_range + r - s_range
                #print(fert_data)
        if cParse:
            if sorted_lines != '':
                waters = sorted_lines.split(' ')
                d_range = int(waters[0])
                s_range = int(waters[1])
                range_l = int(waters[2])
                for r in range(s_range,s_range+range_l):
                    water_data[fert_data.index(r)] = d_range + r - s_range
                print("Adding Water Data...", d_range, s_range, range_l)
                #print(water_data)
        if dParse:
            if sorted_lines != '':
                lights = sorted_lines.split(' ')
                d_range = int(lights[0])
                s_range = int(lights[1])
                range_l = int(lights[2])
                for r in range(s_range,s_range+range_l):
                    light_data[water_data.index(r)] = d_range + r - s_range
                print("Adding Light Data...", d_range, s_range, range_l)
                #print(light_data)
        if eParse:
            if sorted_lines != '':
                temps = sorted_lines.split(' ')
                d_range = int(temps[0])
                s_range = int(temps[1])
                range_l = int(temps[2])
                for r in range(s_range,s_range+range_l):
                    temp_data[light_data.index(r)] = d_range + r - s_range
                print("Adding Temperature Data...", d_range, s_range, range_l)
                #print(temp_data)
        if fParse:
            if sorted_lines != '':
                hums = sorted_lines.split(' ')
                d_range = int(hums[0])
                s_range = int(hums[1])
                range_l = int(hums[2])
                for r in range(s_range,s_range+range_l):
                    humidity_data[temp_data.index(r)] = d_range + r - s_range
                print("Adding Humidity Data...", d_range, s_range, range_l)
                #print(humidity_data)
        if gParse:
            if sorted_lines != '':
                locs = sorted_lines.split(' ')
                d_range = int(locs[0])
                s_range = int(locs[1])
                range_l = int(locs[2])
                for r in range(s_range,s_range+range_l):
                    location_data[humidity_data.index(r)] = d_range + r - s_range
                print("Adding Location Data...", d_range, s_range, range_l)
                #print(location_data)
        #print(sorted_lines)
    
    outputfile = open("testdata/5out.txt", "w")
    outputfile.write('seed' + '\t' + 'soil' + '\t' + 'fert' + '\t' + 'water' + '\t' + 'light' + '\t' + 'temp' + '\t' + 'humi' + '\t' + 'loc' + '\n')
    outputfile.close

    for s in seed_list:
        outputfile = open("testdata/5out.txt", "a")
        outputfile.write(str(seed_list[s]) + '\t\t' + str(soil_data[s]) + '\t\t' + str(fert_data[s]) + 
                         '\t\t' + str(water_data[s]) + '\t\t' + str(light_data[s]) + '\t\t' + 
                         str(temp_data[s]) + '\t\t' + str(humidity_data[s]) + '\t\t' + str(location_data[s]) + '\n')
        outputfile.close

    for s in seeds:
        c = int(s)
        print("Seed", seed_list[c], "soil", soil_data[c], "fertilizer", fert_data[c], "water", water_data[c], 
          "light", light_data[c], "temperature", temp_data[c], "humidity", humidity_data[c], "location", location_data[c])

main()