import random
letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='0123456789'
symbols='!@#$%^&*()_+'


print("Welcome to the PyPassword Generator!")   
noLetters=int(input("How many letters would you like in your password?\n")) 
noNumbers=int(input("How many numbers would you like?\n"))  
noSymbols=int(input("How many symbols would you like?\n"))      

# password=""

# for i in range(0,noLetters+1):
#     password+=random.choice(letters)
# for i in range(0,noNumbers+1):
#     password+=random.choice(numbers)    
# for i in range(0,noSymbols+1):  
#     password+=random.choice(symbols)    

# print(password)


passwordList=[]
for i in range(0,noLetters+1):
    passwordList.append(random.choice(letters))
for i in range(0,noNumbers+1):
    passwordList.append(random.choice(numbers))
for i in range(0,noSymbols+1):
    passwordList.append(random.choice(symbols)) 
random.shuffle(passwordList)
password=""
for char in passwordList:
    password+=char  
print(passwordList) 
print(f"Your password is: {password}")







