import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import webbrowser as wb

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate',150)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning !")

    elif hour >= 12 and hour < 17:
        say("Good Afternoon !")

    else:
        say("Good Evening !")

    say("how may i help you today")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.phrase_threshold = 0.3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return ""
    return query

def string_to_binary(string):
    binary_result = ""
    for char in string:
        binary_char = format(ord(char), '08b')  
        binary_result += binary_char + " "  
    return binary_result.strip()  

def add(a,b):
    return a+b

import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def words_to_numbers(text):
    # Dictionary mapping words to their numeric values
    number_words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10
    }
    # Replace numeric words with their numerical values
    for word, number in number_words.items():
        text = text.replace(word, str(number))
    return text



import requests

def get_weather(city):
    api_key = 'bb4f8785a03bce05c5e73aa18ae6a2c6'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:  # Check if the request was successful
        if 'main' in data:
            temp = data['main']['temp']
            return f"The temperature in {city} is {temp} degrees Celsius."
        else:
            return "Sorry, I couldn't retrieve the temperature information for that city. Please try again."
    else:
        return "Sorry, I couldn't retrieve the weather information at the moment. Please try again later."



if __name__=='__main__':
    greet()
    

    while True:
        command=takeCommand().lower()
        if "what is the time right now" in command:
            time=datetime.datetime.now().strftime("%I:%M %p")
            say(f"right know its {time}")

        elif "convert into binary" in command:
            say("Sure! Tell me what to convert into binary.")
            text = takeCommand()
            binary_code = string_to_binary(text)
            print(binary_code)
            say(f"this is the binary representation {text}")

        elif "add these two numbers" in command:
            say("sure! tell me that 2 numbers ")
            num1=int(takeCommand())
            num2=int(takeCommand())
            addthem=num1+num2
            say(f"sum of that 2 numbers is {addthem}")
            print(addthem)        

        elif "virat" in command:
            say("Virat Kohli is an Indian international cricketer and the former captain of the Indian national cricket team. He is a right-handed batsman and an occasional medium-fast bowler. He currently represents Royal Challengers Bengaluru in the IPL and Delhi in domestic cricket")

        elif " password" in command:
            say("Sure! Tell me the length of the password.")
            while True:
                length_input = takeCommand()
                length_input = words_to_numbers(length_input) 
                if length_input.isdigit():  # Check if the input is a digit
                    length = int(length_input)  # Convert the input to an integer
                    password = generate_password(length)
                    say(f"Your generated password is {password}")
                    print(password)
                    break
                else:
                    say("Please provide a valid number for the length.")

        elif "who are you"in command:
            say("i am your personal assistant")

        elif "weather" in command:
            say("Sure! Please tell me the city name.")
            city = takeCommand()
            weather_info = get_weather(city)
            print(weather_info)
            say(weather_info)

        elif "add two number" in command:
            print("a=10 \nb=20 \nprint(""sum of numbers is" ",a+b)")

        elif "open youtube" in command:
            wb.open("youtube.com")
            say("opening youtube!")

        elif "open google" in command:
            try:
                wb.Chrome.open("https://www.google.com")

            except Exception as e:
                say("sorry not able to open google")

        
        


        

        elif "exit"in command:
            say("goodbye sir..")
            break

