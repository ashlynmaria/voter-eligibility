age = int(input("🗳️  How old are you? "))
# If the user's age s greater than or equal to 18, they can vote
if age >= 18: 
    print("🎉 Congratulations! You are eligible to vote. Go make a difference!")
else:
    waiting_years = 18 - age
    print(f"🥺 Oops! You're not eligible yet. But hey, only {waiting_years} more years to go!")
