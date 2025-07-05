fr = open("PythonPracticeSheet-9\DonkeyFile.txt", "r")
content = fr.read()

previous = "donkey"
new = "######"

final = content.lower().replace(previous, new)

fw = open("PythonPracticeSheet-9\DonkeyFile.txt", "w")
fw.write(final)