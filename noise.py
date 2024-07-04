import numpy as np

class Noise:
    def __init__(self, height, width, velr, velc):
        self.img = np.zeros((height, width))
        self.rr = np.array([], dtype=int)
        self.cc = np.array([], dtype=int)
        self.velr = velr
        self.velc = velc

    def move(self):
        if len(self.rr) > 0:
            self.rr = (self.rr + self.velr) % self.img.shape[0]
            self.cc = (self.cc + self.velc) % self.img.shape[1]

    def append(self, squares):
        for square in squares:
            sq_rr, sq_cc = square.getPixelCoordinates()
            sq_rr = sq_rr.astype(int)
            sq_cc = sq_cc.astype(int)
            self.img[sq_rr, sq_cc] = 1

        rr_list = []
        cc_list = []

        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if self.img[i, j] == 1:
                    rr_list.append(i)
                    cc_list.append(j)

        self.rr = np.array(rr_list, dtype=int)
        self.cc = np.array(cc_list, dtype=int)

    def draw(self, frame):

        frame[self.rr, self.cc, 0] = 123
        frame[self.rr, self.cc, 1] = 142
        frame[self.rr, self.cc, 2] = 173

        return frame