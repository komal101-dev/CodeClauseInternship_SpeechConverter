print("Helloo guys!!")
import pyttsx3
speech=pyttsx3.init()
input=input("what you want to do")
speech.say(input)
speech.runAndWait()

