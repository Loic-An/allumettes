import turtle
couleurs=[[0,(203,79,15),(5,5,5),(255,191,179)],[0,(221,31,38),(130,66,32),(239,189,139),(0,0,0),(77,89,167),(253,232,33)],[0,(232,53,43),(135,4,4),(236,243,163),(5,155,9),(255,255,255),(255,192,0),(67,64,75),(177,119,40)],[0,(254,224,196),(225,84,13),(4,3,8)],[0,(255,255,255),(5,5,5),(255,191,179)],[0,(31,35,36),(255,255,255),(189,190,222),(214,217,243)]]
personnages = [[[0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
                [0,0,0,1,2,2,1,1,1,1,1,1,2,2,1,0,0,0],
                [0,0,1,1,1,3,2,1,1,1,1,2,3,1,1,1,0,0],
                [0,0,1,1,1,3,2,2,2,2,2,2,3,1,1,1,0,0],
                [0,1,1,1,1,3,2,3,1,1,3,2,3,1,1,1,1,0],
                [0,1,1,1,1,3,3,3,1,1,3,3,3,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,3,3,3,3,3,3,1,1,1,1,0,0],
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],
                [0,0,0,0,2,2,3,3,3,3,3,3,2,2,0,0,0,0],
                [0,0,0,0,2,2,2,3,3,3,3,2,2,2,0,0,0,0],
                [0,0,0,0,0,2,2,2,0,0,2,2,2,0,0,0,0,0]],
               [[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                [0,0,0,0,0,2,2,2,3,3,4,3,0,0,0,0,0,0],
                [0,0,0,0,2,3,2,3,3,3,4,3,3,3,0,0,0,0],
                [0,0,0,0,2,3,2,2,3,3,3,4,3,3,3,0,0,0],
                [0,0,0,0,2,2,3,3,3,3,4,4,4,4,0,0,0,0],
                [0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0],
                [0,0,0,0,0,1,1,5,1,1,1,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,5,1,1,5,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,5,5,5,5,1,1,1,1,0,0,0],
                [0,0,0,3,3,1,5,6,5,5,6,5,1,3,3,0,0,0],
                [0,0,0,3,3,3,5,5,5,5,5,5,3,3,3,0,0,0],
                [0,0,0,3,3,5,5,5,5,5,5,5,5,3,3,0,0,0],
                [0,0,0,0,0,5,5,5,0,0,5,5,5,0,0,0,0,0],
                [0,0,0,0,2,2,2,0,0,0,0,2,2,2,0,0,0,0],
                [0,0,0,2,2,2,2,0,0,0,0,2,2,2,2,0,0,0],],
               [[0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,2,2,1,2,1,1,0,0,0,0],
                [0,0,0,0,0,3,0,0,1,3,2,1,2,1,0,0,0,0],
                [0,0,0,0,0,3,3,4,1,3,1,1,4,4,1,0,0,0],
                [0,0,0,0,0,1,1,4,4,3,3,1,1,1,4,0,0,0],
                [0,0,0,3,4,4,5,5,4,4,4,4,5,2,1,3,3,0],
                [0,0,0,3,3,5,6,7,4,3,3,4,4,4,3,3,7,3],
                [0,0,0,1,7,6,6,7,4,3,1,3,3,3,3,3,3,3],
                [0,0,0,6,7,7,6,7,7,3,3,1,5,1,5,1,5,0],
                [0,0,7,6,6,7,7,8,7,7,3,3,3,3,3,3,0,0],
                [0,6,7,7,6,6,8,8,8,7,7,7,7,7,7,6,7,0],
                [0,6,6,7,7,8,8,6,3,3,3,3,3,3,6,7,7,0],
                [0,5,6,6,6,5,6,6,3,3,3,3,3,3,7,7,6,6],
                [6,0,5,6,5,8,8,8,6,6,6,6,6,6,8,6,6,5],
                [6,6,6,8,8,6,6,6,8,3,3,3,3,3,8,6,5,0],
                [0,6,6,8,6,6,6,6,8,6,6,6,6,8,6,6,0,0],
                [0,0,6,8,6,6,6,6,8,8,3,3,8,3,3,3,0,0],
                [0,0,0,0,6,5,6,5,6,0,0,0,6,6,6,5,6,5]],
               [[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],
                [0,0,0,2,2,2,2,2,3,2,2,2,2,2,3,0,0,0],
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0],
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],
                [0,0,0,2,2,3,2,2,2,2,2,3,2,2,2,0,0,0],
                [0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,2,0,0,2,2,0,0,0,0,0,0],
                [0,0,0,0,0,2,1,1,2,2,1,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,1,1,1,1,1,2,0,0,0,0,0],
                [0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0],
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],
                [0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0,0],
                [0,0,0,0,2,2,3,3,3,3,3,3,2,2,0,0,0,0],
                [0,0,0,0,2,2,2,3,3,3,3,2,2,2,0,0,0,0],
                [0,0,0,0,0,2,2,2,0,0,2,2,2,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,4,4,1,0,0,0,0],
                [1,2,2,2,2,2,2,2,2,2,2,2,2,4,1,0,0,0],
                [1,2,2,2,2,2,2,2,2,2,4,2,2,2,4,1,0,0],
                [1,2,3,4,4,4,4,4,4,4,4,4,2,2,2,4,1,0],
                [1,2,3,4,4,4,4,4,4,4,4,4,4,2,2,2,4,1],
                [1,2,3,4,4,4,4,4,4,4,4,4,2,2,2,4,1,0],
                [1,2,2,2,2,2,2,2,2,2,4,2,2,2,4,1,0,0],
                [1,2,2,2,2,2,2,2,2,2,2,2,2,4,1,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,4,4,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0]]]
def print_personnage(s:int,personnage:int,t=turtle):
    global personnages, couleurs
    t.width(0)
    for ligne in personnages[personnage]:
        for couleur in ligne:
            if couleur!=0:
                t.down()
                t.color(couleurs[personnage][couleur])
                t.fillcolor(couleurs[personnage][couleur])
                t.begin_fill()
                for i in range(4):
                    t.forward(s)
                    t.right(90)
                t.end_fill()
            t.up()
            t.forward(s+1)
        t.backward((s+1)*18)
        t.right(90)
        t.forward(s+1)
        t.left(90)

if __name__ == '__main__':
    turtle.tracer(0)
    turtle.colormode(255)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(-200,200)
    turtle.down()
    for i in range(len(personnages)):
        print_personnage(8,i)
    turtle.exitonclick()
