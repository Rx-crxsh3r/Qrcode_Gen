import qrcode
from PIL import Image
import os

# Create the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data("https://www.geeksforgeeks.org/")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Define the path to save the image (example: Desktop)
save_path = os.path.join(os.path.expanduser("~"), "Desktop", "qr2.png")
img.save(save_path)

print(f"QR code saved to {save_path}")
