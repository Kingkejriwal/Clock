
import time
import turtle

# set background

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock")
wn.tracer(0)

# create drawing pen

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def clock_draw(h, m, se, pen):

	# Draw clock face

	pen.up()
	pen.goto(0,210)
	pen.setheading(180)
	pen.color("blue")
	pen.pendown()
	pen.circle(210)

	# Draw lines for hours

	pen.penup()
	pen.goto(0,0)
	pen.setheading(90)

	for _ in range(12):
		pen.fd(190)
		pen.pendown()
		pen.fd(20)
		pen.penup()
		pen.goto(0,0)
		pen.rt(30)

	# Draw hour hand
	pen.penup()
	pen.goto(0,0)
	pen.color("White")
	pen.setheading(90)
	angle = (h / 12) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(125)

	# Draw minute hand
	pen.penup()
	pen.goto(0,0)
	pen.color("green")
	pen.setheading(90)
	angle = (m / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(180)

	# Draw hour hand
	pen.penup()
	pen.goto(0,0)
	pen.color("gold")
	pen.setheading(90)
	angle = (se / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(75)

while True:
	h = int(time.strftime("%I"))
	m = int(time.strftime("%M"))
	se = int(time.strftime("%S"))

	clock_draw(h, m, se, pen)
	wn.update()

	time.sleep(1)

	pen.clear()

wn.mainloop()