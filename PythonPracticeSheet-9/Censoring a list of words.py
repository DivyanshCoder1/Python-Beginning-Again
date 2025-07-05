#Content Censoring Program
fr = open("PythonPracticeSheet-9\ToBeCensored.txt", "r", encoding='utf-8')
content = fr.read()
print("Previous: ", content)

old = ["fucking", "bullshit", "porn", "fuck", "sex", "ass", "hell", "shit"]
new = ["f***ing", "b******t", "p***", "f***", "s**", "a**", "h***", "sh*t"]

for item in old:
    if item in content:
        content = content.replace(item, new[old.index(item)])

fw = open("PythonPracticeSheet-9\ToBeCensored.txt", "w")
fw.write(content)
print("Final: ", content)