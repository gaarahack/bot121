import warnings
import pywhatkit
import speech_recognition as sr
import pyttsx3 as tts

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

speaker.say("hey there, iam rusty i am a personal assistant\n")
speaker.runAndWait()
speaker.say("what is your name")
speaker.runAndWait()
user = input()

print("here are things in which i can help you\n"
      "1.playing your fav songs on youtube.\n"
      "2.sending messages on whatsapp.\n"
      "3.performing google search.\n"
      "4.Get information on a particular topic.")

speaker.say("here are things in which i can help you"
            "1.playing your fav songs on yt.\n"
            "2.sending messages on whatsapp.\n"
            "3.performing google search.\n"
            "4.Get information on a particular topic.")
speaker.runAndWait()

selection = int(input("what do you like me to do?\n"
                      "1 -> for playing on youtube\n"
                      "2 -> for sending messages whatsapp\n"
                      "3 -> for google search\n"
                      "4 -> for information on particular topic"))

if selection == 1:
    speaker.say(f"what song do like to listen {user} ?")
    speaker.runAndWait()
    song = input(f">>>what song do like to listen {user} ?\n")
    pywhatkit.playonyt(song)
    print("Playing...")

elif selection == 3:
    speaker.say(f"On which topic you need information just type the keyword {user} ?")
    speaker.runAndWait()
    keywords = input("On which topic you need information just type the keyword")
    pywhatkit.search(keywords)
    print("Searching...")

elif selection == 4:
    speaker.say(f"On what topic you need information{user} ?")
    speaker.runAndWait()
    topicc = input(f"On what topic you need information {user}. ")
    speaker.say(f"how many lines you need regarding the topic{user} ?")
    speaker.runAndWait()
    lines = int(input(f"how many lines you need regarding the topic {user}. "))
    pywhatkit.info(topicc, lines=lines)
    print("\nSuccessfully Searched")

elif selection == 2:
    num = int(input("choose the number to send message"))
    message = input("text the message to send")
    hour = int(input("choose the hour to send "))
    minn = int(input("choose the minutes to send"))
    pywhatkit.sendwhatmsg(f"+91{num}",
                          message,
                          hour, minn)
    print("Successfully Sent!")

# API_KEY = "f9add44c5070911e729580a7ec7521a4"
