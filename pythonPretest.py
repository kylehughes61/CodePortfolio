#The code in this text file comes from a group submission for a
# scrum-style entry exam to a second-level Python class offered by
# Red Rocks Community College. It is not indicative of any relevant
# skills or experience, and is intended as a placeholder while I set
# up a Portfolio Repository.

def math(funcType):
    numA = int(input('What is the first number? '))
    numB = int(input('What is the second number? '))
    if funcType == 'add':
        return numA + numB
    elif funcType == 'subtract':        #The if/elif statements were
        return numA - numB              # used to cover the if/nested
    elif funcType == 'multiply':        # if part of the assignment. 
        return numA * numB              # User input was implemented
    elif funcType == 'divide':          # afterwards with help from
        return numA / numB              # the group.
    else:
        print('Error: Function type undefined')
        return
    
    #The first function was written by Kyle on day one, before
    # we decided to work on the rest of the project as a group.
    # This was done because our group had similar gaps in our
    # knowledge (nobody knew how to write files), and it was
    # deemed unfair to make one member do the code for the more
    # difficult functions.

def tuples():
    minimum = int(input('What is the low number? '))
    maximum = int(input('What is the maximum number? '))
    average = int(input('What is the average? '))
    print('Min: %d, Max: %d, Avg: %d' %(minimum, maximum, average))

    #The tuples function was written with our final function in
    # mind; this way it would be easier to implement when we
    # reached that part of the assignment.
    
def nests(inputVar):
    numA = int(input('What is the first number? '))
    numB = int(input('What is the second number? '))
    if numA == inputVar or numB == inputVar:
        print('One of your numbers is exactly the input variable.')
    elif numA > inputVar:
        if numB > inputVar:
            print('The numbers you chose are both larger than the reference.')
        elif numB < inputVar:
            print('One number is greater than the reference, the other is less.')
    elif numB > inputVar:
        if numA < inputVar:
            print('One number is greater than the reference, the other is less.')
    elif numA < inputVar:
        if numB < inputVar:
            print('The numbers you chose are both smaller than the reference.')
    else:
        print('Error: this escapes my logic!')

    #The nested if function works as a guessing game where
    # the user tries to guess the input variable (chosen as the
    # function argument). It can not be played twice, because
    # we knew we had to make a different function using loops.

def loops():
    num = int(input('Choose an ineger: '))  #The loops function uses a
    i = 0                                   # single while loop to print
    while i <= num:                         # all integers below the
        print('%d ' %i, end='')             # user input integer.
        i += 1

def strings():
    str1 = input('Enter a first name: ')    #The strings function will
    str2 = input('Enter a last name: ')     # concatenate the first and
    str1 = str1 + ' ' +str2                 # last names given from user
    print(str1)                             # input.

def dictionaries():
    ourDict = { 'Brand': '', 'Model': '', 'Year': '' }
    ourDict['Brand'] = input('Name a brand of a car: ')
    ourDict['Model'] = input('Name a model made by %s: ' %ourDict['Brand'])
    ourDict['Year'] = input('Choose a recent year: ')
    print(ourDict)

    #Our dictionaries function required user input, so we created
    # a dictionary for a car model, and let the user enter the
    # car's information.

def files():
    try:
        open("newfile.dat", "w")
    except:
        print('There was an error with the chosen file.')
    fVar = open("newfile.dat", "w")
    fVar.write(input('Please enter the content of the file: '))
    fVar.close()
    fVar = open("newfile.dat", "r")
    print(fVar.read() + ' from file newfile.dat')
    
    #The files function creates and opens a new file, newfile.dat,
    # then checks for errors. If there aren't any, the function
    # will ask the user to populate the file, then will read the
    # updated file.

def main():
    varList = [0, 0, 0, 0, 0]
    i = 1
    while i <= 5:
        varList[i - 1] = int(input('Enter number %d: ' %(i)))
        i += 1
    print(varList)

main()