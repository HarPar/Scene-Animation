from tkinter import *
from random import *
from time import *
from math import *


#Setting up the screen
root = Tk()
screen = Canvas(root, width=800, height=800,background="sky blue")
screen.pack()

#Making the title
root.title("Chinese Temple")

#Defining drawing leaves on the sakura trees
def drawingtheleaves():
        #Deciding y1,x2 and y2 for the sakura leaves
        sakuray1 = randint(435,525)
        sakurax2 = newsakurax1 + 5
        sakuray2 = sakuray1 - 5

        #Drawing the leaf
        screen.create_oval(newsakurax1,sakuray1,sakurax2,sakuray2,fill="pink")



#Defining drawing sakura tree stump
def drawingsakuratree():
    #Determining the second x-coordinate relative to the first x-coordinate
    Tsakurax2 = Tsakurax1 + 25

    #Drawing the stump of the sakura tree
    screen.create_rectangle(Tsakurax1,500,Tsakurax2,600,fill="brown")
    movement = 0
    
    for sakuraleaf in range(1,150):
        global newsakurax1

        #If 5 is a factor of sakuraleaf then reassign movement by adding 0.29349343
        if sakuraleaf % 5 == 0:
            movement = movement + 0.29349343

        #Determining the first x-coordinate of sakure trees leaf    
        sakurax1 = randint(Tsakurax1-10,Tsakurax1+25)
        newsakurax1 = sakurax1 - movement

        #Drawing the leaf
        drawingtheleaves()

        #Reassigning the first x-coordinate of sakure trees leaf, i am doing this to have symmetry
        newsakurax1 = sakurax1 + 2*movement

        #Drawing the leaf
        drawingtheleaves()



global lanterncolour
lanterncolour = "orange"
def lanternsontemple():
        global lantern1
        global lantern2
        global lantern3
        global lantern4
        #Lanterns on the building
        lantern1 = screen.create_oval(218,315,232,335,fill=lanterncolour,outline=lanterncolour)
        lantern2 = screen.create_oval(568,315,582,335,fill=lanterncolour,outline=lanterncolour)
        lantern3 = screen.create_oval(160,400,180,425,fill=lanterncolour,outline=lanterncolour)
        lantern4 = screen.create_oval(640,400,620,425,fill=lanterncolour,outline=lanterncolour)

#Creating the grass
screen.create_rectangle(0,600, 800, 800, fill="#00ff00",outline="#00ff00")

#Drawing the Chinese Temple
screen.create_rectangle(250,475,550,575, fill="red",outline="red")
screen.create_rectangle(200,450,600,475, fill="red")
screen.create_polygon(250,450,200,430,175,400,225,425,250,425, fill="yellow",outline="yellow")
screen.create_polygon(550,450,600,430,625,400,575,425,550,425, fill="yellow",outline="yellow")
screen.create_rectangle(250,425,550,450,fill="yellow",outline="yellow")
screen.create_rectangle(150,575,650,600,fill="#c0c0c0",outline="#c0c0c0")
screen.create_rectangle(275,350,525,425,fill="red",outline="red")
screen.create_rectangle(275,325,525,350,fill="yellow",outline="yellow")
screen.create_polygon(275,350,240,330,225,315,260,325,275,325,fill="yellow",outline="yellow")
screen.create_polygon(525,350,560,330,575,315,540,325,525,325,fill="yellow",outline="yellow")
screen.create_rectangle(325,275,475,325,fill="red",outline="red")
screen.create_polygon(325,275,310,260,300,250,500,250,490,260,475,275,fill="yellow",outline="yellow")
screen.create_polygon(270,260,350,225,400,200,450,225,530,260,fill="yellow",smooth="true",outline="yellow")

#Creating the door
screen.create_rectangle(375,500,425,575,fill="dark green",outline="dark green")

#3 Balls at the top of the building
screen.create_oval(380,175,420,210,fill="gold",outline="gold")
screen.create_oval(385,150,415,175,fill="gold",outline="gold")
screen.create_oval(390,130,410,150,fill="gold",outline="gold")

lanternsontemple()

#Creating the text ton the building: Translation: 你好 = ni hao = hi
screen.create_text(400,300,text="你好",font = " times 35 bold")

#Making the pillars for the building
#Setting starting positions
pillarx1 = 206
pillarx2 = 219
for pillars in range(1,7):
    #Drawing the pillars
    screen.create_rectangle(pillarx1,475,pillarx2,575,fill="orange")

    #Moving the pillars at a constant increment
    pillarx1 = pillarx1+75
    pillarx2 = pillarx2+75

#Details on the building:2 straight lines, jagged line design
#The 2 staright lines on the second floor
screen.create_line(275,362,525,362,width=2)
screen.create_line(275,412,525,412,width=2)

#The jagged line design at the very top of the temple
screen.create_line(400,500,400,575,width=2)
screen.create_line(300,250,350,237,width=2)
screen.create_line(350,237,400,262,width=2)
screen.create_line(400,262,450,237,width=2)
screen.create_line(500,250,450,237,width=2)


#Making windows on the building for the second floor
#Declaring starting positions of the windows
windowx1 = 305
windowx2 = 330
for windows in range(1,5):
    #Drawing the windows 
    screen.create_rectangle(windowx1,375,windowx2,400,fill="dark blue")

    #Moving the windows at a constant increment
    windowx1 = windowx1 + 55
    windowx2 = windowx2 + 55

