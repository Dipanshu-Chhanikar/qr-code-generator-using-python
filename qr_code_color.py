import qrcode                                                               #importing qrcode module
from PIL import Image                                                       #importing pil module

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H ,
                   box_size = 10 ,
                   border = 4)

qr.add_data("https://github.com/Dipanshu-Chhanikar")                        #specifying the url for qr code
qr.make(fit = True)
img = qr.make_image(fill_color = "blue" , back_color = "white")             #specifying colors for qr code
img.save("github_color_profile.png")                                        #saving the qr code in image format
