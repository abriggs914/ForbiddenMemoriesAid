from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
from functools import reduce
from collections import Counter
import time
style.use("ggplot")

###
# print("Hello World!")
###

### looking at dot image
# dot_image = Image.open('images/dot.png')
# dot_image_arr = np.asarray(dot_image)
# print(dot_image_arr)
###

### looking at dot_n image
# dot_n_image = Image.open('images/dotndot.png')
# dot_n_image_arr = np.asarray(dot_n_image)
# print(dot_n_image_arr)
###

### plotting dot_n image
# plt.imshow(dot_image_arr)
# plt.imshow(dot_n_image_arr)
# plt.show()
# print(dot_n_image_arr)
###

# converts all pixels of an image array to
# it's black and white underlying colours using
# average colour calculations.
# def threshold(imageArray):
#
#     balanceAr = []
#     newAr = imageArray
#     for eachRow in imageArray:
#         for eachPix in eachRow:
#             avgNum = mean(eachPix[:3])
#             balanceAr.append(avgNum)
#
#     balance = mean(balanceAr)
#     for eachRow in newAr:
#         for eachPix in eachRow:
#             if mean(eachPix[:3]) > balance:
#                 eachPix[0] = 255
#                 eachPix[1] = 255
#                 eachPix[2] = 255
#                 eachPix[3] = 255
#             else:
#                 eachPix[0] = 0
#                 eachPix[1] = 0
#                 eachPix[2] = 0
#                 eachPix[3] = 255
#     return newAr
#
# def create_examples():
#     numberArrayExamples = open('numArEx.txt','a')
#     numbersWeHave = range(1,10)
#     for eachNum in numbersWeHave:
#         #print eachNum
#         for furtherNum in numbersWeHave:
#             # you could also literally add it *.1 and have it create
#             # an actual float, but, since in the end we are going
#             # to use it as a string, this way will work.
#             print(str(eachNum)+'.'+str(furtherNum))
#             imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
#             ei = Image.open(imgFilePath)
#             eiar = np.array(ei)
#             eiarl = str(eiar.tolist())
#
#             print(eiarl)
#             lineToWrite = str(eachNum)+'::'+eiarl+'\n'
#             numberArrayExamples.write(lineToWrite)
#
#
# def what_num_is_this(filePath):
#     matchedAr = []
#     loadExamps = open('numArEx.txt', 'r').read()
#     loadExamps = loadExamps.split('\n')
#
#     i = Image.open(filePath)
#     iar = np.array(i)
#     iarl = iar.tolist()
#
#     inQuestion = str(iarl)
#
#     for eachExample in loadExamps:
#         try:
#             splitEx = eachExample.split('::')
#             currentNum = splitEx[0]
#             currentAr = splitEx[1]
#
#             eachPixEx = currentAr.split('],')
#             eachPixInQ = inQuestion.split('],')
#
#             x = 0
#
#             while x < len(eachPixEx):
#                 if eachPixEx[x] == eachPixInQ[x]:
#                     matchedAr.append(int(currentNum))
#
#                 x += 1
#         except Exception as e:
#             print(str(e))
#
#     print(matchedAr)
#     x = Counter(matchedAr)
#     print(x)
#     print(x[0])

###
# y_04_image = Image.open('images/numbers/y0.4.png')
# y_04_image_arr = np.asarray(y_04_image)
#
# o_04_image = Image.open('images/numbers/0.4.png')
# o_04_image_arr = np.asarray(o_04_image)
#
# y_05_image = Image.open('images/numbers/y0.5.png')
# y_05_image_arr = np.asarray(y_05_image)
#
# plt.imshow(y_04_image_arr)
# plt.imshow(y_05_image_arr)
# plt.imshow(o_04_image_arr)
#
# print(y_04_image_arr)
# print(y_05_image_arr)
# print(o_04_image_arr)
#
# plt.show()
###

###
# i = Image.open('images/numbers/0.1.png')
# iar = np.array(i)
# i2 = Image.open('images/numbers/y0.4.png')
# iar2 = np.array(i2)
# i3 = Image.open('images/numbers/y0.5.png')
# iar3 = np.array(i3)
# i4 = Image.open('images/sentdex.png')
# iar4 = np.array(i4)
#
# iar = threshold(iar)
# iar2 = threshold(iar2)
# iar3 = threshold(iar3)
# iar4 = threshold(iar4)
#
# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)
#
# ax1.imshow(iar)
# ax2.imshow(iar2)
# ax3.imshow(iar3)
# ax4.imshow(iar4)
#
# plt.show()
#
# create_examples()
# what_num_is_this('images/sentdex.png')
# what_num_is_this('images/dot.png')
# what_num_is_this('images/dotndot.png')
###

###
def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(1, 10)
    for eachNum in numbersWeHave:
        for furtherNum in numbersWeHave:
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(furtherNum) + '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWrite = str(eachNum) + '::' + eiarl + '\n'
            numberArrayExamples.write(lineToWrite)


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachPart in imageArray:
        for theParts in eachPart:
            # for the reduce(lambda x, y: x + y, theParts[:3]) / len(theParts[:3])
            # in Python 3, just use: from statistics import mean
            # then do avgNum = mean(theParts[:3])
            avgNum = reduce(lambda x, y: x + y, theParts[:3]) / len(theParts[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
        except Exception as e:
            print(str(e))

    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]

    print("loadExamps: " + str(loadExamps))
    print("iarl: " + str(iarl))
    print("InQuestion: " + str(inQuestion))
    print("matchedAr: " + str(matchedAr))
    print("graphX: " + str(graphX))
    print("graphY: " + str(graphY))
    print("ylimi: " + str(ylimi))

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()

createExamples()
whatNumIsThis('images/numbers/1.1.png')
# whatNumIsThis('images/8.1_test.png')
# whatNumIsThis('images/8.2_test.png')
# whatNumIsThis('images/8.3_test.png')
###

