"""
Create a combat function that takes the player's current health and the amount of damage recieved, 
and returns the player's new health. Health can't be less than 0.
"""


def combat(health, damage):
    result = health - damage
    return result if result >= 0 else 0
