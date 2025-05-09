# NLTK- Natural Language Processing Toolkit
from nltk.chat.util import Chat, reflections

# We create user inputs and Bot responses Pairs
pairs = [
    (r"hi|hello|hey",["Hello, How are you","Hi, Thanks for checking","Hi, How can I assist you","I'm Good, how about you"]),
    (r"How are you",["I'm doing great", "I am doing great","Good Can be of help"]),
    (r"(.*)program(.*)" ,["We offer Software development courses. Reply with android, web to get full description"]),
    (r"(.*)android(.*)" ,["Android program offers students with hando practcal in creating mobile apps."]),
    (r"(.*)web(.*)" ,["Web Development offers students with web dev skills in HTML/CSS/BOOTSRAP/REACT/JS"]),
    (r"(.*)full{\s?}stack(.*)" ,["Web provide Full Stack Training, You wi;; learn frontend and backend"]),
    (r"(.*)back\s?end(.*)" ,["Web provide Full Stack Training, You wi;; learn frontend and backend"]),
    (r"(.*)front\s?end(.*)" ,["Web provide Full Stack Training, You wi;; learn frontend and backend"]),
    (r"(.*)(join|enroll|register)(.*)", ["Yes, you can join us! Please follow the link below."]),
    (r"(.*)intake(.*)", ["We have our january and may intake, for mor information please call +254789012345 and book a spot"]),
    (r"(.*)(mobile|apps|applications|mobile\s?apps|mobile-apps)(.*)", ["We do mobile development in android"]),



    (r"(.*)", ["I didn't catch that", "I can't uanderstand","Please clarify","Pardon me"])


]
 

# Initialize/Start the bot
chatbot = Chat(pairs,reflections)
print("Hello,I am Kimari.\nHow can I help you. Type 'quit' to exit")


# We use a loop to have a continious conversation with the Bot
while True:
    user_input = input("You:")
    if user_input.lower() == "quit":
        print("Goodbye, See you soon.")
        break
    else:
        response = chatbot.respond(user_input)
        print("Kimari", response)