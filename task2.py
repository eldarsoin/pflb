
import math 

def checkCollision(a, b, c, x, y, radius): 
	
	# Finding the distance of line 
	# from center. 
	dist = ((abs(a * x + b * y + c)) /
			math.sqrt(a * a + b * b)) 

	# Checking if the distance is less 
	# than, greater than or equal to radius. 
	if (radius == dist): 
		print("Touch") 
	elif (radius > dist): 
		print("Intersect") 
	else: 
		print("Коллизий не найдено")

# Driven Program 
radius = 10.67
x = 0
y = 0
a = 1
b = 0.5
c = 15
checkCollision(a, b, c, x, y, radius) 



#find the intercepts
c1.find_intercept(c2)

#test results by reversing the operation
c2.find_intercept(c1)