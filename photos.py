import os
import sys


PHOTOS_FOLDER_LOCATION = ''
HTML_TEMPLATE_FILE = 'template.html'
HTML_OUTPUT = 'output.html'

def validimgextensions(filename):
    accepted = False
    if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.jpeg') or filename.endswith('.JPEG') or filename.endswith('.png') or filename.endswith('.PNG') or filename.endswith('.bmp') or filename.endswith('.BMP'):
        accepted = True
    return accepted

def parse_template(slides, carousel):
    f=open(HTML_TEMPLATE_FILE, "r")
    if f.mode == 'r':
        html =f.read()
        html = html.replace("%slides%", slides)
        htmldone = html.replace("%carousel%", carousel)
        try:
            file = open(HTML_OUTPUT,"w")
            file.write(htmldone)
            file.close()
        except ValueError as e :
            print ("Error msg: ", e)


# ---------------------------- Main program --------------------------- #

s1 = s2 = ''
i = 0

while True:
    try:
        photopath = input("Enter full path of photos: ")
        for f_name in os.listdir(photopath):
            if validimgextensions(f_name):
                if(s1==""):
                    s1 = '<li data-target="#myCarousel" data-slide-to="'+str(i)+'" class="active">'
                else:
                    s1 += '<li data-target="#myCarousel" data-slide-to="'+str(i)+'"></li>'
                if(s2==""):
                    s2 = '<div class="item active"><img src="'+PHOTOS_FOLDER_LOCATION+f_name+'" style="width:100%;"></div>'
                else:
                    s2 += '<div class="item"><img src="'+PHOTOS_FOLDER_LOCATION+f_name+'" style="width:100%;"></div>'
                print(f_name)
                i += 1
        parse_template(s1, s2)
        s1 = s2 = ''
        i = 0
        print(f"HTML file generated with photos carousel in: {HTML_OUTPUT}\n")
    except ValueError:
        print("Oops!  That was no valid path.")

