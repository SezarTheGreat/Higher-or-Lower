import art
import game_data
import random


def format_data(account):
    """Takes the account format a makes it in readable format!"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def compare(user_guess,a_follower,b_follower):
    """Take the user guess and follower count of a and b and returns if it got it right."""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(art.logo)
score = 0
game_continue = True
account_b = random.choice(game_data.data)

while game_continue:
    account_a = account_b
    account_b = random.choice(game_data.data)
    if account_a == account_b:
        account_a = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)
    print(art.logo)

    a_followerCount = account_a["follower_count"]
    b_followerCount = account_b["follower_count"]

    is_correct = compare(guess,a_followerCount,b_followerCount)

    if is_correct:
        score += 1
        print(f"You're Right! Current score {score}")
    else:
        print(f"Sorry, that's Wrong. Final Score: {score}")
        game_continue = False