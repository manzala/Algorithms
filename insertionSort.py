import timeit
import random

def insertion_sort(array):
    for element in range(0,len(array)):
        move_left(array,element)

def move_left(array,index):
    popValue = array.pop(index)
    while index!=0 and popValue<array[index-1]:
            index -= 1
    array.insert(index,popValue)


numbers = [4,7,3,8,1,12,9,14]
for x in range(0,5000):
    rand = random.randint(1,99999)
    numbers.append(rand)


start_time = timeit.default_timer()
insertion_sort(numbers)
elapsed_time = timeit. default_timer() - start_time
print("Insertion Sort: " + str(elapsed_time))

print(numbers)















