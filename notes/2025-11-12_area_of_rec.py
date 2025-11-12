'''
1. 
function definition >>> def cal_area_of_rec(width, height)

function call >>> cal_area_of_rec(4, 5)


2.
We can use differently values by calling the functions anytime we want.

3.
If there is on return statement, it will not give the function's output.
But what if we use "print" statement inside the sub-function.


'''


def cal_area_of_rec(width, height):
    area = width * height
    return area

print(f"The area of rectangle is: {cal_area_of_rec(4,5)} square meter.")

