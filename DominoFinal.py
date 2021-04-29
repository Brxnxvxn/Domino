#Author: Branavan Keethabaskaran
#Date: Novemeber 23, 2020
#Purpose: Draw and change the value and size of a domino

import random
from tkinter import *



#Author: Branavan Keethabaskaran
#Date: Wednesday, November 18, 2020
#Purpose: Create a Domino
#Data Elements: Value, Size, Diameter, Gap, Orientation, Face, all data fields use to create the domino
#Methods: __init__ : sets data elements
#         __str__: converts domino value as string
#         getValue: gets value of domino from user
#         setValue: sets value of domino
#         flip: flips values of domino
#         setOrientation: sets domino to horizontal or vertical
#         setSize: sets the size of the domino
#         setFace: decides if domino is face up or face down
#         randomize: randomly changes the dominos value
#         draw: draw the dominos using canvas
#         __add__,  adds two dominoes together
#         __sub__, subtracts domino from anther domino
#         __mul__, finds the product of the two dominos
#         __gt__, overloads the ">" operator
#         __lt__, overloads the "<" operator
#         __ge__, overloads the ">=" operator
#         __le__, overloads the "<=" operator
#         __==__, overloads the "==" operator
#         __!=__, overloads the "!=" operator
class Domino:

    def __init__(self, size = 30):

        self.value = random.randint(0, 66)

        while self.value // 10 > 6 or self.value % 10 > 6:
            self.value = random.randint(0, 66)

        self.size = size
        self.diameter = size // 5
        self.gap = self.diameter // 2
        self.orientation = True
        self.face = True

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: Print the domino value as a formatted string
    #Input: None
    #Return: value, domino value as string
    def __str__(self):
        return str(self.value)


    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: gets the value of domino from user through console
    #Input: None
    #Return: None
    def getValue(self):
        value = input("Enter an integer between 0-66 where each digit is less than or equal to 6: ")

        while value.isdigit() == False or int(value) // 10 > 6 or int(value) % 10 > 6:
            print("ERROR: Enter a number between 0 and 66 where each is digit is less than or equal to 6")
            value = input("Enter an integer between 0-66 where each digit is less than or equal to 6: ")

        self.value = int(value)
        print("Domino Value: ", self.value)


    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: takes the value of domino from paramater and sets it to self.value
    #Input: value, the domino value
    #Return: None    
    def setValue(self, value):

        num = str(value)
        
        if num.isdigit():
            if int(num) // 10 <= 6 and int(num) % 10 <= 6:
                self.value = int(num)

            else:
                messagebox.showerror("ERROR", "Enter a valid number between 0 and 66")
                self.value = 0


        else:
            messagebox.showerror("ERROR", "Enter a valid number between 0 and 66")
            self.value = 0

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: flips the value of the domino. Ex: 43 to 34
    #Input: None
    #Return: None        
    def flip(self):
        x = self.value // 10
        y = self.value % 10
        yx = str(y) + str(x)
        self.value = int(yx)

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: sets to orienation of the domino, given via parameter
    #Input: orient, the orientation of domino, vertical or horizontal, is a boolean
    #Return: None  
    def setOrientation(self, orient):
        if orient == True:
            self.orientation = True
        else:
            self.orientation = False


    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: sets the size of the domino given via parameter
    #Input: size, domino size
    #Return: None  
    def setSize(self, size = 30):

        if str(size).isdigit():
            if int(size) >= 30 and int(size) <= 100:
                self.size = int(size)
                self.diameter = self.size // 5
                self.gap = self.diameter // 2

        else:
#            messagebox.showerror("ERROR", "Enter a size between 30 and 100")
            self.size = 30
            self.diameter = self.size // 5
            self.gap = self.diameter // 2


    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: sets the face of the domino, either up or down
    #Parameters: faceup, the domino face
    #Return: None  
    def setFace(self, faceup):
        if faceup == True:
            self.face = True

        if faceup == False:
            self.face = False

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: randomizes the value and the size of the domino
    #Parameters: None
    #Return: None 
    def randomize(self):
        self.value = random.randint(0, 66)

        while self.value // 10 > 6 or self.value % 10 > 6:
            self.value = random.randint(0, 66)

    #Author: Branavan Keethabaskran
    #Date: November 23, 2020
    #Purpose: Randomize the size of the domino
    #Parameters: None
    #Return: None
    def randomizeSize(self):
        self.size = random.randint(30, 100)
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        


    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: draws the domino
    #Parameters: canvasSize, x, y, orienation, faceup, flip, all used to draw the domino
    #Return: None
    def draw(self, x, y, canvasSize, orientation = True, faceup = True, flip = False):

        prevSize = self.size

