#This asks the user to input the number of 4-tuples in its subset.
num_tuple = int(input("How many 4-tuples are you going to input? "))
lst = []

"""This for loop asks the user to input the 4-tuples in a straight line as SPACE SEPARATED INTEGERS.
eg of User Input: 0 0 0 0 
                  0 0 0 1
                  and so on....
    Then it stores each 4-tuple inputed by the user in a new list - 'lst'. """
for i in range(num_tuple):
    lst.append([str(x) for x in input("Input the elements of your 4-tuple in a straight line with spaces i.e. as SPACE SEPARATED INTEGERS: ").split()])

#Error Handling for if the user inputs a n-tuple wherein n != 4 or if any of the elements of the tuple is not 0 or 1.
count = 0
for i in range(len(lst)):
    if (len(lst[i]) != 4):
        count += 1
    for j in range(len(lst[i])):
        a = lst[i][j]
        if (a != '1') and (a != '0'):
            count += 1

#Count is number of errors in user input and if count != 0 then it will ask you to re-run the program.
if count != 0:
    print("User Input is incorrect, please re-run the program.")
else:
    #This For Loop performs the addition operation on the subset with each 4-tuple of the subset.
    res1 = []
    for j in range(len(lst)):
        for k in range(len(lst)):
            tup = ()
            for h in range(4):
                #The addition operation's Truth Table is akin to XOR gate which is why each of the 2 elements of the tuple are XORed with each other.
                a = (int(lst[j][h])) ^ (int(lst[k][h]))
                #The resultant elements are added to a tuple which is then appended to a new list res1. 
                tup += tuple(list(str(a)))
            res1.append(tup)

    #This converts each stored 4-tuple resulting from the XOR operation as a 4-element list.
    for i in range(len(res1)):
        res1[i] = list(res1[i])

    #This For Loop performs the AND operation with 0 and each of the 4-tuple.
    res2 = []
    for j in range(len(lst)):
        tup = ()
        for k in range(len(lst[j])):
            a = 0 and (int(lst[j][k]))
            tup += tuple(list(str(a)))
        #Then stores the resulting tuple in a new list res2.
        res2.append(tup)

    #This For Loop performs the AND operation with 1 and each of the 4-tuple.
    for j in range(len(lst)):
        tup = ()
        for k in range(len(lst[j])):
            a = 1 and (int(lst[j][k]))
            tup += tuple(list(str(a)))
        #Then stores the resulting tuple in a new list res2.
        res2.append(tup)

    #This converts each stored 4-tuple resulting from the AND operation with 0 and 1 as a 4-element list.
    for i in range(len(res2)):
        res2[i] = list(res2[i])


    """This function then checks res1 and res2 if every 4 tuple is same as those inputted into the subset. If it fails anywhere,
    it returns FALSE. Else it returns TRUE."""
    def Subspace(res1, res2):
        for i in res1:
            if i not in lst:
                return 'FALSE'
        for i in res2:
            if i not in lst:
                return 'FALSE'

        return 'TRUE'

    print(Subspace(res1, res2))