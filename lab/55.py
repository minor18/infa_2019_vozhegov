from graph import *

# (230,230,230) - grey color
# (0,255,255) - sky color
# (170,255,255) - sun color
# (230,230,230) - bear color


def elipsfill(x,y, x0, y0, a, b)  :
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1):
        return True
    else :
        return False
    
def elipsboard (x,y, x0, y0, a, b):
    e = 0.032
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1+e
         and
         (x-x0)**2/(a**2) + (y-y0)**2/(b**2) >= 1-e) :
        return True
    else :
        return False
    
def contur_elips(x0,y0, a, b):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsboard (x,y, x0, y0, a, b):
                 point (x,y,"black")           
def elips(x0, y0, a, b, color):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsfill(x,y, x0, y0, a, b):
                point(x,y,color)
    contur_elips(x0,y0, a, b)



windowSize(500,600)

brushColor(0,255,255)
rectangle(0, 0, 500, 350 )

brushColor(230,230,230)
rectangle(0, 350, 500, 800 )



penColor(170,255,255) #outside circle
brushColor(170,255,255)
circle(310,110,110)

penColor(0,255,255) #inside circle
brushColor(0,255,255)
circle(310,110,90)

penColor(170,255,255) #lights
brushColor(170,255,255)
rectangle(300,0,320,220)
rectangle(200,120,420,100)

penColor("white") #circles
brushColor("white")
circle(310,110,15)
circle(210,110,10)
circle(310, 10,10)
circle(410,110,10)
circle(310,210,10)



elips(130,245,50,30, (230,230,230)) #head
elips(100,410,75,150, (230,230,230)) #body
elips(175,525,60,40, (230,230,230)) #leg
elips(240,550,30,12, (230,230,230)) #foot

penColor("black") #nose
brushColor("black")
circle(180,240,4)

circle(125,237,4) #eye

line(135,255,178,255) #mouth

brushColor(230,230,230) #ear
circle(95,225,7)



elips(360,490,80,30, (100,100,100)) #loonka
elips(360,500,65,20, (40,100,90)) #water



penColor("black")
line(360,200,360,500)
penSize(3)
line(360,200,125,410)
penSize(1)
elips(175,360,40,15,  (230,230,230)) #arm



elips(380,565,40,15,(180,180,180)) #body

penColor(100,100,255) #eye
brushColor(100,100,255)
circle( 405, 560, 6)
penColor("black")
brushColor("black")
circle( 405, 560, 3)

penColor(255,100,100)
brushColor(255,200,200)
polygon([(340,565), (300,555), (295,580)]) #tail

polygon([(395, 550), (390, 535), (350,538), (375, 550)]) #fins
polygon([(375, 580), (375,590), (355,590), (365,580)])
polygon([(385,580), (395, 580), (415,590), (385,590), ]) 


run()
