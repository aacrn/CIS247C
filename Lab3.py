#Aaron Truong
# Lab 3 CIS 247 C

"""
Args
    angle_1 = input float
    angle_2 = input float
    angle_3 = input float

returns
    check if valid triangle
    check for acute, right, obtuse
"""

def get_angle_input(answer): #check if numeric value input
    while True:
        try:
            angle = float(input(answer))
            return angle
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def is_valid_triangle():
    angle_1 = get_angle_input("First Angle:")
    angle_2 = get_angle_input("Second Angle:")
    angle_3 = get_angle_input("Third Angle:")

#check for valid triangle
    if (angle_1 + angle_2 + angle_3) != 180:
        print("Not a valid triangle, angles do not add to 180")
        return False
    elif (angle_1 or angle_2 or angle_3 < 0):
        print("Not a valid triangle, angles must be positive")
        return False
    elif (angle_1 or angle_2 or angle_3 >= 180):
        print("Not a valid triangle, angle must be less than 180")
        return False
    else: 
        get_triangle_type(angle_1, angle_2, angle_3)
        return True

def get_triangle_type(angle_1, angle_2, angle_3):
#determine what type of triangle
    if (angle_1 and angle_2 and angle_3 < 90):
        print("This is an Acute Triange")
    elif (angle_1 or angle_2 or angle_3 == 90):
        print("This is a Right Triangle")
    else:
        print("This is an Obtuse Triangle")

is_valid_triangle()