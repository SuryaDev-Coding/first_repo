def armstrong(num):
    original = num
    total = 0
    n = len(str(num))
    while(num):
        digit = num%10
        total += digit**n
        num //= 10
    return(original==total)


def automorphic(num):
    ''' To check for auto morphic 

    1. Mathematical method
    square = str(num*num)
    countofdigit = len(str(num))
    total = 0
    for i in range(0,countofdigit):
        total += (10**i) * (square%10)
        square //=10

    2. String Way
    n = len(str(num))
    total = square[-n:]
    if total == str(num):
        return True
    else:
        return False

    3. Built In function    '''
    return str(num*num).endswith(str(num))

def kaprekar(num):
    iskaprekar = False
    square = num**2
    i = 0
    test = 0
    while(square):
        digit = square%10
        digit *= (10**i)
        test += digit
        square//=10
        total = test + square
        if total == num:
            iskaprekar = True
            break
        i+=1
    return iskaprekar

def palindrome(num):

    '''original = num
    total = 0
    while(num!=0):
        digit = num%10
        total += digit
        total*=10
        num//=10
    if(original==total):
        print("palidrome")'''
    string = str(num)
    return(string==string[::-1])

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

functions = {1: armstrong,
             2: automorphic, 
             3: kaprekar, 
             4: palindrome}
while(True):
    choice = get_int('''
      -----MENU-----
      1. Armstrong
      2. Automorphic
      3 Kaprekar
      4. Palindrome
      5. Quit
      ''')
    if choice == 5:
        break
    
    if choice not in functions:
        print("Enter Valid Choice!! ")
        continue
    check_function = functions[choice]
    option = input('''
    A. Check if a number posses this property
    B. Find all numbers of n digit which posses this property''').upper()
    
    if(option=='A'):
        num = get_int("Enter a number: ")
        print('\nResult\n','Yes' if check_function(num) else 'No')

    elif(option=='B'):
        n = get_int("Enter number of digits: ")
        if n > 6:
            print('n is too large \n Try n<=6')
            continue
        if n<=0:
            print('n cannot zero or negative \n Try n>0')
        start = 10**(n-1)
        stop = 10**n
        sequence = [i for i in range(start,stop) if check_function(i)]
        print(f"Found {len(sequence)} numbers")
        print(f"\nThe sequence of {n} digit number which satisfy this property\n",sequence)

    else:
        print("Invalid Choice")
'''



'''