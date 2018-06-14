"""
This script will split the sample into positive sample and negative sample. Firstly, I will train
program to recognize 'A'.
"""

import os
import cv2

def createPos(org, dst,posInfo):
    image = cv2.imread(org)
    image = cv2.resize(image,(20,20))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    try:
        (cnts, _) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    except:
        (_, cnts, _) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    if len(cnts) <= 1:
        return False
    # print(thresh)

    cv2.imwrite(dst,thresh)
    posInfo.write("./{}  1 0 0 20 20\n".format(dst))
    return True


if __name__ == '__main__':

    allFile = os.listdir("sampleData/")
    if not os.path.exists('pos'):
        os.makedirs('pos')

    posInfo = open("posdata.dat", 'w')

    count = 0
    for item in allFile:
        if item[0] == 'A':
            org = "sampleData/" + item
            dst = "pos/" + item
            dst = dst.split('.')[0] + ".jpg"
            result = createPos(org,dst,posInfo)
            if result:
                count += 1


    print("We totally have {} positive samples".format(count))

            # print(dst)
            # os.rename(org, dst)