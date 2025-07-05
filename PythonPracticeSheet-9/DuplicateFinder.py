f1 = open("PythonPracticeSheet-9\\this.txt", "r")
f1_content = f1.read()
f1.close()

f2 = open("PythonPracticeSheet-9\\this(copy).txt", "r")
f2_content = f2.read()
f2.close()

if f1_content == f2_content:
    print("Same content")
else:
    print("Different content")