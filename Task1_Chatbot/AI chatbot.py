import datetime
import random

def greet():
    return "Hello! 😊 How can I help you today?"

def get_time():
    now = datetime.datetime.now()
    return "Current time is " + now.strftime("%H:%M:%S")

def get_date():
    today = datetime.date.today()
    return "Today's date is " + today.strftime("%d-%m-%Y")

def tell_joke():
    jokes = [
        "Why did the computer go to the doctor? Because it caught a virus! 😂",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why was the computer cold? It forgot to close its Windows! 🪟"
    ]
    return random.choice(jokes)

def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot:", greet())

        # How are you
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")

        # Name
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm your friendly chatbot!")

        # Time
        elif "time" in user_input:
            print("🤖 Chatbot:", get_time())

        # Date
        elif "date" in user_input:
            print("🤖 Chatbot:", get_date())

        # Joke
        elif "joke" in user_input:
            print("🤖 Chatbot:", tell_joke())

        # Help
        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about time, date, jokes, or just chat!")

        # Exit
        elif "bye" in user_input or "exit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day 😄")
            break

        # Unknown input
        else:
            print("🤖 Chatbot: Hmm... I didn't understand that. Try asking something else!")

# Run chatbot
chatbot()