import turtle
import random
from pico2d import*



def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())




def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)

    for i in range (0,100,2):
        t = i/100
        x = (2*t**2-3*t+1)*p1[0] + (-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1] + (-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))

    draw_point(p3)
    pass


def draw_curve_10_points(p1, p2, p3, p4,p5,p6,p7,p8,p9,p10):
    global x,y,frame,Char_Shape


    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]

        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p1[0] < p2[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p2[0] < p3[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p3[0] < p4[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p4-p5
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p4[0] < p5[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p5-p6
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p5[0] < p6[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p6-p7
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p6[0] < p7[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()
    # draw p7-p8
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p7[0] < p8[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()

    # draw p8-p9
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p8[0] < p9[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()
    # draw p9-p10
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p9[0] < p10[0]:
            Char_Shape = 100
        else:
            Char_Shape = 0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()



    # draw p10-p1
    for i in range(50, 100, 2):
        t = i/100
        x = (2 * t ** 2 - 3 * t + 1) * p9[0] + (-4 * t ** 2 + 4 * t) * p10[0] + (2 * t ** 2 - t) * p1[0]
        y = (2 * t ** 2 - 3 * t + 1) * p9[1] + (-4 * t ** 2 + 4 * t) * p10[1] + (2 * t ** 2 - t) * p1[1]
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        frame = (frame + 1) % 8
        if p10[0] < p1[0]:
            Char_Shape = 100
        else:
            Char_Shape =0
        Charcter.clip_draw(frame * 100, Char_Shape, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        get_events()


KPU_WIDTH = 1280
KPU_HEIGHT = 1024

pico2d.open_canvas()

Map = load_image('KPU_GROUND.png')
Charcter = load_image('animation_sheet.png')

x, y = 400,400
Char_Shape =0
frame = 0
size =10
points = [(random.randint(0,800),random.randint(0,600))for i in range(size)]
while True:
    draw_curve_10_points(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9])





