import qrcode
import qrcode.image.pil
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/belos/Desktop/бэк/my_qrcode.png")

result = decode(img)

print(result)
