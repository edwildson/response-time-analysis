from tablib import Dataset

def analysis(data):
    data_to_analysis = data
    dataset = Dataset()
    imported_data = dataset.load(data_to_analysis.read(),format='xlsx')
    print(imported_data)

    for data in imported_data:
        print(data[1])