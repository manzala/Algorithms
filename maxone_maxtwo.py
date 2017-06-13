

def maxone_maxtwo(array):
    max = 0
    max_two = 0
    for element in range(0,len(array)):
        if max < array[element]:
            max_two = max
            max = array[element]

        elif max_two < array[element]: #keeps the loop going
            max_two = array[element]

    return max_two,max






array=[2,4,9,4,20,666,45,55]

print maxone_maxtwo(array)[0]
print maxone_maxtwo(array)[1]



