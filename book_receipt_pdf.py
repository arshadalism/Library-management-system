from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


async def book_issue_receipt():
    canvas1 = canvas.Canvas("book_output.pdf", pagesize=(700, 600))

    image_path = "University_logo.jpg"
    image = ImageReader(image_path)

    canvas1.drawImage(image, 260, 430, 200, 200)

    canvas1.line(260, 450, 450, 450)
    canvas1.setFont("Times-Bold", 32)
    canvas1.drawString(250, 420, "Book issue receipt")
    canvas1.line(260, 400, 450, 400)

    canvas1.setFont("Times-Bold", 24)
    canvas1.drawString(90, 350, "Student Name:-")
    canvas1.drawString(90, 300, "Enrollment:-")
    canvas1.drawString(90, 250, "Book name:-")
    canvas1.drawString(90, 200, "Writer:-")
    canvas1.drawString(90, 150, "Issue Date:-")
    canvas1.drawString(90, 100, "Due Date:-")

    canvas1.setFillColorRGB(0, 1, 0)  # RGB values for green
    canvas1.drawString(270, 65, "The book has been issued successfully.")
    canvas1.setFillColorRGB(0, 0, 0)  # RGB values for green

    canvas1.drawString(505, 30, "Thank You......")

    canvas1.save()

if __name__ == '__main__':
    pass