#        canvas.bind("<Key>", keyPressed)
#       canvas.place(x = 195, y = 55, width = canvasSize * 2, height = canvasSize)
#        canvas.focus_set()

        firstValue = self.value // 10
        secondValue = self.value % 10

        self.orientation = orientation
        self.face = faceup

        if self.orientation == True and self.face == True and flip == False:
            canvas.create_rectangle(x, y, x + self.size * 2, y + self.size, fill = "white")
            canvas.create_line(x +(self.size * 2) / 2, y, x +(self.size * 2) / 2, y + self.size, fill = "black")
            self.drawDot(x, y, firstValue)
            self.drawDot(x + self.size, y, secondValue)

        elif self.orientation == False and self.face == True and flip == False:
            canvas.create_rectangle(x, y, x + self.size, y + self.size * 2, fill = "white")
            canvas.create_line(x, y +(self.size * 2) / 2, x + self.size, y +(self.size * 2) / 2, fill = "black")
            self.orientation = False
            self.drawDot(x, y, firstValue)
            self.drawDot(x, y + self.size, secondValue)


        elif self.orientation == True and self.face == True and flip == True:
            self.flip()
            firstValue = self.value // 10
            secondValue = self.value % 10
            canvas.create_rectangle(x, y, x + self.size * 2, y + self.size, fill = "white")
            canvas.create_line(x +(self.size * 2) / 2, y, x +(self.size * 2) / 2, y + self.size, fill = "black")
            self.drawDot(x, y, firstValue)
            self.drawDot(x + self.size, y, secondValue)
            self.flip()

        elif self.face == False:
            canvas.create_rectangle(x, y, x + self.size * 2, y + self.size, fill = "white")
            canvas.create_line(x +(self.size * 2) / 2, y, x +(self.size * 2) / 2, y + self.size, fill = "black")

            tempX = x
            tempY = y
            for i in range(0, self.size // 5):
                canvas.create_line(tempX, tempY, tempX + self.size, tempY)
                tempY += 5

            tempX = x
            tempY = y

            for i in range(0, self.size // 5):
                canvas.create_line(tempX + self.size, tempY, tempX + self.size * 2, tempY)
                tempY += 5

        
                



    #Author: Branavan Keethabaskaran
    #Date: Novemeber 23, 2020
    #Purpose: draws the dots of domino
    #Parameters: x, y, value, used to draw dots
    #Return: None
    def drawDot(self, x, y, value):

        gap = self.gap
        diameter = self.diameter

        
        if self.orientation == True:
            if value == 1:
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")

            elif value == 2:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 3:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 4:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 5:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 6:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + gap, x + (gap * 2) + (diameter * 2), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 3) + (diameter * 2), x + (gap * 2) + (diameter * 2), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

        elif self.orientation == False:
            if value == 1:
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")

            elif value == 2:
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 3:
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 4:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

            elif value == 5:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 2) + diameter, y + (gap * 2) + diameter, x + (gap * 2) + (diameter * 2), y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")
                
            elif value == 6:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + gap, x + (gap * 3) + (diameter * 3), y + gap + diameter, fill = "black")
                canvas.create_oval(x + gap, y + (gap * 2) + diameter, x + gap + diameter, y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 2) + diameter, x + (gap * 3) + (diameter * 3), y + (gap * 2) + (diameter * 2), fill = "black")
                canvas.create_oval(x + (gap * 3) + (diameter * 2), y + (gap * 3) + (diameter * 2), x + (gap * 3) + (diameter * 3), y + (gap * 3) + (diameter * 3), fill = "black")
                canvas.create_oval(x + gap, y + (gap * 3) + (diameter * 2), x + gap + diameter, y + (gap * 3) + (diameter * 3), fill = "black")

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: decides the weight of the domino
    #Parameters: None
    #Return: None
    def checkWeight(self):
        firstDigit = self.value // 10
        secondDigit = self.value % 10

        if firstDigit > secondDigit:
            self.flip()

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "+" arithmetic operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: add, the sum of the dominos   
    def __add__(self, secondDomino):
        add = 0
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        add = self.value + secondDomino.value

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return add
    
    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "-" arithmetic operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: sub, the difference of the dominos 
    def __sub__(self, secondDomino):
        sub = 0
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        sub = self.value - secondDomino.value

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return sub

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "*" arithmetic operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: mul, the product of the dominos
    def __mul__(self, secondDomino):
        mul = 0
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        mul = self.value * secondDomino.value

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return mul
    
    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the ">" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __gt__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value > secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result       

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "<" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __lt__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value < secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the ">=" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __ge__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value >= secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result
    
    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "<=" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __le__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value <= secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "==" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __eq__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value == secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result

    #Author: Branavan Keethabaskaran
    #Date: December 3, 2020
    #Purpose: overloads the "!=" operator
    #Parameters: secondDomino, the domino object used when comparing
    #Return: result, a boolean
    def __ne__(self, secondDomino):
        result = False
        originalSelf = self.value
        originalSecond = secondDomino.value

        self.checkWeight()
        secondDomino.checkWeight()

        if self.value != secondDomino.value:
            result = True

        self.setValue(originalSelf)
        secondDomino.setValue(originalSecond)

        return result
            
#Author: Branavan Keethabaskaran
#Date: Novemeber 23, 2020
#Purpose: detects user input from keyboard
#Parameters: None
#Return: None

#def keyPressed(event):
#    if event.char == "d":
#        canvas.delete("all")

#        x = 5
#        y = 5
        
#        if randomValue.get() == 1 and randomSize.get() == 1:
#            d.randomize()
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = False)
#            x = x + d.size * 2 + 5
#            d.randomize()
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = True)
#            x = x + d.size * 2 + 5
#            d.randomize()
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = False, faceup = True, flip = False)
#            d.randomize()
#           d.randomizeSize()
#           d.draw(5, 200, 300, faceup = False)            

#        elif randomValue.get() == 1 and randomSize.get() == 0:
#           size = str(dominoSize.get())
#            d.setSize(size)
#            d.randomize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = False)
#            x = x + d.size * 2 + 5
#            d.randomize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = True)
#            x = x + d.size * 2 + 5
#            d.randomize()
#            d.draw(x, y, 300, orientation = False, faceup = True, flip = False)
#            d.randomize()
#            d.draw(10, 200, 300, faceup = False)
            
#        elif randomValue.get() == 0 and randomSize.get() == 1:
#            value = str(dominoValue.get())
#            d.setValue(value)
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = False)
#            x = x + d.size * 2 + 5
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = True)
#            x = x + d.size * 2 + 5
#            d.randomizeSize()
#            d.draw(x, y, 300, orientation = False, faceup = True, flip = False)
#            d.randomizeSize()
#            d.draw(10, 200, 300, faceup = False)
#            
#        elif dominoValue.get() != "" and dominoValue.get() != "":
#            value = str(dominoValue.get())
#            size = str(dominoSize.get())
#            d.setValue(value)
#            d.setSize(size)
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = False)
#            x = x + d.size * 2 + 5
#            d.draw(x, y, 300, orientation = True, faceup = True, flip = True)
#            x = x + d.size * 2 + 5
#            d.draw(x, y, 300, orientation = False, faceup = True, flip = False)
#            d.draw(10, 200, 300, faceup = False)

#    elif event.char == "x":
#        form.destroy()


#Author: Branavan Keethabaskaran
#Date: Novemeber 23, 2020
#Purpose: sets focus to canvas when clicked
#Parameters: None
#Return: None
#def callback(event):
#    canvas.focus_set()


##MAIN PROGRAM##
#form = Tk()
#form.geometry("800x400")
#canvas = Canvas(form, bg = "green")

#variables
#dominoValue = StringVar()
#dominoSize = StringVar()
#randomValue = IntVar()
#randomValue.set(0)
#randomSize = IntVar()
#randomSize.set(0)

#d = Domino()

#title
#title = Label(form, text = "Dominos", font = (None, 30), relief = SUNKEN).place(x = 0, y =  0, width = 800, height = 50)

