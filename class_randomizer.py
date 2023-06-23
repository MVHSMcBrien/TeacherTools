import random
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

class_names= ["Trevor","Julian","Stryder","Matthew","Dylan","Taylor","Lincoln","Kayden","Jack","Kinohi","Noah","Cressida","Eilam","Brendan"]

def randomizeNames(names):
 randomNamesList=names.copy()
 random.shuffle(randomNamesList)
 return randomNamesList

print(randomizeNames(class_names))
print(class_names)


myclass = ["Bobby","Jimmy","John"]
canvas = Canvas("font-colors.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 12)
canvas.setFillColor(blue)
for i in range(len(myclass)):
    canvas.drawString(1 * inch, (10 * inch)-(10 *i), myclass[i])

canvas.save()