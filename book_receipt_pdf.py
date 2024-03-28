import random
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime


async def date_data():
    current_date = datetime.datetime.now()
    day_month_year_format = current_date.strftime("%d/%m/%y")
    due_date = current_date + datetime.timedelta(days=10)
    due_date_format = due_date.strftime("%d/%m/%y")
    return day_month_year_format, due_date_format


async def book_issue_receipt(Student_name, enrollment, book_name, writer):
    result = await date_data()
    issue_date = result[0]
    due_date = result[1]
    canvas1 = canvas.Canvas(f"{enrollment}.pdf", pagesize=(700, 600))

    image_path = "University_logo.jpg"
    image = ImageReader(image_path)

    canvas1.drawImage(image, 260, 430, 200, 200)

    canvas1.line(260, 455, 450, 455)
    canvas1.setFont("Times-Bold", 32)
    canvas1.drawString(230, 420, "Book issue receipt")
    canvas1.line(235, 400, 480, 400)

    canvas1.setFont("Times-Bold", 24)
    canvas1.drawString(150, 350, "Student Name:-")
    canvas1.drawString(150, 300, "Enrollment:-")
    canvas1.drawString(150, 250, "Book name:-")
    canvas1.drawString(150, 200, "Writer:-")
    canvas1.drawString(150, 150, "Issue Date:-")
    canvas1.drawString(150, 100, "Due Date:-")

    canvas1.setFont("Times-Bold", 20)
    canvas1.drawString(360, 350, str(Student_name))
    canvas1.drawString(360, 300, str(enrollment))
    canvas1.drawString(360, 250, str(book_name))
    canvas1.drawString(360, 200, str(writer))
    canvas1.drawString(360, 150, str(issue_date))
    canvas1.drawString(360, 100, str(due_date))

    canvas1.setFillColorRGB(0, 1, 0)  # RGB values for green
    canvas1.drawString(310, 65, "The book has been issued successfully.")
    canvas1.setFillColorRGB(0, 0, 0)  # RGB values for green

    canvas1.drawString(505, 30, "Thank You......")

    canvas1.save()
    content_disposition = f'attachment; filename="{enrollment}"'
    return FileResponse(f"{enrollment}.pdf",
                        headers={"Content-Disposition": content_disposition})


if __name__ == '__main__':
    pass
