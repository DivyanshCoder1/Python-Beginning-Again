for i in range(2,21):
    with open(f"PythonPracticeSheet-9\MultiplicationTable\{i}.txt", "a") as f:
        for j in range(10):
            f.write(str(f"{i} x {j+1} = {i*(j+1)}\n"))
