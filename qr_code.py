import qrcode as qr                                         #importing qrcode module

img = qr.make("https://github.com/Dipanshu-Chhanikar")      #specifying the url for qr code

img.save("github_profile.png")                              #saving the qr code in image format

