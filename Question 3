import turtle
import math

def draw_edge(length, depth):
    """Recursive function to draw one edge with indentation pattern."""
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.left(60)    # turn to form the triangle indentation
        draw_edge(length, depth - 1)
        turtle.right(120)  # turn inward
        draw_edge(length, depth - 1)
        turtle.left(60)    # reset orientation
        draw_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    """Draw the fractal polygon with recursive edges."""
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

def main():
    # Get user inputs
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Setup turtle
    turtle.speed(0)  # fastest drawing
    turtle.penup()
    turtle.goto(-length, length/2)  # reposition for better view
    turtle.pendown()

    # Draw fractal polygon
    draw_polygon(sides, length, depth)

    # Finish
    turtle.done()

if __name__ == "__main__":
    main()
