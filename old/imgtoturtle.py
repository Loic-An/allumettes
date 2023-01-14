from PIL import Image
import turtle as t
# Set the image name and path
image_name = 'bgrd.gif'
precision = 1 # 1 = all pixels, 2 = every two pixel, 3 = every third pixel, etc.
assert precision > 0, 'precision must be > 0'
assert type(precision) == int, 'precision must be an integer'

# Open the image
im = Image.open(image_name)
print(f'importing {image_name} ({im.format} image) of size {im.size}')
im_lraw = list(im.getdata())
im_list = [im_lraw[i:i+im.size[0]:precision] for i in range(0,im.size[0]*im.size[1],im.size[0])][::precision]
print(f'imported {im.size[0]*im.size[1]//precision} pixels',f'over {im.size[0]*im.size[1]} pixels' if precision > 1 else '')
im_palette = im.getpalette()
im_colors = [tuple(im_palette[i:i+3]) for i in range(0,len(im_palette),3)]
print(f'found {len(im_colors)} colors in the image')
bgcolor = im_colors[0] # background color, first color in the list == most common color
print(f'background color is {bgcolor}')
#im = None # free memory (not really necessary)
print('generating turtle code (this may take a while)...')
im_list_text = 'bgrd_list=['+','.join(['['+','.join(map(str,im_list[i]))+']' for i in range(len(im_list))])+']'
im_colors_text = 'bgrd_colors=['+','.join(['('+','.join(map(str,im_colors[i]))+')' for i in range(len(im_colors))])+']'
im_text = im_list_text+'\n'+im_colors_text

bg = t.Turtle()
t.setup(im.size[0],im.size[1])
t.colormode(255)
t.tracer(0)
bg.hideturtle()
# Set the background color
bg.color(bgcolor)
bg.goto(-im.size[0]//2,-im.size[1]//2)
bg.down()
bg.begin_fill()
bg.forward(im.size[0])
bg.left(90)
bg.forward(im.size[1])
bg.left(90)
bg.forward(im.size[0])
bg.left(90)
bg.forward(im.size[1])
bg.left(90)
bg.end_fill()
bg.up()
# Draw the image
bt = t.Turtle()
bt.hideturtle()
bt.up()
bt.goto(-im.size[0]//2,im.size[1]//2)
t.update()
for i in range(len(im_list)):
    for j in range(len(im_list[i])):
        c = im_colors[im_list[i][j]]
        if c:
            bt.down()
            bt.color(c)
            bt.forward(1)
            bt.up()
        else:
            bt.goto(bt.xcor()+1,bt.ycor())
    bt.up()
    bt.goto(-im.size[0]//2,im.size[1]//2-i-1)
    t.update()
t.exitonclick()
