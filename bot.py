"""
This is a program for chatbot to give suggestions for online courses.
1. The chatbot name is boomer.
2. The bommer will start with a greeting and self intro and ask for name of the person .
3. The bommer give suggestions of courses for 10th and secondary standard students.
4. Bommer will calculate ur age .
5. Bommer will crack a joke and finally the bot ends.
"""
import datetime
import random

def greeting():
    # Greets the user and introduces itself.
    Help_desk = [
        "Hi ! Iam Boomer. I'm here to help you. May i know your name.",
        "Wonderful, It is so nice to be in touch with you. I'm Boomer....."
    ]
    print(random.choice(Help_desk))

def wish(name):
    # Wishes the user according to the time
    time_now = datetime.datetime.now().hour
    if time_now < 12:
        print(f"It's nice to meet you {name}, Good morning")
    elif time_now > 12 and time_now < 17:
        print(f"It's nice to meet you {name}, Good afternoon")
    elif time_now > 18:
        print(f"It's nice to meet you {name}, Good evening")

def welcome(name):
    # Wellcomes the use
    messages = [
        f"U can make ur work easier with my help {name}, what are u searching for?",
        f"Lets have some good time together, I can help u to search courses or we can have some fun {name}."
    ]
    print(random.choice(messages))

def show_menu():
    # Display menu for the user to select the action of the bot.
    print("How can I help you? :")
    print("1. Could you give some suggestions about courses to learn?")
    print("2. Calculate my age")
    print("3. Crack a joke for me")
    print("4. End my session")
    try:
        return int(input("Enter your choice: ")) # Returns the choice of the user.
    except Exception:
        print("Enter a valid option")

def tenth():
    # Asking the input the user whether he completed his 10th or not.
    print("Please help me understand about you!")
    print("Have you completed tenth?")
    print("1. Yes")
    print("2. No or Failed")
    try:
        tenth_choice = int(input("Have you completed tenth? :"))
        if tenth_choice<1 or tenth_choice>2:
            print("Sorry I didn't get that")
            print("----------------------------------")
        else:
            return tenth_choice
    except Exception:
        print("Enter a valid option")

def tenth_qualified():
    # If the user completed his tenth it returns True.
    tenth_completed = tenth()
    if tenth_completed == 1:
        return True
    elif tenth_completed == 2: 
        print("Sorry you have to complete tenth first!!")
        print("-----------------------------------------")
        
def twelth():
    # If the user completed his tenth, it asks the user twelfth whether he completed twelfth or not.
    if tenth_qualified():
        print("Have you completed you twelfth? ")
        print("1. Yes or persuing deploma")
        print("2. No or Failed")
        try:
            twelfth_choice =  int(input("Have you completed your twelth? :"))
            if twelfth_choice <1 or twelfth_choice > 2:
                print("Sorry I didn't get that")
                print("-----------------------------------------")
            else:
                return twelfth_choice
        except Exception:
            print("Enter a valid choice")

def stream(): 
    # If the user completed his tenth, it asks his stream in twelfth. If not it will suggest some after tenth courses.
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
        # Courses for 10th completed students.
        print("We have some courses for tenth complted students too....")
        print("1. Basic English skills")
        print("2. Trignometry")
        print("3. Indian history")
        print("4. Harappan civilization")
        print("---------------------------------------------")
def suggestions():
    # Based on the stream the user selected, it will suggest a few online courses.
    twelth_stream = stream()
    if twelth_stream == 1:
        print("In this pandemic situation, we have to utlize this time for improving knowledge.")
        print("I will suggest you some courses....")
        print("For MPC, you an prefer courses like: ")
        print("1. Basics of Programming")
        print("2. Basis of Electronics")
        print("3. Intro to Designing")
        print("4. Basics of Web development")
        print("--------------------------------------")
    elif twelth_stream == 2:
        print("In this pandemic situation, we have to utlize this time for improving knowledge.")
        print("I will suggest you some courses....")
        print("For BiPC, you can prefer courses like: ")
        print("1. Know about Anatomy")
        print("2. Intro to Bio Chemistry")
        print("3. Agriculture Development")
        print("4. Intro to Botany")
        print("--------------------------------------")
    elif twelth_stream == 3:
        print("In this pandemic situation, we have to utlize this time for improving knowledge.")
        print("I will suggest you some courses....")
        print("For CEC, you can prefer courses like: ")
        print("1. Public policy analysis")
        print("2. Society and media")
        print("3. Numerical analysis")
        print("4. Corporate law")
        print("--------------------------------------")
    elif twelth_stream == 4:
        print("In this pandemic situation, we have to utlize this time for improving knowledge.")
        print("I will suggest you some courses....")
        print("For HEC, you can prefer courses like: ")
        print("1. Applied business analytics")
        print("2. Enterpreneur strategies")
        print("3. Business model innovations")
        print("4. Strategic management of innovations")
        print("---------------------------------------")
    elif twelth_stream == 5:
        print("In this pandemic situation, we have to utlize this time for improving knowledge.")
        print("I will suggest you some courses....")
        print("For Diploma, you can prefer courses like: ")
        print("1. Programming basics")
        print("2. Foundations of data structures")
        print("3. Basic electronics")
        print("4. Analog circuits")
        print("-----------------------------------------")
        
def joke():
    # Cracks a joke when the user selected that action.
    jokes = ["I ate a clock yesterday, it was very time-consuming."," I failed math so many times at school, I can’t even count.","I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.","Most people are shocked when they find out how bad I am as an electrician.","Just burned 2,000 calories. That’s the last time I leave brownies in the oven while I nap."]
    print(random.choice(jokes))
    
def age_calculation():
    # Calculates the age of the user by taking birth date, birth year and birth month as input from the user.
    today_date = datetime.date.today()
    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month: "))
        date = int(input("Enter your birth date: "))
        birth_day = datetime.date(year,month,date)
        age = today_date.year - birth_day.year
        if age < 0:
            print("Enter valid date")
        else:
            return age
    except Exception:
        print("Enter valid input")
    
def boomer():
    # Out bot function
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
