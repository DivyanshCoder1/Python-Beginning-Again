import random
f = open("PythonPracticeSheet-9\HiScore.txt", "r")
score_high = int(f.read())
f.close()

def game():
    #Just returning random number for now as user score!!
    return random.randint(1,100)
def game_score_updator(score_now, score_high):
    if score_now > score_high:
        w = open("PythonPracticeSheet-9\HiScore.txt", "w")
        w.write(str(score_now))
        print(f"The new high score is: {score_now}")
    else:
        print(f"Current Score is: {score_now}")
        print(f"Highest Score is: {score_high}")


game_score_updator(game(), score_high)
