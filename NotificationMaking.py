from notifypy import Notify

notification = Notify()


notification.title = "DRINK WATER!!"
notification.message = "Please drink water, it has been 2 hours!!"
notification.application_name = "Drink Water Notifier"
notification.icon = "drop.png"

notification.send()
