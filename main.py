import turtle

SCREEN_DISTANCE = 240


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.image = turtle.Turtle()
        self.image.penup()
        self.image.speed("fastest")
        self.image.hideturtle()

    def update(self, camera, screen_distance):
        x_app = camera.x - self.x
        y_app = camera.y - self.y
        z_app = camera.z - self.z
        
        if z_app > 0:
            y_displayed = screen_distance * (y_app / z_app)
            x_displayed = screen_distance * (x_app / z_app)
            self.image.goto(x_displayed, y_displayed)
        else:
            self.image.hideturtle()


class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move_forward(self):
        self.z -= 10

    def move_backward(self):
        self.z += 10

    def move_right(self):
        self.x -= 10

    def move_left(self):
        self.x += 10

    def move_up(self):
        self.y -= 10
        
    def move_down(self):
        self.y += 10


class Cube:
    def __init__(self, side_length, x, y, z):
        foo = side_length/2
        self.p1 = Point(x + foo, y + foo, z + foo)
        self.p2 = Point(x + foo, y + foo, z - foo)
        self.p3 = Point(x + foo, y - foo, z + foo)
        self.p4 = Point(x + foo, y - foo, z - foo)
        self.p5 = Point(x - foo, y + foo, z + foo)
        self.p6 = Point(x - foo, y - foo, z + foo)
        self.p7 = Point(x - foo, y + foo, z - foo)
        self.p8 = Point(x - foo, y - foo, z - foo)
        self.renderer = turtle.Turtle()
        self.renderer.hideturtle()
        self.renderer.speed("fastest")
        self.renderer.penup()

    def update(self, camera, screen_distance):
        self.p1.update(camera, screen_distance)
        self.p2.update(camera, screen_distance)
        self.p3.update(camera, screen_distance)
        self.p4.update(camera, screen_distance)
        self.p5.update(camera, screen_distance)
        self.p6.update(camera, screen_distance)
        self.p7.update(camera, screen_distance)
        self.p8.update(camera, screen_distance)
        self.renderer.penup()
        self.renderer.goto(self.p1.image.pos())
        self.renderer.pendown()
        self.renderer.goto(self.p2.image.pos())
        self.renderer.goto(self.p4.image.pos())
        self.renderer.goto(self.p3.image.pos())
        self.renderer.goto(self.p6.image.pos())
        self.renderer.goto(self.p8.image.pos())
        self.renderer.goto(self.p7.image.pos())
        self.renderer.goto(self.p5.image.pos())
        self.renderer.goto(self.p1.image.pos())
        self.renderer.penup()
        self.renderer.goto(self.p7.image.pos())
        self.renderer.pendown()
        self.renderer.goto(self.p2.image.pos())
        self.renderer.penup()
        self.renderer.goto(self.p5.image.pos())
        self.renderer.pendown()
        self.renderer.goto(self.p6.image.pos())
        self.renderer.penup()
        self.renderer.goto(self.p3.image.pos())
        self.renderer.pendown()
        self.renderer.goto(self.p1.image.pos())
        self.renderer.penup()
        self.renderer.goto(self.p4.image.pos())
        self.renderer.pendown()
        self.renderer.goto(self.p8.image.pos())
    
    def clear(self):
        self.renderer.clear()


screen = turtle.Screen()
cube1 = Cube(100, 0, 0, 0)
cube2 = Cube(100, 100, 0, 0)
cube3 = Cube(100, 100, 100, 0)
cube4 = Cube(100, 100, 100, 100)
camera = Camera(0, 0, 0)

screen.tracer(0, 0)
    
screen.onkey(camera.move_forward, "Up")
screen.onkey(camera.move_backward, "Down")
screen.onkey(camera.move_right, "Right")
screen.onkey(camera.move_left, "Left")
screen.onkey(camera.move_up, "w")
screen.onkey(camera.move_down, "s")
screen.listen()

while True:
    cube1.update(camera, SCREEN_DISTANCE)
    cube2.update(camera, SCREEN_DISTANCE)
    cube3.update(camera, SCREEN_DISTANCE)
    cube4.update(camera, SCREEN_DISTANCE)
    screen.update()
    cube1.clear()
    cube2.clear()
    cube3.clear()
    cube4.clear()

