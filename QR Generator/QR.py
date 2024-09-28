import qrcode # type: ignore
from PIL import Image # type: ignore

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4,)
qr.add_data(input("Enter Your URL: "))
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")