#labelFrame
#valueFrame = LabelFrame(form, text = "Value").place(x = 5, y = 100, width = 185, height = 80)
#sizeFrame = LabelFrame(form, text = "Size").place(x = 5, y = 250, width = 185, height = 80)

#Entry
#valueEntry = Entry(valueFrame, textvariable=dominoValue).place(x = 10, y = 130, height = 30, width = 90)
#sizeEntry = Entry(sizeFrame, textvariable=dominoSize).place(x = 10, y = 280, height = 30, width = 90)

#CheckButtons
#valueCheck = Checkbutton(valueFrame, text = "Random", variable = randomValue, onvalue = 1, offvalue = 0).place(x = 100, y = 130, height = 30, width = 80)
#sizeCheck = Checkbutton(sizeFrame, text = "Random", variable = randomSize, onvalue = 1, offvalue = 0).place(x = 100, y = 280, height = 30, width = 80)


#canvas.bind("<Button-1>", callback)
#canvas.bind("<Key>", keyPressed)
#canvas.place(x = 195, y = 55, width = 600, height = 340)

#canvas.focus_set()


#Author: Branavan Keethabaskaran
#Date: November 24, 2020
#Purpose: Create a "hand" that holds the three domino objects. Uses the domino class created in prev assignment


#Author: Branavan Keethabaskaran
#Date: Tuesday, November 24, 2020
#Purpose: Create a hand of dominos
#Data Elements: size, firstDomino, secondDomino, and thirdDomino, three dominoObjects that each have a size
#Methods: __init__ : sets data elements
#         __str__: converts domino values into a string
#         setSize: sets the size of all the domino
#         sort: sorts the dominos from smallest to largest. the "lessor" value is the weight of the domino
#         roll: randomizes the value of each domino
#         getRun: finds the amount of dominos that can be connected or joined together. 
#         drawHand: draw the dominoes of the hand using draw method from domino class
#         drawRun: draws the dominoHand with the run. Shows the connected parts of the domino
class Hand: 

    def __init__(self, size):

        self.size = str(size)

        if self.size.isdigit():
            if int(self.size) >= 30 and int(self.size) <= 100:
                self.size = int(size)

            else:
                self.size = 30
        else:
            self.size = 30
            
        self.firstDomino = Domino(size = self.size)
        self.secondDomino = Domino(size = self.size)
        self.thirdDomino = Domino(size = self.size)

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 24, 2020
    #Purpose: Print the domino values as a formatted string
    #Input: None
    #Return: dominos, returns domino values as a string 
    def __str__(self):
        dominoOne = str(self.firstDomino)
        dominoTwo = str(self.secondDomino)
        dominoThree = str(self.thirdDomino)

        dominos = dominoOne + "-" + dominoTwo + "-" + dominoThree
        
        return dominos

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 24, 2020
    #Purpose: sets the size of the three dominos
    #Input: size, default = 60
    #Return: None  
    def setSize(self, size = 60):
        if size.isdigit():
            if int(size) >= 30 or int(size) <= 100:
                self.size = int(size)

        else:
            self.size = 60

        self.firstDomino.setSize(self.size)
        self.secondDomino.setSize(self.size)
        self.thirdDomino.setSize(self.size)

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 24, 2020
    #Purpose: sorts the dominos from smallest to largest. the "lessor" value is the weight of the domino
    #Input: canvasSize, x, y, used to draw the sorted hand
    #Return: None  
    def sort(self, x, y, canvasSize):
        originalFirst = self.firstDomino.value
        originalSecond = self.secondDomino.value
        originalThird = self.thirdDomino.value        
                    
        firstOne = self.firstDomino.value // 10
        secondOne = self.firstDomino.value % 10

        firstTwo = self.secondDomino.value // 10
        secondTwo = self.secondDomino.value % 10

        firstThree = self.thirdDomino.value // 10
        secondThree = self.thirdDomino.value % 10

        if firstOne > secondOne:
            self.firstDomino.flip()

        if firstTwo > secondTwo:
            self.secondDomino.flip()

        if firstThree > secondThree:
            self.thirdDomino.flip()


        firstWeight = self.firstDomino.value
        secondWeight = self.secondDomino.value
        thirdWeight = self.thirdDomino.value

        if firstWeight >= secondWeight and secondWeight >= thirdWeight:
            self.thirdDomino.draw(x, y, canvasSize)
            self.secondDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.firstDomino.draw(x + self.size * 4 + 10, y, canvasSize)                

        elif firstWeight >= thirdWeight and secondWeight <= thirdWeight:
            self.secondDomino.draw(x, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.firstDomino.draw(x + self.size * 4 + 10, y, canvasSize)  

        elif firstWeight <= secondWeight and thirdWeight <= firstWeight:
            self.thirdDomino.draw(x, y, canvasSize)
            self.firstDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.secondDomino.draw(x + self.size * 4 + 10, y, canvasSize)

        elif secondWeight >= thirdWeight and thirdWeight >= firstWeight:
            self.firstDomino.draw(x, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.secondDomino.draw(x + self.size * 4 + 10, y, canvasSize)

        elif thirdWeight >= firstWeight and firstWeight >= secondWeight:
            self.secondDomino.draw(x, y, canvasSize)
            self.firstDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 4 + 10, y, canvasSize) 

        elif thirdWeight >= secondWeight and firstWeight <= secondWeight:
            self.firstDomino.draw(x, y, canvasSize)
            self.secondDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 4 + 10, y, canvasSize)      

        #reset values
        self.firstDomino.setValue(originalFirst)
        self.secondDomino.setValue(originalSecond)
        self.thirdDomino.setValue(originalThird)        

        
    #Author: Branavan Keethabaskaran
    #Date: Novemeber 24, 2020
    #Purpose: randomizes the value of each domino
    #Input: None
    #Return: None      
    def roll(self):
        self.firstDomino.randomize()
        self.secondDomino.randomize()
        self.thirdDomino.randomize()

    #Author: Branavan Keethabaskaran
    #Date: Novemeber 24, 2020
    #Purpose: draw the three dominos
    #Input: x, y, canvasSize, used to draw the three dominos
    #Return: None     
    def drawHand(self, x, y, canvasSize):
        self.firstDomino.draw(x, y, canvasSize)
        self.secondDomino.draw(x + self.size * 2 + 5, y, canvasSize)
        self.thirdDomino.draw(x + self.size * 4 + 10, y, canvasSize)

           
    #Author: Branavan Keethabaskaran
    #Date: Novemeber 26, 2020
    #Purpose: finds the amount of dominos that can be connected or joined together. 
    #Input: None
    #Return: run, the amount of dominos that can be connected    
    def getRun(self):
        run = 0
        indicator = 0
        secondIndicator = 0
        thirdIndicator = 0
        
        firstDomOne = self.firstDomino.value // 10
        firstDomTwo = self.firstDomino.value % 10
        secondDomOne = self.secondDomino.value // 10
        secondDomTwo = self.secondDomino.value % 10
        thirdDomOne = self.thirdDomino.value // 10
        thirdDomTwo = self.thirdDomino.value % 10

        #Between first and second set
        if firstDomOne == secondDomOne:
            run += 1
            indicator = 1

        elif firstDomOne == secondDomTwo:
            run += 1
            indicator = 2


        elif firstDomTwo == secondDomOne:
            run += 1
            indicator = 3

        elif firstDomTwo == secondDomTwo:
            run += 1
            indicator = 4


        #Between second and third        
        if thirdDomOne == secondDomOne and indicator != 1 and indicator != 3:
            run += 1
            secondIndicator = 5


        elif thirdDomOne == secondDomTwo and indicator != 2 and indicator != 4:
            run += 1
            secondIndicator = 6

        elif thirdDomTwo == secondDomOne and indicator != 1 and indicator != 3:
            run += 1
            secondIndicator = 7


        elif thirdDomTwo == secondDomTwo and indicator != 2 and indicator != 4:
            run += 1
            secondIndicator = 8

        
        #Between third and first
        if firstDomOne == thirdDomOne and indicator != 1 and indicator != 2 and secondIndicator != 5 and secondIndicator != 6 and run < 2:
            run += 1
            thirdIndicator = 9

        elif firstDomOne == thirdDomTwo and indicator != 1 and indicator != 2 and secondIndicator != 7 and secondIndicator != 8 and run < 2:
            run += 1
            thirdIndicator = 10

        elif firstDomTwo == thirdDomOne and indicator != 3 and indicator != 4 and secondIndicator != 5 and secondIndicator != 6 and run < 2:
            run += 1
            thirdIndicator = 11

        elif firstDomTwo == thirdDomTwo and indicator != 3 and indicator != 4 and secondIndicator != 7 and secondIndicator != 8 and run < 2:
            run += 1
            thirdIndicator = 12

        if run == 1:
            run = 2

        elif run >= 2:
            run = 3

        #special case
        if self.firstDomino.value == self.secondDomino.value:
            if firstDomOne == thirdDomOne or firstDomOne == thirdDomTwo or firstDomTwo == thirdDomOne or firstDomTwo == thirdDomTwo:
                run = 3

        self.firstDomino.flip()

        if self.firstDomino.value == self.secondDomino.value:
            if firstDomOne == thirdDomOne or firstDomOne == thirdDomTwo or firstDomTwo == thirdDomOne or firstDomTwo == thirdDomTwo:
                run = 3

        self.firstDomino.flip()
            
        return run            



    #Author: Branavan Keethabaskaran
    #Date: Novemeber 27, 2020
    #Purpose: draws the dominoHand with the run. Shows the connected parts of the domino
    #Input: x, y, canvasSize, used to draw dominos
    #Return: None 
    def drawRun(self, canvasSize, x, y):

        originalFirst = self.firstDomino.value
        originalSecond = self.secondDomino.value
        originalThird = self.thirdDomino.value

        #special case
        if self.firstDomino.value == self.secondDomino.value:
            if self.firstDomino.value // 10 == self.thirdDomino.value // 10 or self.firstDomino.value // 10 == self.thirdDomino.value % 10 \
               or self.firstDomino.value % 10 == self.thirdDomino.value // 10 or self.firstDomino.value % 10 == self.thirdDomino.value % 10:
                self.secondDomino.flip()

        else:        
            self.firstDomino.flip()
        
        if self.firstDomino.value == self.secondDomino.value and (self.firstDomino.value // 10 == self.thirdDomino.value // 10 or self.firstDomino.value // 10 == self.thirdDomino.value % 10):
            self.secondDomino.flip()

        elif self.firstDomino.value == self.secondDomino.value and (self.firstDomino.value % 10 == self.thirdDomino.value // 10 or self.firstDomino.value % 10 == self.thirdDomino.value % 10):
            self.firstDomino.flip()
        
        else:
            self.firstDomino.setValue(originalFirst)
            self.secondDomino.setValue(originalSecond)
            self.thirdDomino.setValue(originalThird)
                
            #Between first and second set
            if self.firstDomino.value // 10 == self.secondDomino.value // 10:

                self.firstDomino.flip()

            elif self.firstDomino.value // 10 == self.secondDomino.value % 10:

                self.firstDomino.flip()
                self.secondDomino.flip()

            elif self.firstDomino.value % 10 == self.secondDomino.value % 10:
                self.secondDomino.flip()


            #Between second and third        
            if self.thirdDomino.value // 10 == self.secondDomino.value // 10 and self.firstDomino.value % 10 != self.secondDomino.value // 10:
                self.secondDomino.flip()

            elif self.thirdDomino.value % 10 == self.secondDomino.value // 10 and self.firstDomino.value % 10 != self.secondDomino.value // 10 :
                self.secondDomino.flip()
                self.thirdDomino.flip()

            elif self.thirdDomino.value % 10 == self.secondDomino.value % 10:
                self.thirdDomino.flip()

                
            #Between third and first
            if self.firstDomino.value // 10 == self.thirdDomino.value // 10 and self.thirdDomino.value // 10 != self.secondDomino.value % 10:
                self.thirdDomino.flip()


            elif self.firstDomino.value % 10 == self.thirdDomino.value // 10 and self.firstDomino.value % 10 != self.secondDomino.value // 10 and self.secondDomino.value % 10 != self.thirdDomino.value // 10:
                self.firstDomino.flip()
                self.thirdDomino.flip()

            elif self.firstDomino.value % 10 == self.thirdDomino.value % 10 and self.firstDomino.value % 10 != self.secondDomino.value // 10:
                self.firstDomino.flip()
                    


        #rearranging of dominos 
        if self.secondDomino.value % 10 != self.thirdDomino.value // 10 and self.firstDomino.value // 10 == self.thirdDomino.value % 10:
            self.thirdDomino.draw(x, y, canvasSize)
            self.firstDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.secondDomino.draw(x + self.size * 4 + 10, y, canvasSize)

        elif self.secondDomino.value // 10 != self.firstDomino.value % 10 and self.firstDomino.value // 10 == self.thirdDomino.value % 10:
            self.secondDomino.draw(x, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.firstDomino.draw(x + self.size * 4 + 10, y, canvasSize)

        else:
            self.firstDomino.draw(x, y, canvasSize)
            self.secondDomino.draw(x + self.size * 2 + 5, y, canvasSize)
            self.thirdDomino.draw(x + self.size * 4 + 10, y, canvasSize)

        #reset values
        self.firstDomino.setValue(originalFirst)
        self.secondDomino.setValue(originalSecond)
        self.thirdDomino.setValue(originalThird)

            
            
#Author: Branavan Keethabaskaran
#Date: Novemeber 26, 2020
#Purpose: detects user input from keyboard
#Input: event
#Return: None                     
#def keyPressed(event):
#    if event.char == "h":
#        canvas.delete("all")
#        dominoHand = Hand(50)
#        dominoHand.roll()
#        print(dominoHand)
#        dominoHand.drawHand(5, 5, canvas)
#        sortedHand = dominoHand.sort(5, 80, canvas)
#        print("sort: ", sortedHand)
#        run = dominoHand.getRun()
#        print(run)
#        dominoHand.drawRun(canvas, 5, 150)
        

#    elif event.char == "g":
#        anotherDom = Hand(50)

#        zero = 0
#        two = 0
#        three = 0
#        num = 0

#        for i in range(0, 10000):
#            anotherDom.roll()
#            tenThousandRun = anotherDom.getRun()

#            if tenThousandRun == 0:
#                zero += 1

#            elif tenThousandRun == 2:
#                two += 1

#            else:
#                three += 1

#            num += 1

#        zeroPercentage = zero / 10000
#        twoPercentage = two / 10000
#        threePercentage = three / 10000

#        print(num)
#        print("Run of 0:", zero, "Percentage", "%2.1f"%(zeroPercentage * 100) + "%")
#        print("Run of 2:", two, "Percentage", "%2.1f"%(twoPercentage * 100) + "%")
#        print("Run of 3:", three, "Percentage", "%2.1f"%(threePercentage * 100) + "%")
            

#Author: Branavan Keethabaskaran
#Date: Novemeber 29, 2020
#Purpose: validates entry boxes
#Input: value, high, low
#Return: value, validated value
#def validate(value, high, low):
#    if value != "":
#        if value.isdigit():
#            if int(value) < high + 1 and int(value) > low - 1:
#                value = int(value)

#            else:
#                value = 0
#                messagebox.showerror("ERROR", "Enter a value between" + str(high) + "and" + str(low))
                

#        else:
#            value = 0
#            messagebox.showerror("ERROR", "Enter a value between" + str(high) + "and" + str(low))
#    else:
#        value = 0
#        messagebox.showerror("ERROR", "Enter a value between" + str(high) + "and" + str(low))

#    return int(value)
        
    

#Author: Branavan Keethabaskaran
#Date: Novemeber 29, 2020
#Purpose: used to display dominos on gui interface
#Input: None
#Return: None
#def clickRoll():
                

#        x = validate(xVar.get(), 400, 0)
#        y = validate(yVar.get(), 300, 0)

#        canvas.delete("all")
#        if randomSize.get() == 0:
#            dominoHand = Hand(sizeVar.get())
#        else:
#            size = random.randint(30, 100)
#            dominoHand = Hand(size)
#        dominoHand.roll()
#        dominoHand.drawHand(x, y, 400)
#        dominoHand.sort(x, y + dominoHand.size + 5, 400)
#        run = dominoHand.getRun()
#        dominoHand.drawRun(400, x, y + dominoHand.size * 2 + 10)

#        statList.delete(0, 5)
#        statList.insert(1, "Domino: " + str(dominoHand))
#        statList.insert(2, "Run: " + str(run))



        
#Author: Branavan Keethabaskaran
#Date: Novemeber 29, 2020
#Purpose: used to display run percentages on gui interface
#Input: None
#Return: None
#def clickStats():
#        statList.delete(0, 5)        
#        anotherDom = Hand(50)
#
#        zero = 0
#        two = 0
#        three = 0
#        num = 0

#        for i in range(0, 10000):
#            anotherDom.roll()
#            tenThousandRun = anotherDom.getRun()

#            if tenThousandRun == 0:
#                zero += 1

#            elif tenThousandRun == 2:
#                two += 1

#            else:
#                three += 1

#            num += 1

#        zeroPercentage = zero / 10000
#        twoPercentage = two / 10000
#        threePercentage = three / 10000
        
#        statList.insert(1, "Run of 0: " + str(zero) + "                                  " + "Percentage of 0: " + "%2.1f"%(zeroPercentage * 100) + "%")
#        statList.insert(2, " ")
#        statList.insert(3, "Run of 2: " + str(two) +  "                                  " + "Percentage of 2: " + "%2.1f"%(twoPercentage * 100) + "%") 
#        statList.insert(4, "")
#        statList.insert(5, "Run of 3: " +  str(three) + "                                  " + "Percentage of 3: " + "%2.1f"%(threePercentage * 100) + "%") 

##### MAIN PROGRAM #######
#form = Tk()

#sizeVar = IntVar()
#randomSize = IntVar()
#xVar = StringVar("")
#yVar = StringVar("")

#form.geometry("1165x360")

##labels
#Label(form, text = "Domino", relief = SUNKEN, font = (None, 20)).place(x = 0, y = 0, width = 500, height = 30)
#Label(form, text = "x coordinate of dominos", relief = GROOVE).place(x = 230, y = 60, height = 20, width = 180)
#Label(form, text = "y coordinate of dominos", relief = GROOVE).place(x = 230, y = 110, height = 20, width = 180)

##scale
#scale = Scale(form, variable = sizeVar, from_ = 30, to = 100, orient = HORIZONTAL, label = "Size").place(x = 5, y = 35, width = 200, height = 80)

##checkbutton
#sizeCheck = Checkbutton(form, text = "Random Size", variable = randomSize, onvalue = 1, offvalue = 0, font = (None, 10)).place(x = 5, y = 110 , height = 20, width = 200)

##entries
#xCoord = Entry(form, text = "x coordinate of dominos", textvariable = xVar).place(x = 420, y = 60, width = 75, height = 20)
#yCoord = Entry(form, text = "y coordinate of dominos", textvariable = yVar).place(x = 420, y = 110, width = 75, height = 20)

##buttons
#roll = Button(form, text = "ROLL", command=clickRoll).place(x = 20, y = 160, width = 200, height = 30)
#stats = Button(form, text = "STATISTICS", command=clickStats).place(x = 250, y = 160, width = 200, height = 30)

##canvas
#canvas = Canvas(form, bg = "blue", width = 650, height = 345)

##listbox
#statList = Listbox(form)

#statList.place(x = 5, y = 205, width = 490, height = 145)
#canvas.bind("<Key>", keyPressed)
#canvas.place(x = 505, y = 5)
#canvas.focus_set()
                                                      
#mainloop()
        
        
########### MAIN PROGRAM OOP3: Overloading ###########

#begin = input("Enter 'y' to begin: ")
#begin = begin.strip()
#begin = begin.lower()

#while begin == "y":

#    firstDomino = Domino()
#    firstDomino.getValue()
#    secondDomino = Domino()
#    secondDomino.getValue()


#    mathOperators = "y"

#    while mathOperators == "y":
#        print("Arithmetic Operators: +, -, *")
#        operatorChoice = input("Enter the arithmetic operator you would like to use: ")
#        operatorChoice = operatorChoice.strip()
#        operatorChoice = operatorChoice.lower()

#        if operatorChoice == "+":
#            add = firstDomino + secondDomino
#            print(firstDomino, "+", secondDomino, "=", add)

#        elif operatorChoice == "-":
#            sub = firstDomino - secondDomino
#            print(firstDomino, "-", secondDomino, "=", sub)

#        elif operatorChoice == "*":
#            mul = firstDomino * secondDomino
#            print(firstDomino, "*", secondDomino, "=", mul)

#        mathOperators = input("Enter 'y' to continue using the arithmetic operators: ")
#        mathOperators = mathOperators.strip()
#        mathOperators = mathOperators.lower()

#    compareOperators = "y"

#    while compareOperators == "y":
#        print("Comparison Operators: >, <, >=, <=, ==, !=")
#        compare = input("Enter a comparison operator to compare the dominos: ")
#        compare = compare.strip()
#        compare = compare.lower()


#        if compare == ">":
#            if firstDomino > secondDomino:
#               print("yes, the first domino is greater than the second domino")

#            else:
#                print("no, the first domino is not greater than the second domino")

#        if compare == "<":
#            if firstDomino < secondDomino:
#                print("yes, the first domino is less than the second domino")

#            else:
#                print("no, the first domino is not less than the second domino")
#                        
#        if compare == ">=":
#            if firstDomino >= secondDomino:
#                print("yes, the first domino is greater than or equal to the second domino")

#            else:
#                print("no, the first domino is less than the second domino")

#        if compare == "<=":
#            if firstDomino <= secondDomino:
#                print("yes, the first domino is less than or equal to the second domino")
#            else:
#                print("no, the first domino is greater than the second domino")
        
#        if compare == "==":
#            if firstDomino == secondDomino:
#                print("yes, the first domino is equal to the second domino")

#            else:
#                print("no, the first domino is not equal to the second domino")

#        if compare == "!=":
#            if firstDomino != secondDomino:
#               print("yes, the first domino is not equal to the second domino")

#            else:
#                print("No, the first domino is equal to the second domino")


#        compareOperators = input("Enter 'y' to continuing comparing: ")
#        compareOperators = compareOperators.strip()
#        compareOperators = compareOperators.lower()

#    begin = input("Enter 'y' to begin: ")
#    begin = begin.strip()
#    begin = begin.lower()
    


#Author: Branavan Keethabaskaran
#Date: Thursday, Decemeber 10, 2020
#Purpose: Incorporate lists into domino program


#Author: Branavan Keethabaskaran
#Date: Thursday, Decemeber 10, 2020
#Purpose: Create a list of dominoes
#Data Elements: Value, Size, Diameter, Gap, Orientation, Face, all data fields use to create the domino
#Methods: __init__ : initializes data elements
#         __str__: converts domino list into string
#         initDeal: Randomizes the dominoes in the domino list
#         calcTotal: calculate the total value of the dominos in the list
#         findLargest: find the largest domino in list
#         findPossible: find the first match to a given integer paramater
#         clacFreq: return the frequency of a domino in the list
#         insertAt: inserts a domino into a given position
#         removeAt: remove a domino at a given position
#         drawList: draws the list of dominos
#         setSize: sets the size of each domino in the list
#         linearSearch: performs a linear search on the list given a value *compares WEIGHT of domino
#         sentinelSearch: perfroms a sentinel search on the list given a value *compares WEIGHT of domino
#         binarySearch: performs a binary search on the list given a value *compares WEIGHT of domino
#         exchangeSort: performs a bubble sort on the list given an order *compares WEIGHT of domino
#         selectionSort: performs a bubble sort on the list given an order *compares VALUE of domino    *COMPARING WEIGHT DOES NOT WORK CORRECTLY FOR ME*
#         insertionSort: performs a bubble sort on the list given an order *compares WEIGHT of domino
class DominoGroup:

    #Author: Branavan Keethabaskaran
    #Date: Thursday, Decemeber 10, 2020
    #Purpose: initalize data elements
    #Paramaters: size, the size of the list
    #Return: None
    def __init__(self, size = 0):
        self.list = []
        if str(size).isdigit():
            if int(size) >= 0 and int(size) <= 7:
                    self.size = int(size)
            else:
                self.size = 0
        else:
            self.size = 0
        for i in range(0, self.size):
            self.list.append(Domino())


    #Author: Branavan Keethabaskaran
    #Date: Thursday, Decemeber 10, 2020
    #Purpose: returns domino list as string
    #Paramaters: None
    #Return: string, list formatted as a string
    def __str__(self):
        stringList = []

        for i in range(0, self.size):
            domino = self.list[i]
            firstDigit = str(domino.value // 10)
            secondDigit = str(domino.value % 10)
            stringList.append(firstDigit + "|" + secondDigit)

        string = str(stringList) + " size: " + str(self.size)

        return string

    #Author: Branavan Keethabaskaran
    #Date: Thursday, Decemeber 10, 2020
    #Purpose: randomizes domino values in list
    #Paramaters: None
    #Return: None
    def initDeal(self):
        unique = False
        duplicateCounter = 0
        
        for i in range(0, self.size):
            self.list[i].randomize()
                
        while unique == False:
            self.list.sort()
            for i in range(0, self.size - 1):
                if self.list[i] == self.list[i + 1]:
                    self.list[i].randomize()
                    duplicateCounter += 1

            if duplicateCounter == 0:
                unique = True

            duplicateCounter = 0
               
    #Author: Branavan Keethabaskaran
    #Date: Thursday, Decemeber 10, 2020
    #Purpose: calculates the total value of all the domino values in the list
    #Paramaters: None
    #Return: total, total value of list
    def calcTotal(self):
        totalTemp = Domino()
        totalTemp.setValue(0)
        total = 0
        finalTotal = 0
        for i in range(0, self.size):
            total = totalTemp + self.list[i] + total
            
        return total


    #Author: Branavan Keethabaskaran
    #Date: Friday, Decemeber 11, 2020
    #Purpose: find the largest domino in list
    #Paramaters: None
    #Return: largest, the largest domino in list 
    def findLargest(self):
        largest = Domino()
        largest.setValue(0)
        for i in range(0, self.size):
            if self.list[i] > largest:
                largest.setValue(self.list[i])

        return largest

    #Author: Branavan Keethabaskaran
    #Date: Friday, Decemeber 11, 2020
    #Purpose: find the first match to a given integer paramater 
    #Paramaters: value, the integer that is searched for in the list
    #Return: match, the domino value that matches the given paramater
    # -1 represent not finding a match
    def findPossible(self, value):
        match = 0
        first = False
        counter = 0

        while first == False:
            if self.list[counter].value // 10  == value:
                match = self.list[counter].value
                first = True
                
            elif self.list[counter].value % 10 == value:
                match = self.list[counter].value
                first = True
                
            elif self.list[counter].value == value:
                match = self.list[counter].value            
                first = True

            counter += 1

            if counter >= self.size:
                first = True

        if match == 0:
            match = -1

        return match

    #Author: Branavan Keethabaskaran
    #Date: Friday, Decemeber 11, 2020
    #Purpose: return the frequency of a domino in the list 
    #Paramaters: value, integer that is checked for frequency of
    #Return: freq, the frequency of a domino in the list
    def calcFreq(self, value):
        freq = 0
        valueDomino = Domino()
        valueDomino.setValue(value)
        
        for i in range(0, self.size):
            if self.list[i] == valueDomino:
                freq += 1

        return freq

    #Author: Branavan Keethabaskaran
    #Date: Friday, Decemeber 11, 2020
    #Purpose: inserts a domino into a given position 
    #Paramaters: value and position, the value of the domino and the position it is placed in the list
    #Return: None
    def insertAt(self, position, value):
        valueDomino = Domino()
        valueDomino.setValue(value)
        if self.size < position:
            position = self.size

        elif position < 0:
            position = 0

        self.list.insert(position, valueDomino)
        self.size += 1


    #Author: Branavan Keethabaskaran
    #Date: Friday, Decemeber 11, 2020
    #Purpose: removes a domino at a given position 
    #Paramaters: position, the position of the domino
    #Return: None
    def removeAt(self, position):
        if position >= 0 and position <= self.size:
            if position == 0:
                position = 1
                
            del self.list[position - 1]
            self.size -= 1

    #Author: Branavan Keethabaskaran
    #Date: Saturday, Decemeber 12, 2020
    #Purpose: draw the domino list on a canvas
    #Paramaters: canvas, x, y, canvasSize, used to draw the list
    #Return: None
    def drawList(self, canvas, x, y, canvasSize = 0):
        for i in range(0, self.size):
            self.list[i].draw(x, y, canvas)
            x += (self.list[i].size * 2 + 5)

            if (x + self.list[i].size * 2 + 5) >= canvasSize: #moves the dominoes down if the canvas size is not large enough
               y += (self.list[i].size + 5)
               x = 5

    #Author: Branavan Keethabaskaran
    #Date: Saturday, Decemeber 12, 2020
    #Purpose: sets the size of each domino to a given size
    #Paramaters: size, the size of each domino
    #Return: None
    def setSize(self, size):
        for i in range(0, self.size):
            self.list[i].setSize(size)

#print("THE DOMINO LIST")
#begin = input("Enter 'y' to begin: ")
#begin = begin.strip()
#begin = begin.lower()

#while begin == "y":
#    userSize = input("Enter the size of your domino list. Must be between 0 and 7: ")
#    dominoList = DominoGroup(size = userSize)
#    print("Domino List: ", dominoList)

#    userRandomize = input("Enter 'y' if you'd like to randomize the domino list once again: ")
#    userRandomize = userRandomize.strip()
#    userRandomize = userRandomize.lower()

#    if userRandomize == "y":
#        dominoList.initDeal()
#        print("Domino List: ", dominoList)

#    total = dominoList.calcTotal()
#    largest = dominoList.findLargest()    
#    print("Total of Domino: ", total)
#    print("Largest of List: ", largest)

#    userPossible = input("Enter a domino value you'd like to find in the list. Press 'Enter' to skip: ")
    
#    if userPossible.isdigit():
#        userPossible = int(userPossible)
#        match = dominoList.findPossible(userPossible)
#        print("Match: ", match)

#    userFreq = input("Enter a domino value you'd like to find the frequency of. Press 'Enter' to skip: ")

#    if userFreq.isdigit():
#        userFreq = int(userFreq)
#        freq = dominoList.calcFreq(userFreq)
#        print("Frequency of", userFreq, "in list: ", freq)


#    insertCheck = input("Would you like to insert a domino into the list. Enter 'y': ")
#    inserCheck = insertCheck.strip()
#    insertCheck = insertCheck.lower()

#    if insertCheck == "y":
#        userInsert = int(input("Enter a domino value you'd like to add to the list. Press 'Enter' to skip: "))     
#        insertPosition = int(input("Enter the position you'd like to insert the domino value: "))
#        dominoList.insertAt(insertPosition, userInsert)
#        print("Domino List: ", dominoList)
        
#    removeCheck = input("Would you like to remove an integer at a certain position. Enter 'y': ")
#    removeCheck = removeCheck.strip()
#    removeCheck = removeCheck.lower()

#    if removeCheck == "y":
#        userRemove = int(input("Enter the position of the domino value you'd like to remove. Press 'Enter' to skip.: "))
#        dominoList.removeAt(userRemove)
#        print(dominoList)

#    userDraw = input("Enter 'y' if you'd like to draw the list: ")
#    userDraw = userDraw.strip()
#    userDraw = userDraw.lower()

#    if userDraw == "y":
#        drawSize = input("Enter the size of the dominos: ")
#        if drawSize.isdigit():
#            drawSize = int(drawSize)
#            dominoList.setSize(drawSize)
            
#        form = Tk()
#        canvas = Canvas(form, width = 600, height = 430, bg = "blue")
#        canvasSize = 600 # the width of the canvas
#        canvas.pack()
#        dominoList.drawList(canvas, 5, 5, canvasSize = 600)
#        mainloop()

#    begin = input("Enter 'y' to begin: ")
#    begin = begin.strip()
#    begin = begin.lower()

    #Author: Branavan Keethabaskaran
    #Date: Jan 14, 2021
    #Purpose: perfroms a linear search on the list given a value *compares WEIGHT of domino
    #Parameters: value, the domino being searched for
    #Return: location of value
    def linearSearch(self, value):
        counter = 0
        keyDomino = Domino()
        keyDomino.setValue(value)
        
        while counter < self.size and keyDomino != self.list[counter]:
            counter += 1

        if counter == self.size and self.list[counter - 1]!= keyDomino:
            return -1
        else:
            return counter
        
    #Author: Branavan Keethabaskaran
    #Date: Jan 14, 2021 
    #Purpose: performs a sentinel search on the list given a value *compares WEIGHT of domino
    #Parameters: value, the domino being searched for
    #Return: location of the value
    def sentinelSearch(self, value):
        keyDomino = Domino()
        keyDomino.setValue(value)
        self.list.append(keyDomino)
        self.size += 1
        counter = 0

        while keyDomino != self.list[counter]:
            counter += 1

        if (counter + 1) == self.size:
            result = -1
        else:
            result = counter
            
        del self.list[self.size - 1]
        self.size -= 1
        
        return result
        
        
    #Author: Branavan Keethabaskaran
    #Date: Jan 14, 2021
    #Purpose: performs a binary search on the list given a value *compares WEIGHT of domino
    #Parameters: value, the domino being searched for
    #Return: location of the value
    def binarySearch(self, value):
        lower = 0
        upper = self.size - 1
        middle = (lower + upper) // 2
        domino = Domino()
        domino.setValue(value)

        while lower <= upper and self.list[middle] != domino:
            print(lower)
            print(upper)
            print(middle)
            if domino > self.list[middle]:
                lower = middle + 1
            else:
                upper = middle - 1
                
            middle = (lower + upper) // 2
            


        if lower > upper:
            return -1
        else:
            return middle
        
    #Author: Branavan Keethabaskaran
    #Date: Jan 14, 2021
    #Purpose: performs a bubble sort on the list *compares WEIGHT of domino
    #Parameters: none
    #Return: none
    def exchangeSort(self):
        notSorted = True
        listLength = self.size - 1
        
        while listLength >= 0 and notSorted == True:
            notSorted = False
            for i in range(0, listLength):
                if self.list[i] > self.list[i + 1]:
                    temp = self.list[i]
                    self.list[i] = self.list[i + 1]
                    self.list[i + 1] = temp
                    notSorted = True

            listLength -= 1
            
    #Author: Branavan Keethabaskaran
    #Date: Jan 15, 2021
    #Purpose: performs a selection sort on the list *compares VALUE of domino
    #Parameters: none
    #Return: none
 
    ########## For some reason my selection sort does not work properly when comparing weight, which is why this sort compares the values ############
    def selectionSort(self):
        listLength = self.size - 1
#        largestDomino = Domino()
#        largestDomino.setValue(0)
        largestDomino = 0
        largestIndex = 0
        
        while listLength > 0:
            for i in range(0, listLength + 1):
                if self.list[i].value > largestDomino:
                    largestDomino = self.list[i].value
                    largestIndex = i
     
            temp = self.list[listLength].value
            self.list[listLength].value = largestDomino
            self.list[largestIndex].value = temp
            largestDomino = 0
            listLength -= 1
            
    #Author: Branavan Keethabaskaran
    #Date: Jan 14, 2021
    #Purpose: performs a insertion sort on the list *compares WEIGHT of domino
    #Parameters: none
    #Return: none
    def insertionSort(self):
        listLength = 0
        lengthCounter = 0
        currentTempIndex = 0
        for i in range(1, self.size):
            temp = self.list[i]
            lengthCounter = listLength
            currentTempIndex = i
            while lengthCounter >= 0:
                if temp < self.list[lengthCounter]:
                    self.list[lengthCounter + 1] = self.list[lengthCounter]
                    currentTempIndex = lengthCounter
                lengthCounter -= 1

            self.list[currentTempIndex] = temp
            listLength += 1
                    
    
        
########### MAIN PROGRAM ##########
begin = input("Enter 'y' to begin: ")
begin = begin.strip()
begin = begin.lower()

while begin == "y":
    dominoSize = int(input("Enter the size of your domino list: "))
    dominoList = DominoGroup(size = dominoSize)
    print(dominoList)

    userSort = input("Enter 'y' to sort your domino list. Press 'Enter' to skip: ")
    userSort = userSort.strip()
    userSort = userSort.lower()

    if userSort == "y":
        rnd = random.randint(1, 3)

        if rnd == 1:
            dominoList.exchangeSort()
            print(dominoList)
            print("Sort used: Bubble Sort")

        elif rnd == 2:
            dominoList.selectionSort()
            print(dominoList)
            print("Sort used: Selection Sort")

        else:
            dominoList.insertionSort()
            print(dominoList)
            print("Sort used: Insertion Sort")

    search = input("Enter an integer you'd like to search for in the list: ")

    rndNum = random.randint(1, 3)

    if rndNum == 1:
        value = dominoList.linearSearch(search)
        print("Location of " + str(search) + " : " + str(value))
        print("Search used: Linear")

    elif rndNum == 2:
        value = dominoList.sentinelSearch(search)
        print("Location of " + str(search) + " : " + str(value))
        print("Search used: Sentinel")
    else:
        if userSort == "y":
            value = dominoList.binarySearch(search)
            print("Location of " + str(search) + " : " + str(value))
            print("Search used: Binary")

        else:
            print("Error: list not sorted for binary search")
    
    

    
    begin = input("Enter 'y' to begin: ")
    begin = begin.strip()
    begin = begin.lower()

            

