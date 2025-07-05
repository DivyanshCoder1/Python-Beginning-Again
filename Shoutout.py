import win32com.client as s
import time
people = ["Divyansh", "Shreyansh", "Gojo", "Ichigo"]

speaker = s.Dispatch("SAPI.Spvoice")

speaker.Speak("Hello")
for i in range(len(people)):
    speaker.Speak("Shoutout to")
    speaker.Speak(people[i])
