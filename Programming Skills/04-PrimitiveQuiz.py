#Exercise 4-Primitive Quiz

Quiz_Questions = {
    "France": "Paris",
    "Belgium": "Brussels",
    "England": "London",
    "Finland": "Helsinki",
    "Germany": "Berlin",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

for Country, Capital in Quiz_Questions.items():
   
    Answer = input(f"What is the capital of {Country}? ").strip()

    if Answer.lower() == Capital.lower():
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {Capital}.")
