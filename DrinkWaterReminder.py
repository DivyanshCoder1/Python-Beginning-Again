from notifypy import Notify
import time
import winsound

notification = Notify()

while True:
    notification.title = "DRINK WATER!!"
    notification.message = "Please drink water, it has been 2 hours!!"
    notification.application_name = "Drink Water Notifier"
    notification.icon = "drop.png"
    winsound.Beep(2000, 1500)
    notification.send()
    time.sleep(7200)