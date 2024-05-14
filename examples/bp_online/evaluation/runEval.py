import importlib
from get_instance import GetData
from evaluation  import Evaluation

eva = Evaluation()

capacity_list = [100,300,500]
#size_list = ['1k','5k','10k','100k']
size_list = ['1k','5k','10k']
with open("results.txt", "w") as file:
    for capacity in capacity_list:
        for size in size_list:
            getdate = GetData()
            instances, lb = getdate.get_instances(capacity, size)    
            heuristic_module = importlib.import_module("heuristic")
            heuristic = importlib.reload(heuristic_module)  
            
            for name, dataset in instances.items():
                
                avg_num_bins = -eva.evaluateGreedy(dataset,heuristic)
                excess = (avg_num_bins - lb[name]) / lb[name]
                
                result = f'{name}, {capacity}, Excess: {100 * excess:.2f}%'
                print(result)
                file.write(result + "\n")
 
