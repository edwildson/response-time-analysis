from math import ceil
from multiprocessing.spawn import import_main_path
from urllib import response
from tablib import Dataset
from django.http import JsonResponse 

def analysis(data):
    data_to_analysis = data
    dataset = Dataset()
    imported_data = dataset.load(data_to_analysis.read(),format='xlsx')
    for (index, data) in enumerate(imported_data):
        print(index, data)
    

    response_time_dict = {}

    U = 0

    for data in imported_data:
        if None not in data:
            U += data[3]/data[1]
        else:
            del imported_data[-1]
            

    if U <= 1:
        for (index, data) in enumerate(imported_data):
            response_time_dict[index] = []
            counter = 0
            print("Tarefa ", index+1, "\n")
            if not index:
                response_time_dict[index] = [data[3]]
                continue
            j=0
            while True :
                # j = 0
                if not counter:
                    print("Primeira iteração")
                    print("sum: ", data[3])
                    response_time_dict[index] = [data[3]]            

                else:
                    print(counter+1, " iteração")
                    
                    sum = 0
                
                    print("Percorrendo o conjunto")
                    print("j: ", j, "\ncounter:", counter)
                    
                    for i in range (index):
                        sum+= ceil(response_time_dict[index][j] / imported_data[i][1]) * imported_data[i][3]

                    
                    print("sum: ", sum)
                    j+=1
                    r = data[3] + sum
                    print("Valor adicionado no array: ", r)
                    response_time_dict[index].append(r)
                    
                # for j in range(index):
                #     print("Percorrendo o conjunto")
                #     print("j: ", j, "\ncounter:", counter)
                #     print(response_time_dict[index])
                #     print(response_time_dict[index][j])
                #     sum += ceil(response_time_dict[index][j] / imported_data[j][1]) * imported_data[j][3]
                #     j+=1
                #     r = data[3] + sum
                #     print("Valor adicionado no array: ", r)
                #     response_time_dict[index].append(r)
                
                # r = data[3] + sum
                # print("Valor adicionado no array: ", r)
                # response_time_dict[index].append(r)

                    if r == response_time_dict[index][-2]:
                        print("Tarefa ", index+1, " ok")
                        break

                    if r > data[2]:
                        return {
                            "data": response_time_dict, "status": "fail", "msg": "Atividade " + index+1 + "não é escalonável."
                        }  
                        # return data[0] + " não escalonável"

                counter += 1
            print("passou do while")
        print(response_time_dict) 
        
        return {
            "table": imported_data, "data": response_time_dict.values(), "status": "ok"
        }    
    else:
        return {
            "data": {}, "status": "fail", "msg": "Atividade " + index+1 + "não é escalonável."
        }  

