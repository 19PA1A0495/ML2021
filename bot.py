import datetime
import random

def greeting():
    Help_desk = [
        "Hi ! Iam Boomer. I'm here to help you. May i know your name.",
        "Wonderful, It is so nice to be in touch with you. I'm Boomer....."
    ]
    print(random.choice(Help_desk))

def wish(name):
    time_now = datetime.datetime.now().hour
    if time_now < 12:
        print(f"It's nice to meet you {name}, Good morning")
    elif time_now > 12 and time_now < 17:
        print(f"It's nice to meet you {name}, Good afternoon")
    elif time_now > 18:
        print(f"It's nice to meet you {name}, Good evening")

def welcome(name):
    messages = [
        f"U can make ur work easier with my help {name}, what are u searching for?",
        f"Lets have some good time together, I can help u to search courses or we can have some fun {name}."
    ]
    print(random.choice(messages))

def show_menu():
    print("How can I help you? :")
    print("1. Could you give some suggestions about courses to learn?")
    print("2. Calculate my age")
    print("3. Crack a joke for me")
    print("4. End my session")
    try:
        return int(input("Enter your choice: "))
    except Exception:
        print("Enter a valid option")

def tenth():
    print("Please help me understand about you!")
    print("Have you completed tenth?")
    print("1. Yes")
    print("2. No or Failed")
    try:
        t = int(input("Have you completed tenth? :"))
        if t<1 or t>2:
            print("Sorry I didn't get that")
            print("----------------------------------")
        else:
            return t
    except Exception:
        print("Enter a valid option")

def tenth_qualified():
    tenth_completed = tenth()
    if tenth_completed == 1:
        return True
    elif tenth_completed == 2:
        print("Sorry you have to complete tenth first!!")
        print("-----------------------------------------")
        
def twelth():
    if tenth_qualified():
        print("Have you completed you twelfth? ")
        print("1. Yes or persuing deploma")
        print("2. No or Failed")
        try:
            re =  int(input("Have you completed your twelth? :"))
            if re <1 or re > 2:
                print("Sorry I didn't get that")
                print("-----------------------------------------")
            else:
                return re
        except Exception:
            print("Enter a valid choice")

def stream():
    twelfth_completion = twelth()
    if twelfth_completion == 1:
        print("Which stream are you in twelth? :")
        print("1. MPC")
        print("2. BiPC")
        print("3. CEC")
        print("4. HEC")
        print("5. Diploma persuing")
        try:
            st =  int(input("Enter your stream: "))
            if st<1 or st>5:
                print("Sorry I didn't get that")
                print("-------------------------------")
            else:
                return st
        except Exception:
            print("Enter valid option")
    elif twelfth_completion == 2:
        print("We have some courses for tenth complted students too....")
        print("1. Basic English skills")
        print("2. Trignometry")
        print("3. Indian history")
        print("4. Harappan civilization")
        print("---------------------------------------------")
        
def joke():
    jokes = ["I ate a clock yesterday, it was very time-consuming."," I failed math so many times at school, I can’t even count.","I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.","Most people are shocked when they find out how bad I am as an electrician.","Just burned 2,000 calories. That’s the last time I leave brownies in the oven while I nap."]
    print(random.choice(jokes))
    
def boomer():
    greeting()
    name = input("Enter your name: ")
    wish(name)
    welcome(name)
    choice = show_menu()
    while choice != 4:
        if choice == 1:
            suggestions()
        elif choice == 2:
            age = age_calculation()
            print(f"Your age is {age}. Remeber age is just a number :-) ")
        elif choice == 3:
            joke()
        else:
            print("Sorry I didn't get that!!")
        choice = show_menu()
    if choice == 4: 
        print(f"All the best for your future {name}, good bye :-) ")

boomer()
