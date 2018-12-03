import graphics as gr

window = gr.GraphWin("Sirius project", 600, 600)


def draw_circle(x, y, size, color, width=5):
    my_circle = gr.Circle(gr.Point(x, y), size)
    my_circle.setWidth(width)
    my_circle.setOutline(color)
    my_circle.draw(window)


def draw_rectangle(x1, y1, x2, y2, color):
    my_rectangle = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    my_rectangle.setFill(color)
    my_rectangle.draw(window)


draw_circle(200, 200, 50, "blue")
draw_circle(310, 200, 50, "black")
draw_circle(420, 200, 50, "red")
draw_circle(255, 260, 50, "orange")
draw_circle(365, 260, 50, "green")

draw_rectangle(1, 1, 160, 40, "white")
draw_rectangle(1, 40, 160, 80, "blue")
draw_rectangle(1, 80, 160, 120, "red")



window.getMouse()

window.close()