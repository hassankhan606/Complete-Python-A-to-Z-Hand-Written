import random

#* 🎮 Function to Play the Game and Track High Score
def game():
    print("🎯 You are playing a game...")

    #* 🎲 Generate a random score between 0 and 100
    score = random.randint(0, 100)

    try:
        with open("hiScore.txt", "r") as f:
            hiScore = f.read()
            hiScore = int(hiScore) if hiScore.strip() else 0
    except FileNotFoundError:
        hiScore = 0  #* File doesn't exist yet, assume 0

    print(f"📊 Your Score: {score}")
    print(f"🏆 High Score: {hiScore}")

    #* 🆕 Update High Score if new score is higher
    if score > hiScore:
        with open("hiScore.txt", "w") as f:
            f.write(str(score))  #* Save new high score
        print("🎉 New High Score Achieved!")

    return score

#* ▶️ Run the Game
game()
