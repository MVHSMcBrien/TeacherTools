# This script will take a list of class names randomize it and create 
# a seating chart with tables

import random
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

# Number of Students in each group
groupsof = 5
# Change this with each class
class_names= ["Trevor","Julian","Stryder","Matthew","Dylan","Taylor","Lincoln","Kayden","Jack","Kinohi","Noah","Cressida","Eilam","Brendan"]

def randomizeNames(names):
    randomNamesList=names.copy()
    random.shuffle(randomNamesList)
    return randomNamesList


def createPDF(names_list):
    canvas = Canvas("randomized-class-list.pdf", pagesize=LETTER)
    canvas.setFont("Times-Roman", 20)
    canvas.drawString(inch, 10*inch, "Randomized Class List")
    canvas.setFont("Times-Roman", 12)
    #canvas.setFillColor(blue)
    for i in range(len(names_list)):
        canvas.drawString(1 * inch, (10 * inch-20)-(12 *i), names_list[i])
    canvas.showPage()
    canvas.save()
    return None

def groups(names):
    if groupsof <= 0:
        raise Exception("Number of Groups must be greater than zero")
    row = []
    groupedclass = []
    for i in range(len(names)):
        row.append(names[i])
        if (i%groupsof == (groupsof-1)):
            groupedclass.append(row)
            row=[]
    if len(row) != 0:
        groupedclass.append(row)
    return groupedclass

def printGroup(studentgroupslist):
    groupnum=1
    for group in studentgroupslist:
            print("GROUP",groupnum,' '.join(group))
            groupnum +=1



if __name__ == '__main__':
    
    printGroup(groups(class_names))
   #random_names = randomizeNames(class_names)
   #createPDF(random_names)