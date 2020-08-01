from PIL import Image , ImageDraw

import qrcode

Data = "roboadda.com"
image = qrcode.make(Data)
image.save("roboaddaqrcode.png")

