from math import ceil
from multiprocessing.spawn import import_main_path
from tablib import Dataset
from django.contrib.messages import constants as messages

def analysis(data):
    data_to_analysis = data
    dataset = Dataset()
    imported_data = dataset.load(data_to_analysis.read(),format='xlsx')
    sucess = True
    for (index, data) in enumerate(imported_data):
        print(index, data)
    

    response_time_dict = {}

    U = 0

    # print('Coluna J: ' ,imported_data['J'])
    # Checa se possue Jitter

    jitter = False
    for j in imported_data['J']:
        if j is not None and j > 0:
            jitter = True
        

    for (index, data) in enumerate(imported_data):
        if data[3] is not None and data[1] is not None:
            U += data[3]/data[1]
        else:
            print("wtf")
            U = -1
            continue
            # del imported_data[index]
            

    if U <= 1 and U > 0:
        print("opa")
        if jitter is False:
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

                        if r > data[2]:
                            return {
                                "table": imported_data, "data": response_time_dict.values(), "status": messages.ERROR, "message": "Tarefa não é escalonável."
                            }  
                            # return data[0] + " não escalonável"
                        if r == response_time_dict[index][-2]:
                            print("Tarefa ", index+1, " ok")
                            break


                    counter += 1
                print("passou do while")
                print(response_time_dict) 
                
            return {
                "table": imported_data, "data": response_time_dict.values(), "message": "Tarefas escalonáveis", "status": messages.SUCCESS
            }  
        else:
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
                            sum+= ceil((response_time_dict[index][j]+imported_data[i][4]) / imported_data[i][1]) * imported_data[i][3]

                        
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

                        # if r+data[4] > data[2]:
                        #     response_time_dict[index].append(r+data[4])
                        #     return {
                        #         "table": imported_data, "data": response_time_dict.values(), "status": messages.ERROR, "message": "Tarefa não é escalonável."
                        #     }  
                        #     # return data[0] + " não escalonável"
                        if r == response_time_dict[index][-2]:
                            
                            response_time_dict[index].append(r+data[4])
                            if r+data[4] > data[2]:
                                sucess = False
                            break


                    counter += 1
                print("passou do while")
                print(response_time_dict) 
                
            return {
                "table": imported_data, "data": response_time_dict.values(), "message": "Tarefas escalonáveis" if sucess else "Tarefas não escalonáveis", "status": messages.SUCCESS if sucess else messages.ERROR
            }  

    else:
        return {
           "table": imported_data, "data": {}, "status": messages.ERROR, "message": "Tarefas não escalonáveis, pois U>1."
        }  

