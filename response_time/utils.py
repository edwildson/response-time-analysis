from math import ceil
from tablib import Dataset

def analysis(data):
    data_to_analysis = data
    dataset = Dataset()
    imported_data = dataset.load(data_to_analysis.read(),format='xlsx')
    print(imported_data)

    response_time_dict = {}

    for (index, data) in enumerate(imported_data):
        response_time_dict[index] = []
        counter = 0
        if not index:
            response_time_dict[index] = [data[3]]
            print("Index 0")
            continue

        while True :
            print(counter)
            if not counter:
                response_time_dict[index] = [data[3]]            

            else:
                j = 0
                sum = 0
                while j < index: 
                    # print("Percorrendo o conjunto")
                    print(j)
                    sum += ceil(response_time_dict[index][j] / imported_data[j][1]) * imported_data[j][3]
                
                r = data[3] + sum
                response_time_dict[index].extend(r)

                if r == response_time_dict[index][-2]:
                    break

                if r > data[2]:
                    return data[0] + " não escalonável"

            counter += 1
    print(response_time_dict)    

