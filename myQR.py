
import qrcode
import numpy as np

data = input('Enter data for the barcode: ')

qr = qrcode.QRCode(version=1, box_size=10, border=4)

qr.add_data(data)

qr.make()

print("Dimensions of the QR code:", np.array(qr.get_matrix()).shape)

img = qr.make_image(fill_color="white", back_color="black")

img.save("site_inversed.png")

img.show("site_inversed.png")
