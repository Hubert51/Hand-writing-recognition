"""
This script try to collect data from web about raw training data. The data is different
version of handwriting letter.
"""


import lxml.html
import sys
import urllib.request
import time
import os
from PIL import Image


class GetData(object):
    def __init__(self,url):
        self.url = url
        self.index = 0
        self.pageIndex = 1
        self.rawLetterData = "rawLetterData"


    def getCurrent(self):
        self.webPage = urllib.request.urlopen(self.url)
        print("this is {:d} pages".format(self.pageIndex))
        doc = lxml.html.parse(self.webPage)
        matches = doc.xpath( "//div[@class='fontPreviewImageWrapper']/a") #'//img[@id="imgPage2]')
        print(matches[0])
        # urllib.request.urlretrieve("https://en.wikipedia.org/wiki/Linear_equation#/media/File:Linear_Function_Graph.svg", "local-filename.jpg")

        for element in matches:
            fontURL = element.get("href")
            self.getImage(fontURL)

        self.changeToNextPage()

    def changeToNextPage(self):
        # self.index = 0
        self.pageIndex += 1
        self.url = self.url[0:len(url)-1] + str(self.pageIndex)


    def getImage(self, fontURL):

        fd = urllib.request.urlopen(fontURL)
        doc = lxml.html.parse(fd)
        matches = doc.xpath( "//img[@class='fontPreview']") #'//img[@id="imgPage2]')
        if not os.path.exists(self.rawLetterData):
            os.makedirs(self.rawLetterData)
        if matches:
            imageURL = matches[0].get('src')
            # print(imageURL)
            fileName = self.rawLetterData + "/" + str(self.index) + '.png'
            urllib.request.urlretrieve(imageURL, fileName)
            self.removeAlpha(fileName)
            self.index += 1

    def removeAlpha(self, fileNmae):

        image = Image.open(fileNmae)
        image.convert("RGBA")  # Convert this to RGBA if possible
        # print(image)
        pixel_data = image.load()
        if image.mode == "RGBA":
            # If the image has an alpha channel, convert it to white
            # Otherwise we'll get weird pixels
            for y in range(image.size[1]):  # For each row ...
                for x in range(image.size[0]):  # Iterate through each column ...
                    # Check if it's opaque
                    if pixel_data[x, y][3] < 255:
                        # Replace the pixel data with the colour white
                        pixel_data[x, y] = (255, 255, 255, 255)

        # Resize the image thumbnail
        # image.thumbnail([resolution.width, resolution.height], Image.ANTIALIAS)
        image.save(fileNmae)


if __name__ == '__main__':
    url = "https://fontmeme.com/fonts/handwriting-fonts-collection/1"
    print()

    myData = GetData(url)

    i = 0
    while i < 3:
        myData.getCurrent()
        # time.sleep(10)



    # getImage()
