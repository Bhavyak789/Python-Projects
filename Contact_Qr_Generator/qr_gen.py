import qrcode as qr
from PIL import Image as Img

url = "C://Users//bhavy\Desktop//Py projects//Contact_Qr_Generator//bk_contact.jpg"

qrC = qr.QRCode(
    version=3,  
    error_correction=qr.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,  
)

def createQr(name = "None", mobile = "None", email = "None"):
    qrC.add_data(f"MECARD:N:{name};TEL:{mobile};EMAIL:{mail};;")
    img = qrC.make_image(fill_color="cyan", back_color="black")
    img.save(url)

def open_Img():
    image  = Img.open(url)
    image.show()


print("Welcome to Create Your Contact QR!\nEnter your contact details below :")
name  = input("Name : ")
tel = input("Mobile : ")
mail = input("Email : ")

createQr(name, tel, mail)
open_Img()

