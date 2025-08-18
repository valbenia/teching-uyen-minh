import turtle
import math

def draw_detailed_vietnam_flag():
    """
    Draw the Vietnam national flag with official colors and proportions.
    The flag consists of a red background with a yellow five-pointed star in the center.
    """
    
    # Setup screen
    screen = turtle.Screen()
    screen.title("Vietnam National Flag - Official Version")
    screen.bgcolor("white")
    screen.setup(900, 700)
    
    # Create turtle
    flag_turtle = turtle.Turtle()
    flag_turtle.speed(3)
    
    # Official flag proportions (2:3 ratio)
    flag_width = 360
    flag_height = 240
    
    # Calculate positions
    start_x = -flag_width // 2
    start_y = flag_height // 2
    
    # Draw red background with official red color
    flag_turtle.goto(start_x, start_y)
    flag_turtle.color("#DA020E")  # Official Vietnam red
    flag_turtle.begin_fill()
    flag_turtle.pendown()
    
    # Draw flag rectangle
    for _ in range(2):
        flag_turtle.forward(flag_width)
        flag_turtle.right(90)
        flag_turtle.forward(flag_height)
        flag_turtle.right(90)
    
    flag_turtle.end_fill()
    flag_turtle.penup()
    
    # Draw the star with proper proportions
    # The star's diameter should be 3/5 of the flag's height
    star_radius = (flag_height * 3/5) // 2
    print('start radius: ', star_radius)
    draw_precise_star(flag_turtle, 0, 0, star_radius, "#FFFF00")  # Official yellow
    
    # Add flag information
    flag_turtle.goto(0, -flag_height//2 - 60)
    flag_turtle.color("black")
    flag_turtle.write("Cờ đỏ sao vàng - Vietnam National Flag", align="center", font=("Arial", 14, "bold"))
    
    flag_turtle.goto(0, -flag_height//2 - 85)
    flag_turtle.write("Red flag with yellow star", align="center", font=("Arial", 12, "normal"))
    
    # Hide turtle
    flag_turtle.hideturtle()
    
    # Keep window open
    screen.exitonclick()

def draw_precise_star(turtle_obj, x, y, radius, color):
    """
    Draw a geometrically precise five-pointed star with correct orientation.
    The star will have one point facing upward.
    
    Args:
        turtle_obj: The turtle object
        x, y: Center coordinates
        radius: Radius of the circumscribed circle
        color: Fill color
    """
    
    # Calculate the points of the star
    points = []
    for i in range(10):  # 5 outer points + 5 inner points
        # Start from top (90 degrees), going clockwise
        angle = math.radians(90 - i * 36)  # Start from top, 36 degrees between points
        if i % 2 == 0:  # Outer points
            point_x = x + radius * math.cos(angle)
            point_y = y + radius * math.sin(angle)
        else:  # Inner points
            inner_radius = radius * 0.38  # Ratio for inner points to create proper star shape
            point_x = x + inner_radius * math.cos(angle)
            point_y = y + inner_radius * math.sin(angle)
        points.append((point_x, point_y))
    
    # Move to first point (top point of star)
    turtle_obj.penup()
    turtle_obj.goto(points[0][0], points[0][1])
    turtle_obj.pendown()
    
    # Set color and start filling
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    
    # Draw the star by connecting all points
    for point in points[1:]:
        turtle_obj.goto(point[0], point[1])
    
    # Close the shape by returning to first point
    turtle_obj.goto(points[0][0], points[0][1])
    turtle_obj.end_fill()
    turtle_obj.penup()

if __name__ == "__main__":
    # Run the detailed Vietnam flag version
    draw_detailed_vietnam_flag()