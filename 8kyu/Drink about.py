"""
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
"""


def people_with_age_drink(age):
    drinks = ["drink toddy", "drink coke", "drink beer", "drink whisky"]
    if age < 14:
        return drinks[0]
    elif 14 <= age < 18:
        return drinks[1]
    elif 18 <= age < 21:
        return drinks[2]
    else:
        return drinks[3]
