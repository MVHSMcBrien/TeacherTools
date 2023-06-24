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

if __name__ == '__main__':
   random_names = randomizeNames(class_names)
   createPDF(random_names)