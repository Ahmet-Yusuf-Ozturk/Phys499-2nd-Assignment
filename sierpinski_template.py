import math
from turtle import Turtle, Screen
import drawpolygon

#
# Draws one triangle with bottom vertex at coordinate (x, y) and side length of s.
#
# Then, recursively calls itself three times to generate the next set of Sierpinski
# triangles to the left, to the right, and above the current triangle you just drew.
# Here the parameters are:
# t: Turtle Graphics object for drawing
# n: the number of recursive iterations
# x, y: the coordinates of the vertex of the equilateral filled triangle with side
#       length of s to be drawn pointing down.
# s: The side length of the equilateral filled triangle to draw
def sierpinski(t, n, x, y, s):
    # Draw one triangle, bottom vertex at (x, y), side length s.
    # Then, recursively call itself three times to generate the
    # next order Sierpinski triangles above, left and right of current triangle
    # TODO Your code below here:
    coordinates = [(x-s/2,y+math.sqrt(3)/2*s),(x,y),(x+s/2,y+math.sqrt(3)/2*s)]
    if n == 0:
        return
    else:
        drawpolygon.drawfilledtriangle(t= t, points= coordinates)
        sierpinski(t,n-1,x+s/2,y,s/2)
        sierpinski(t,n-1,x-s/2,y,s/2)
        sierpinski(t,n-1,x,y+math.sqrt(3)/2*s,s/2)
        """
        How to update parameters t, n, and s is obvious.
        We only need to decide how to update parameters x and y.
        I find the suitable candidates with drawing on the paper
        and playing with them. Since the triangles we are drawing is equilateral
        triangles and s becomes s/2 in the next iteration/recursive call, 
        the triangle on the right and left's y coordinates won't change and
        x coordinate will differ by s/2. And the upper traingle will have it's
        bottom vertex in the current triangles upper edge, it's y value will be
        s*sqrt(3)/2+y and x coordinate won't change.
        """



def main():
    n = int(input("Number of iterations: "))

    t = Turtle('turtle')
    screen = t.getscreen()
    screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
    t.hideturtle()

    # Draw the main unfilled equilateral triangle.
    # Each side of this triangle will be equal to 1 (normalized depending on your screen resolution).
    # See the first figure in the assignment sheet.
    xCoors = [0, 1.0, 0.5]
    yCoors = [0, 0, math.sqrt(3) / 2]
    drawpolygon.draw_triangle(t, xCoors, yCoors)

    # The x and y coordinates of the vertex of the triangle that will point
    # downwards.  See the filled triangle in the first figure in the assignment
    # sheet.
    xi = 0.5
    yi= 0
    side_length = 1.0
    sierpinski(t, n, xi, yi, side_length/2)

    # This will make sure your graph will be up until you close it.
    Screen().exitonclick()

main()