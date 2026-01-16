import random
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
characters = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':',"'",'"',',','<','>','.','?','/','~','`']
a=int(input("how many aphabets you want...."))
b=int(input("how many numbers you want to use....."))
c=int(input("how many special characters you want to use...."))
password=[]
for x in range(0,a):
    password.append(random.choice(alphabets))
for y in range(0,b):
    password.append(random.choice(numbers))
for z in range(0,c):
    password.append(random.choice(characters))
t=len(password)
password1=""
for p in range(0,t):
    password1+=random.choice(password)
print(password1)
    

