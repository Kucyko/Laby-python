'''
with open("tadeusz.txt") as plik:
    for linia in plik:
        print (linia.strip().split())
'''
'''
with open('tadeusz.txt', 'r', encoding='UTF-8') as file:
    for index, line in enumerate(file, start=1):
        if index in [8, 12, 13]:
            print(f"Wiersz {index}: {line.strip()}")
'''
'''
import time
start=time.time()

stos1 = []
stos2 = []
stos3 = []
i=0
fo = open("foo.txt", "w")
for i in range(50000):
    stos1.append(i)
    i=i+1
    fo.writelines(str(i)+" ") 
    
koniec=time.time()
fo.close()
wykonanie=koniec-start
print(stos1)
print(wykonanie)
'''
'''
import time
start=time.time()

stos1 = []
stos2 = []
stos3 = []
i=0
with open('foo1.txt')as plik:
    for linia in plik:

        stos1.append(linia.strip().split())
    
koniec=time.time()

wykonanie=koniec-start
print(stos1)
print(wykonanie)
'''
import heapq
import timeit
numbers = [4, 10, 11, 5, 73, 5, 1]
# Sortowanie kopcowe
def heap_sort(arr):
    sorted_arr = []
    heapq.heapify(arr)
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

# Sortowanie szybkie
def quick_sort(arr):

    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return arr
# Dane wejściowe


# Sortowanie kopcowe
start_time = timeit.default_timer()
heap_sorted = heap_sort(numbers)
heap_execution_time = timeit.default_timer() - start_time

# Sortowanie szybkie
start_time = timeit.default_timer()
quick_sorted = quick_sort(numbers)
quick_execution_time = timeit.default_timer() - start_time

# Porównanie czasów wykonania
print("Sortowanie kopcowe:")
print("Posortowane liczby:", heap_sorted)
print("Czas wykonania:", heap_execution_time, "sekundy")
print()
print("Sortowanie szybkie:")
print("Posortowane liczby:", quick_sorted)
print("Czas wykonania:", quick_execution_time, "sekundy")

# Wczytywanie liczb z pliku
#file_name = "liczby.txt"
#with open(file_name, "r") as file:
#    numbers_from_file = [int(line) for line in file]

# Przykładowe sortowanie wczytanych liczb
#sorted_numbers_from_file = quick_sort(numbers_from_file)

# Zapis wyników do pliku
output_file_name = "wyniki.txt"
with open(output_file_name, "w") as file:
    file.write("Sortowanie kopcowe:\n")
    file.write("Posortowane liczby: " + str(heap_sorted) + "\n")
    file.write("Czas wykonania: " + str(heap_execution_time) + " sekundy\n\n")
    file.write("Sortowanie szybkie:\n")
    file.write("Posortowane liczby: " + str(quick_sorted) + "\n")
    file.write("Czas wykonania: " + str(quick_execution_time) + " sekundy\n")

