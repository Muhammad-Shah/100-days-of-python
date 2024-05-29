import math
# Can required calculation Function Definition
def paint_calc(height, width, cover):
    number_of_cons = (height*width)/cover
    print(f"You will need {round(number_of_cons)} cans of paint")
    # math.ceil() function round it
    # print(f"You will need {math.ceil(number_of_cons)} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# //////////////////////////////////////////////////////
# round() function input for given input
# Height of wall: 7
# Width of wall: 13
# You will need 18 cans of paint


# # math.ceil() function for given input
# Height of wall: 7
# Width of wall: 13
# You will need 19 cans of paint