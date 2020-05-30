import matplotlib.pyplot as plt
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\abrig\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageFilter
import os
import time
import imutils
import cv2


# test_8_2 = r'images\8.2_test.png'
#
# img = Image.open(test_8_2)
# print("img:\t" + str(img))
# txt = tess.image_to_string(img)
# print("\n\tExtracted string:\t{" + str(txt) + "}\n")

###
#
# Sample data
#
###

# card 01 - ganigumo
# card 02 - zone eater
# card 03 - air marmot of nefariousness
# card 04 - penguin soldier
# card 05 - mountain

# Basically none of these pictures work.
# Need to shrink the picture size to that of only the name,
# this will make processing faster. Need to isolate the name
# in the image to have less noise for the program to parse
# through.

horizontal_test_cards_1 = [
    "card_01_horizontal_01",
    "card_01_horizontal_02",
    "card_02_horizontal_01",
    "card_02_horizontal_02",
    "card_03_horizontal_01",
    "card_03_horizontal_02",
    "card_04_horizontal_01",
    "card_04_horizontal_02",
    "card_05_horizontal_01",
    "card_05_horizontal_02"
]

vertical_test_cards_1 = [
    "card_01_vertical_01",
    "card_01_vertical_02",
    "card_02_vertical_01",
    "card_02_vertical_02",
    "card_03_vertical_01",
    "card_03_vertical_02",
    "card_04_vertical_01",
    "card_04_vertical_02",
    "card_05_vertical_01",
    "card_05_vertical_02"
]

horizontal_test_deck_1 = [
    "deck_horizontal_01",
    "deck_horizontal_02",
    "deck_horizontal_03",
    "deck_horizontal_04"
]
vertical_test_deck_1 = [
    "deck_vertical_01",
    "deck_vertical_02",
    "deck_vertical_03",
    "deck_vertical_04"
]

test_cards_2 = [
    "card_01_name_01",
    "card_01_name_02",
    "card_02_name_01",
    "card_02_name_02",
    "card_03_name_01",
    "card_03_name_02",
    "card_04_name_01",
    "card_04_name_02",
    "card_05_name_01",
    "card_05_name_02",
    "handwriting_test_01",
    "card_01_name_02_cropped",
    "test_img"
]

cropped_cards = [
    "card_01_name_02_cropped"
]

small_test_set = horizontal_test_cards_1 + vertical_test_cards_1 + test_cards_2 + cropped_cards
    # [
    # "card_01_name_02_cropped"
# ]

def show_image(image_in):
    print("type: " + str(type(image_in)))
    im = None
    if type(image_in) is str:
        path = os.path.join('test_images', image_in + ".jpg")
        im = Image.open(path)

        image_in = cv2.imread(path)

    frame = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    cv2.imshow("frame", frame)
    print("type image_in: " + str(type(image_in)))
    print("type im      : " + str(type(im)))
    # Image.fromarray(image_in).show()
    # im.show()
    time.sleep(1)
    plt.imshow(image_in)
    plt.show()

# def isolate(image_in, color):


def get_text(image_file):
    path = os.path.join('test_images', image_file + ".jpg")
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (0, 0), fx=2, fy=2)

    config = ("--psm 12")

    data = tess.image_to_string(img, lang='eng', config=config)
    # img1 = Image.fromarray(img, 'RGB')
    # img1.show()
    # Image.new("RGB", )
    return data.strip().split("\n")

def extract_2():
    extracted = {}

    all_to_test = small_test_set

    modes = ["1", "L", "P", "RGB", "RGBA", "I"]
    output_file = open("all_to_test_output_2.txt", "w+")

    for i in range(len(all_to_test)):
        # if i == 0:
        if True:
            for mode in modes:
                file_name = all_to_test[i]
                name = file_name + "_" + mode
                # path = os.path.join('test_images', file_name + ".jpg")
                # img = Image.open(path).filter(ImageFilter.SHARPEN)
                # new_img = img.convert(mode)

                text_list = get_text(file_name)
                extracted[name] = text_list
                print("finished: " + str(name))

    longest = None
    shortest = None
    for file_name, text in extracted.items():
        l = len(text)
        if not longest or l > longest:
            longest = l
        if (not shortest or l < shortest) and (l):
            shortest = l
        line = "file (" + str(l) + "): (" + str(file_name) + "):\ttext:\t(" + str(text) + ")"
        output_file.write(line + "\n")
        # print(line)

    output_file.close()
    print("longest: " + str(longest))
    print("shortest: " + str(shortest))

    return extracted

def extract():
    extracted = {}

    all_to_test = small_test_set

    modes = ["1", "L", "P", "RGB", "RGBA", "I"]
    output_file = open("all_to_test_output.txt", "w+")

    for i in range(len(all_to_test)):
        # if i == 0:
        if True:
            for mode in modes:
                file_name = all_to_test[i]
                name = file_name + "_" + mode
                path = os.path.join('test_images', file_name + ".jpg")
                img = Image.open(path).filter(ImageFilter.SHARPEN)
                print("t: " + str(type(img)))
                new_img = img.convert(mode)
                new_path = os.path.join('output_images', name)
                print(img)
                if not os.path.exists(new_path):
                    new_img.save(new_path + ".png")
                    # show_image(new_img)
                    # new_img.show()

                text = tess.image_to_string(new_img)
                extracted[name] = text.strip().split("\n")


    longest = None
    shortest = None
    for file_name, text in extracted.items():
        l = len(text)
        if not longest or l > longest:
            longest = l
        if (not shortest or l < shortest) and (l):
            shortest = l
        line = "file (" + str(l) + "): (" + str(file_name) + "):\ttext:\t(" + str(text) + ")"
        output_file.write(line + "\n")
        # print(line)

    output_file.close()
    print("longest: " + str(longest))
    print("shortest: " + str(shortest))

    return extracted


# print("extracted: " + str(get_text(small_test_set[0])))

# print(extract_2())
show_image(test_cards_2[0])
# extract()
# img = Image.new('RGB', (60, 30), color = 'red')
# img.save('pil_red.png')
