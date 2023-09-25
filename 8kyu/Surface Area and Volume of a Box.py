"""
Write a function that returns the total surface area and volume of a box as an array: [area, volume]
"""

def get_size(w,h,d):
    total = []
    total.append(2 * w * h + 2 * w * d + 2 * h * d)
    total.append(w * h * d)
    return total