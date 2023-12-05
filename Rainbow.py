import turtle
import colorsys


def rainbow_color(step):
    r, g, b = colorsys.hsv_to_rgb(step, 1.0, 1.0)
    return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))


def draw_spiral(size, step):
    turtle.color(rainbow_color(step))
    turtle.forward(size)
    turtle.right(45)
    draw_spiral(size + 5, step + 0.02)


turtle.speed(2)
turtle.width(2)
turtle.hideturtle()

draw_spiral(5, 0)

turtle.done()
