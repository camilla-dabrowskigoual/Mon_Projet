x = "-"
y = "|"

def draw_rectangle(width, height):
    print(y + width*x +y)
    for i in range(0, (height-2)):
        print(y + width*" "+y)
    print(y + width*x +y)
draw_rectangle(10,3)
draw_rectangle(8,6)