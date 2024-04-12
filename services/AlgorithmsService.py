from algoritmos.BitonicSort import sort
from algoritmos.CombSort import combSort
from algoritmos.GmoneSort import gnomeSort
from algoritmos.HeapSort import heapSort
from algoritmos.PigeonholeSort import pigeonhole_sort
from algoritmos.RadixSort1 import radixSort
#from algoritmos.RadixSort2 import sort
from algoritmos.TimSort import timSort
from algoritmos.TreeSort import treeins

def BitonicSort(array,N, up):
    return sort(array,N, up)

def CombSort(array):
    return combSort(array)

def GnomeSort(array,n):
    return gnomeSort(array,n)

def HeapSort(array):
    return heapSort(array)

def PigeonholeSort(array):
    return pigeonhole_sort(array)

def RadixSort1(array):
    return radixSort(array)

def TimSort(array):
    return timSort(array)

def TreeSort(array):
    return treeins(array)