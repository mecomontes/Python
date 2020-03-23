#pip3 install qrcode
#pip3 install qrcode[pil]

import qrcode

qr = qrcode.QRCode(version=1
                   , error_correction=qrcode.constants.ERROR_CORRECT_L
                   , box_size=8
                   ,border=4
                   ,)

vCard = '''BEGIN:VCARD
VERSION:4.0
N:Linux;;;Ing.;
FN:Inge Linux
ORG:Producciones De un dia para otro
TITLE:CEO
PHOTO;MEDIATYPE=image/png:https://1.gravatar.com/avatar/71a17ea074849f8996007beec643b057?s=400&d=mm
TEL;TYPE=work,voice;VALUE=uri:tel:+1-234-567-8901
TEL;TYPE=home,voice;VALUE=uri:tel:+1-234-567-8910
ADR;TYPE=WORK;PREF=1;LABEL="100 Waters Edge\nBaytown\, LA 30314\nUnited States of America":;;100 Waters Edge;Baytown;LA;30314;United States of America
ADR;TYPE=HOME;LABEL="42 Plantation St.\nBaytown\, LA 30314\nUnited States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America
EMAIL:info.geex@gmail.com
REV:20080424T195243Z
x-qq:21588891
END:VCARD'''

qr.add_data(vCard)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
#image.save('qr_code.png')
#image.save('qr_code.bmp')
#image.save('qr_code.jpeg')
print("Imagen QR grabada")