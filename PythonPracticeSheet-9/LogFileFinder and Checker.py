import os

file_list = os.listdir("PythonPracticeSheet-9\LogFile")
log_files = []

for item in file_list:
    if item.endswith('.log'):
        log_files.append(item)

for file in log_files:
    with open(f"PythonPracticeSheet-9\LogFile\{file}", "r") as f:
        content = f.read()
        if "python" in content.lower():
            print(f"Python is found in {file}")
