with open("PythonPracticeSheet-9\\renamed_by_python.txt", "r") as f:
    if "twinkle" in f.read().lower():
        print("Yes, the word 'twinkle' is present")
    else:
        print("No, the word 'twinkle' is not present")