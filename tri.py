numbers = [6,5,3,1,8,7,2,4]

def tri_insertion1 (array):
    #init
    copy = []
    copy.append(array[0])

    #dev
    for i in range(1,len(array)):
    #for i in range(1,4):
        # i est le pointeur dans array
        len_copy = len(copy)
        print(len_copy)
        for j in range(len_copy):
            # j est le pointeur dans copy
            while array[i] > copy[j]:
                print('break')
                break
            if j == len(copy)-1 and copy[-1] < array[i]:
                copy.append(array[i])
            elif j == len(copy)-1 and copy[-1] > array[i]:
                copy.append(copy[-1])
                copy[-2] = array[i]
            else:
                print(copy)
                copy.append(copy[-1])
                for k in reversed(range(j, len(copy)-1)):
                   copy[k+1]=copy[k] 
                copy[j] = array[i]
    return copy

def tri_insertion2(array):
    copy = []
    copy.append(array[0])
    for i in range(1,len(array)):
        len_copy = len(copy)
        j = 0
        while len(copy) != len_copy+1:
            while array[i] > copy[j] and j != len(copy)-1:
                j += 1
            if j == len(copy):
                copy.append(array[i])
            elif copy[-1] < array[i]:
                copy.append(array[i])
            else:
                copy.append(copy[-1])
                for k in reversed(range(j, len(copy)-1)):
                   copy[k+1]=copy[k] 
                copy[j] = array[i]
    return copy

def tri_insertion3(tableau):
    for i in range(1, len(tableau)):
        element_a_inserer = tableau[i]
        j = i-1
        while j >= 0 and tableau[j] > element_a_inserer:
            tableau[j+1] = tableau[j]
            j -= 1
        tableau[j+1]= element_a_inserer
    return tableau

def bubble_sort(tableau):
    comparaison = 0
    while comparaison != len(tableau)-1:
        comparaison = 0
        for i in range(len(tableau)-1):
            if tableau[i] > tableau[i+1]:
                temp = tableau[i]
                tableau[i] = tableau[i+1]
                tableau[i+1] = temp
            else :
                comparaison += 1
    return tableau
print(bubble_sort(numbers))