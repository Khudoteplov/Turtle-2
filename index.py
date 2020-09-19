import turtle

a=[ (0, 1, 3, 5, 7, 8), (2, 3, 7), (0, 3, 6, 8), (0, 2, 4, 6), (1, 3, 4, 7), (0, 1, 4, 7, 8), (2, 4, 5, 7, 8), (0, 2, 5), (0, 1, 3, 4, 5, 7, 8), (0, 1, 3, 4, 6) ]

fnt = open('font.txt', 'w')

for i in a:
	print(i, file=fnt)



fnt.close()
def q(x, y, s): 
	turtle.penup()
	turtle.goto(x, y)
	if 0 in s:
	    turtle.pendown()
	turtle.goto(x-10, y)
	turtle.penup()
	if 1 in s:
	    turtle.pendown()
	turtle.goto(x-10, y-10)
	turtle.pendown()
	turtle.penup()
	if 2 in s:
	    turtle.pendown()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.penup()
	if 3 in s:
	    turtle.pendown()
	turtle.goto(x, y-10)
	turtle.pendown()
	turtle.penup()
	if 4 in s:
	    turtle.pendown()
	turtle.goto(x-10, y-10)
	turtle.pendown()
	turtle.penup()
	if 5 in s:
	    turtle.pendown()
	turtle.goto(x-10, y-20)
	turtle.pendown()
	turtle.penup()
	if 6 in s:
	    turtle.pendown()
	turtle.goto(x, y-10)
	turtle.pendown()
	turtle.penup()
	if 7 in s:
	    turtle.pendown()
	turtle.goto(x, y-20)
	turtle.pendown()
	turtle.penup()
	if 8 in s:
	    turtle.pendown()
	turtle.goto(x-10, y-20)
	turtle.pendown()
	turtle.penup()


w=[1,4,1,7,0,0]
x, y = 0, 0
for i in w:
    q(x, y, a[i])
    x += 20


	

