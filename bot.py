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
def joke():
    jokes = ["I ate a clock yesterday, it was very time-consuming."," I failed math so many times at school, I can’t even count.","I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.","Most people are shocked when they find out how bad I am as an electrician.","Just burned 2,000 calories. That’s the last time I leave brownies in the oven while I nap."]
    print(random.choice(jokes))
