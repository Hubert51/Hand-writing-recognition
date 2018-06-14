import cv2
from PIL import Image
from PIL import ImageGrab
import os
import numpy as np

class CreateSample(object):
    def __init__(self , fileName):
        self.column = 0
        self.row = 0
        self.capitalLetter = 65
        self.Letter = 97
        self.image = cv2.imread(fileName)
        self.height = 120
        self.width = 110
        self.x = 0
        self.y = 0

    def cropInRow(self):
        pass


    def cropImage(self, fileName):
        x = self.x
        y = self.y
        h = self.height
        w = self.width
        letter = 65
        const = 1

        for row in range(6):
            if row == 3:
                y += 24
                letter = 97
                const = 2
            if (row + 1) % 3 != 0:
                column = 9
            else:
                column = 8
            for col in range(column):
                crop = self.image[y:y+h, x:x+w]
                x1,y1,w1,h1 = self.removeWhite(crop)
                crop = crop[y1:y1+h1, x1:x1+w1]
                if chr(letter) == 'v':
                    print(0)

                cv2.imwrite("sampleData/{}{}".format(chr(letter)*const,fileName), crop)
                print(chr(letter), fileName )

                x += w
                letter += 1
            x = 0
            y += h
    def removeWhite(self,crop):
        height, width, _ = crop.shape
        startHeight = 0
        # print(height)
        # print(width)

        # print(crop.shape)


        x,y,w,h = 0,0,width,height
        defaultY = 0
        blankLine = 0
        continueTime = 0
        for i in range(height):
            pixel = 0
            continueFlag = False
            for j in range(width):
                pixel += crop
                if y == defaultY and np.array_equal(crop[i][j] , [0,0,0]):
                    y = i
                    startHeight = y

                    # cv2.circle(crop, (j,i), 10, [0, 0, 0])
                    # cv2.imshow("crop",crop)
                    # cv2.waitKey(0)
                if  np.array_equal( crop[i][j] , [0,0,0]) :
                    # print("true, i:{}, j:{}, y:{}".format(i,j, y) )
                    continueFlag = True
                    continueTime = 0
                    blankLine = 0

            if continueFlag == False:
                continueTime+=1

            if continueFlag == False and i < 0.5*height:
                blankLine += 1
                if blankLine > 15:
                    y = defaultY = i
                    blankLine = 0

            if continueFlag == False and continueTime >=4 and y != 0 and i > 0.7*height:
                h = i - y -4
                break
        i = 0
        j = 0

        continueTime = 0
        for i in range(width):
            continueFlag = False
            for j in range(startHeight,height):
                if x == 0 and np.array_equal(crop[j][i] , [0,0,0]):
                    # cv2.circle(crop, (i,j), 10, [0, 0, 0])
                    # cv2.imshow("crop",crop)
                    # cv2.waitKey(0)
                    x = i
                if  np.array_equal( crop[j][i] , [0,0,0]) :
                    # print("true, i:{}, j:{}, y:{}".format(i,j, y) )
                    continueFlag = True
                    continueTime = 0
            if continueFlag == False:
                continueTime += 1
            if continueTime >= 4 and x != 0:
                w = i - x-4
                break
        print(x,y,w,h)
        return (x,y,w,h)



        # remove horziton white line





if __name__ == '__main__':
    print(ord('A'))

    # print(os.listdir("rawLetterData/"))
    allFile = os.listdir("rawLetterData/")
    allFile.sort()
    print(allFile)
    allFile.remove(".DS_Store")

    for name in allFile:

        fileName = "rawLetterData/{:s}".format(name)
        sample = CreateSample(fileName)
        sample.cropImage(name)

        print("complete " + name)

        # image = cv2.imread(fileName)
        #
        # createSample(fileName,image)
        #
        #
        #
        # roi = image[0:120,0:110]
        # cv2.imshow("image", roi)
        # cv2.imwrite("A.png",roi)
        # cv2.waitKey(0)



        # image = image[:,:,:3]

        # print(image)

        # image =cv2.cvtColor(image,cv2.COLOR_BGRA2BGR)

        # image = cv2.imread("/Users/gengruijie/Desktop/WechatIMG288.jpeg")
        #
        # res = image
        # # convert image to grayscale
        # gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        # # blur the image slightly to remove noise.
        # gray = cv2.bilateralFilter(gray, 11, 17, 17)
        # # gray = cv2.GaussianBlur(gray, (5, 5), 0)  # is an alternative way to blur the image
        # # canny edge detection
        # edged = cv2.Canny(gray, 200, 200)
        #
        #
        # # two threshold method.
        # # The first one is normal threshold method
        # # The second one is use Gaussian method which has better effect.
        # ret,thresh1 = cv2.threshold(gray,150,150,cv2.THRESH_BINARY)
        # # thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        # try:
        #     (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # except:
        #     (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #
        # cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
        # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # cv2.imshow("image", image)
        # cv2.waitKey(0)



    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
