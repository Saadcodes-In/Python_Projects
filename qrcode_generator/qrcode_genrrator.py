# importing Qrcode module
import qrcode
# Asking for Url
data = input("Enter your URL or text: ")
# file should be jpg or png
filename = input("Enter your file name: ")
# Giving size of qr
qr = qrcode.QRCode(box_size=25,border=8)
qr.add_data(data)
# Adding colour
image = qr.make_image(fillcolor="black",back_color= "white")
# Saving Qr code
image.save(filename)
print(f"QR code saved as {filename}")