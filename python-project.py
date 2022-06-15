from work import Circle

circle1 = Circle(1,10,"Blue", True)
circle2 = Circle(2,8,"Red", True)
circle3 = Circle(3,17,"Yellow", False)

print(" Circle 1 circumfrancre is : " + str(int(circle1.circumfrance())))
print(" Circle 2 circumfrancre is : " + str(circle2.circumfrance()))
print(" Circle 3 circumfrancre is : " + str(circle3.circumfrance()))