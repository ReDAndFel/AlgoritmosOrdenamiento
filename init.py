import time
import services.AlgorithmsService as AS
import services.ArrayService as ArrS
import services.GraphsService as GS
import services.JsonService as JS

json_matrix_file_path = "./array.json"

#Se generan los array del caso 1 y 2. Descomentar si aun no los ha generado
#ArrS.exec()

for i in range(2):
    
    print(f"Vuelta del caso{i+1}")
    
    json_times_file_path = f"./times{i+1}.json"

    array = JS.read_json_array(json_matrix_file_path, i+1)
    
    # Se ejecuta el algoritmo BitonicSort
    start_time = time.time()
    array_result = AS.BitonicSort(array,len(array),True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"BitonicSort", elapsed_time)
    print("Tiempo de ejecución de BitonicSort:", elapsed_time, "segundos")
   
    # Se ejecuta el algoritmo ComboSort
    start_time = time.time()
    array_result = AS.CombSort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"CombSort", elapsed_time)
    print("Tiempo de ejecución de CombSort:", elapsed_time, "segundos")
    
    # Se ejecuta el algoritmo GmoneSort
    start_time = time.time()
    array_result = AS.GnomeSort(array,len(array))
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"GmoneSort", elapsed_time)
    print("Tiempo de ejecución de GmoneSort:", elapsed_time, "segundos")
    
    # Se ejecuta el algoritmo HeapSort
    start_time = time.time()
    array_result = AS.HeapSort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"HeapSort", elapsed_time)
    print("Tiempo de ejecución de HeapSort:", elapsed_time, "segundos")
        
    # Se ejecuta el algoritmo PigeonholeSort
    start_time = time.time()
    array_result = AS.PigeonholeSort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"PigeonholeSort", elapsed_time)
    print("Tiempo de ejecución de PigeonholeSort:", elapsed_time, "segundos")
        
    # Se ejecuta el algoritmo RadixSort1
    start_time = time.time()
    array_result = AS.RadixSort1(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"RadixSort1", elapsed_time)
    print("Tiempo de ejecución de RadixSort1:", elapsed_time, "segundos")
    
      # Se ejecuta el algoritmo RadixSort2
    start_time = time.time()
    array_result = AS.RadixSort2(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"RadixSort2", elapsed_time)
    print("Tiempo de ejecución de RadixSort2:", elapsed_time, "segundos")
     
    # Se ejecuta el algoritmo TimSort
    start_time = time.time()
    array_result = AS.TimSort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"TimSort", elapsed_time)
    print("Tiempo de ejecución de TimSort:", elapsed_time, "segundos")
    
    # Se ejecuta el algoritmo TreeSort
    start_time = time.time()
    array_result = AS.TreeSort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path,"TreeSort", elapsed_time)
    print("Tiempo de ejecución de TreeSort:", elapsed_time, "segundos")

GS.exec()