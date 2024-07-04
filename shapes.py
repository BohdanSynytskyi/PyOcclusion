from skimage import color, draw
import numpy as np


class Square:
    def __init__(self):
        pass

    def __init__(self, r, c, height, width, velr, velc, sizer, sizec, color):
        self.r = r
        self.c = c
        self.frameHeight = height
        self.frameWidth = width
        self.sizec = sizec
        self.sizer = sizer
        self.velr = velr
        self.velc = velc
        self.num_pixels = 0
        self.color = color

    def move(self):
        self.r += self.velr
        self.c += self.velc

    def draw(self, frame):
        rr, cc = draw.rectangle((self.r, self.c), extent=(self.sizer, self.sizec))

        rr = rr % self.frameHeight
        cc = cc % self.frameWidth

        frame[rr, cc, 0] = color[0]
        frame[rr, cc, 1] = color[1]
        frame[rr, cc, 2] = color[2]

        return frame

    def getPixelCoordinates(self):
        rr, cc = draw.rectangle((self.r, self.c), extent=(self.sizer, self.sizec))

        rr = rr % self.frameHeight
        cc = cc % self.frameWidth

        return rr, cc


class Drop:
    def __init__(self):
        pass

    def __init__(self, r, c, height, width, velr, velc, sizer, radius):
        self.r = r
        self.c = c
        self.frameHeight = height
        self.frameWidth = width
        self.radius = radius
        self.sizer = sizer
        self.velr = velr
        self.velc = velc
        self.num_pixels = 0

    def move(self):
        self.r += self.velr
        self.c += self.velc

    def generateVerticies(self, r_start, c_start, r_end, radius):
        rows = []
        rows.append(r_start)
        columns = []
        columns.append(c_start)
        for i in range(-1 * radius, radius + 1, 1):
            column = c_start + i
            row = r_end + np.sqrt(radius ** 2 - i ** 2)
            rows.append(row)
            columns.append(column)

        rows.append(r_start)
        columns.append(c_start)
        return rows, columns

    def draw(self, frame):
        rows, columns = self.generateVerticies(self.r, self.c, self.r + self.sizer, self.radius)

        rr, cc = draw.polygon(rows, columns)

        rr = rr % self.frameHeight
        cc = cc % self.frameWidth

        image_shape = (self.frameHeight, self.frameWidth)
        img = np.zeros(image_shape)
        img[rr, cc] = 1
        self.num_pixels = np.sum(img)
        frame[rr, cc, 0] = 123
        frame[rr, cc, 1] = 142
        frame[rr, cc, 2] = 173
        frame[rr, cc, 3] = 250
        return frame

    def getPixelCoordinates(self):
        rows, columns = self.generateVerticies(self.r, self.c, self.r + self.sizer, self.radius)

        rr, cc = draw.polygon(rows, columns)

        rr = rr % self.frameHeight
        cc = cc % self.frameWidth
        return rr, cc