#Creating clouds
screen.create_polygon(200,125,150,115,60,75,225,50,200,125,fill="dark grey",smooth="true")
screen.create_polygon(675,225,575,210,525,150,675,125,675,225,fill="dark grey", smooth="true")

#Creating the trees
global Tsakurax1
#Deciding the first x-coordinate of the sakura tree stump within range 25-60
Tsakurax1 = randint(25,60)
drawingsakuratree()

#Deciding the first x-coordinate of the sakura tree stump within range 675-710
Tsakurax1 = randint(675,710)
drawingsakuratree()

#Deciding the first x-coordinate of the sakura tree stump within range 90-125
Tsakurax1 = randint(90,125)
drawingsakuratree()

#Deciding the first x-coordinate of the sakura tree stump within range 740-775
Tsakurax1 = randint(740,775)
drawingsakuratree()


#Creating the sun
#Choosing how the sun would look like in terms of position of the first x-coordinate
sunx1 = randint(600,650)
#Drawing the sun
sun = screen.create_oval(sunx1,-125,1000,125,fill="yellow")

#Setting a variable for the image "water fountain test.gif"
waterfountain = PhotoImage(file = "water fountain test.gif")

#Making a label and setting the image as a water fountain
imagewf = Label(root,image = waterfountain, bg="#00ff00")

#Placing the label
imagewf.place(x=255,y=600)


#Declaring some variablea
increment = 0
meteorx1 = 0
bkcolour = 0
meteorFrameCount = 0

#Main for-loop
for frameCount in range(1,325):

        #Deciding if frameCount is in the range of drawing and deleting the sun and the moon, also whether the sky should change colour
        if frameCount < 156 and frameCount > 50:

                #Deciding to draw sun
                if frameCount > 50 and frameCount < 103:
                        screen.delete(sun)

                        #Move sun by 2
                        increment = increment + 2

                        #Draw the sun
                        sun = screen.create_oval(sunx1+increment,-125-increment,1000+increment,125-increment,fill="yellow")

                        #Reset incfrement if drawing the sun is done
                        if frameCount == 102:
                                increment = 0

                #Deciding to draw moon   
                else:
                        #Every frameCount which has a factor of 10 and is between 104 and 155, change the background sky colour
                        if frameCount % 10 == 0:
                                bkcolours = (["#559bf0","#4478f0","#127cf1","#0076ec","black"])
                                bkcolours = bkcolours[bkcolour]
                                bkcolour = bkcolour + 1
                                screen.configure(background=bkcolours)               

                        #Changing the increment at which the moon will be moving
                        increment = increment + 3.2

                        #Deciding to delete moon or not too
                        if frameCount != 103:
                                screen.delete(moon)

                        #Draw the moon
                        moon = screen.create_oval(0-(906-sunx1)+increment,-231+increment,0+increment,0+increment,fill="light grey")

                        #Redrawing the cloud so it looks like the moon is behind the cloud
                        if frameCount > 140:

                                #Deciding whether to delete the cliud or not
                                if frameCount != 141:
                                        screen.delete(cloud)

                                #Redrawing the cloud again
                                cloud = screen.create_polygon(200,125,150,115,60,75,225,50,200,125,fill="dark grey",smooth="true")


        #Deciding to draw meteor or not
        if frameCount > 180:

                #Make my own frameCount
                meteorFrameCount = meteorFrameCount + 1

                #Determining x1 and y1 of the meteor
                meteorx1 = 7*meteorFrameCount
                meteory1 = 100 * cos(.05*meteorFrameCount)+ 125

                #Deciding whether to delete the meteor or not too
                if frameCount != 181:
                        screen.delete(meteor)

                #Drawing the meteor
                meteor = screen.create_oval(meteorx1,meteory1,meteorx1+50,meteory1+50,fill="brown")

                #Determining whether to draw flame#1 or flame#2
                if frameCount % 2 ==0:
                        screen.delete(flame)

                        #Drawing flame #1
                        flame = screen.create_polygon(meteorx1+25,meteory1,meteorx1-35,meteory1+5,meteorx1-22,meteory1+10,meteorx1-55,meteory1+25,meteorx1-22,meteory1+40,meteorx1-35,meteory1+45,meteorx1+25,meteory1+50,fill="yellow")

                else:
                        #Deciding whether to delete flame or not as it is yet not defined
                        if frameCount != 181:
                                screen.delete(flame)

                        #Drawing flame#2
                        flame = screen.create_polygon(meteorx1+25,meteory1,meteorx1-45,meteory1+5,meteorx1-32,meteory1+10,meteorx1-65,meteory1+25,meteorx1-32,meteory1+40,meteorx1-45,meteory1+45,meteorx1+25,meteory1+50,fill="orange")
                        
                        
        #Choosing if the colour of the lantern should be bright orange or just orange
        if frameCount % 2 == 0:     
                lanterncolour = "#ff860d"
        else:
                lanterncolour = "orange"

        #Calling function to draw the lanterns        
        lanternsontemple()

        #Updating the screen
        screen.update()

        #Give some time so the user can see the image
        sleep(0.05)

        #Refreshing the screen by deleting parts of the screen
        screen.delete(lantern1,lantern2,lantern3,lantern4)


        
