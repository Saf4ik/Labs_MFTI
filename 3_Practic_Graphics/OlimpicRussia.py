import graphics as gr

window = gr.GraphWin("Sirius project", 600, 600)

my_circle1 = gr.Circle(gr.Point(200, 200), 50)
my_circle2 = gr.Circle(gr.Point(310, 200), 50)
my_circle3 = gr.Circle(gr.Point(420, 200), 50)
my_circle4 = gr.Circle(gr.Point(255, 260), 50)
my_circle5 = gr.Circle(gr.Point(365, 260), 50)

my_circle1.setWidth(5)
my_circle2.setWidth(5)
my_circle3.setWidth(5)
my_circle4.setWidth(5)
my_circle5.setWidth(5)

my_circle1.setOutline("blue")
my_circle2.setOutline("black")
my_circle3.setOutline("red")
my_circle4.setOutline("orange")
my_circle5.setOutline("green")

my_rectangle1 = gr.Rectangle(gr.Point(1,1), gr.Point(160,40))
my_rectangle2 = gr.Rectangle(gr.Point(1,40),gr.Point(160,80))
my_rectangle3 = gr.Rectangle(gr.Point(1,80),gr.Point(160,120))

my_rectangle2.setFill("blue")
my_rectangle3.setFill("red")


my_rectangle1.draw(window)
my_rectangle2.draw(window)
my_rectangle3.draw(window)
my_circle1.draw(window)
my_circle2.draw(window)
my_circle3.draw(window)
my_circle4.draw(window)
my_circle5.draw(window)

window.getMouse()

window.close()