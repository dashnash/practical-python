# bounce.py
#
# Exercise 1.5

bounce_height = 100 # meters
bounce_count = 10

while bounce_count > 0:
    bounce_height *= 3/5
    bounce_count -= 1
    print(round(bounce_height, 4))
    
