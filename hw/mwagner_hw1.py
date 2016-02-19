# Max Wagner

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    # bubble/selection sort for laziness
    input = list(input)
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[j] < input[i]:
                input[j], input[i] = input[i], input[j]
    return input
	
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input): 
    return sorted(input)

#3. fill in this function
#   it takes a list for input and a value to search for
#   it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    for i in range(len(input)):
        if i == value:
            return True
    return False

#4. fill in this function
#   it takes a list for input and a value to search for
#   it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input	

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
