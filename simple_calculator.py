#addition/subtraction
#division/modulous
#trigonometry(sin,cos,tan)
#multiplication/exponentials
print(('''calculation_actions in this program are:exponentials,logarithms,trigonometry,addition,subtraction,division,modulus and multiplication
NOTE THE SPELLING!!'''))
print("")
calculator=str(input("enter the calculation action you need: "))
#action1=("trigonometry")
action2=("division")
action3=("multiplication")
action4=("modulus")
action5=("subtraction")
action6=("addition")
action7=("exponentials")
if calculator=="trigonometry":
    pass
elif calculator=="logarithms":
    pass
else:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    action6=number1+number2
    action4=number1%number2
    action2=number1/number2
    action5=number1-number2
    action3=number1*number2
    action7=number1**number2

if calculator=="division":
    print("your quotient is: " ,action2)
elif calculator=="multiplication":
    print("your product is: " ,action3)
elif calculator == "addition":
    print("your sum is: " ,action6)
elif calculator == "modulus":
    print("your remainder is: " ,action4)
elif calculator == "subtraction":
    print("your difference is: " ,action5)
elif calculator == " exponentials":
    print("your result is: " ,action7)
elif calculator=="trigonometry":
    trig=str(input("enter trigonometry method: "))
    import math
    x = int(input("enter the number: "))
    if trig=="sin":
        math.sin(x)
        print(math.sin(x))
        print("the answer is in RADIANS!")
    elif trig == "tan":
        math.tan(x)
        print(math.tan(x))
        print("the answer is in RADIANS!")
    elif trig == "cos":
        math.cos(x)
        print(math.cos(x))
        print("the answer is in RADIANS!")
    else:
        print('''check your trigonometry method and re_run the program!
        THANK YOU''')
elif calculator=="logarithms":
    import math
    y= int(input("enter the number:"))
    math.log(y, 10)
    print("log of",y ,"in base of 10 is:", math.log(y, 10))
else:
    import time
    print("wait about 6 seconds as we find your method...")
    for seconds in range(6,0,-1):
        print(seconds)
        time.sleep(1)
    print('''THE METHOD YOU ENTERED IS UNAVAILABLE FOR NOW,WE'RE WOKRING ON THAT...
    
                    THANK YOU!''')