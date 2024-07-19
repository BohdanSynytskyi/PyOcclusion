import imageio
import os
import av
import numpy as np
import noise
from shapes import *
import traceback


class VideoEditor:
    def __init__(self, VELOCITY_R, VELOCITY_C, SIDE_H, SIDE_W, NUM,
                 HEIGHT=720, WIDTH=1280, NOISE_ROW=1, NOISE_COL=1, shape='square', COLOR=(0, 0, 0)):

        self.height = HEIGHT
        self.width = WIDTH
        self.vel_r = VELOCITY_R
        self.vel_c = VELOCITY_C
        self.SIDE_H = SIDE_H
        self.SIDE_W = SIDE_W
        self.NUM = NUM
        self.NOISE_ROW = NOISE_ROW
        self.NOISE_COL = NOISE_COL
        self.COLOR = COLOR
        self.shape = shape
        self.shapes = self.placeShapes()

        self.noise = noise.Noise(HEIGHT, WIDTH, VELOCITY_R, VELOCITY_C)
        self.noise.append(self.shapes)

    def placeShapes(self):

        num_on_x = int(np.sqrt(self.width * self.NUM / self.height))
        num_on_y = self.NUM // num_on_x
        col_gap = self.width / num_on_x
        row_gap = self.height / num_on_y

        shapesArr = []
        if self.shape == 'square':
            for col_i in range(num_on_x):
                for row_i in range(num_on_y):
                    shapesArr.append(Square(row_gap * row_i + row_gap / 2 * self.NOISE_ROW * np.random.rand(),
                                            col_gap * col_i + col_gap / 2 * self.NOISE_COL * np.random.rand(),
                                            self.height, self.width, self.vel_r, self.vel_c,
                                            self.SIDE_H, self.SIDE_W, self.COLOR))
        elif self.shape == 'drop':
            for col_i in range(num_on_x):
                for row_i in range(num_on_y):
                    shapesArr.append(Drop(row_gap * row_i + row_gap / 2 * self.NOISE_ROW * np.random.rand(),
                                          col_gap * col_i + col_gap / 2 * self.NOISE_COL * np.random.rand(),
                                          self.height, self.width, self.vel_r, self.vel_c,
                                          self.SIDE_H, self.SIDE_W, self.COLOR))
        print(f"displayed number of shapes: {num_on_x * num_on_y}")

        return shapesArr

    def calculateCoveredPixels(self):
        tempImgArray = np.zeros((self.height, self.width))
        for square in self.shapes:
            rr, cc = square.getPixelCoordinates()
            rr = rr.astype(int)
            cc = cc.astype(int)
            tempImgArray[rr, cc] = 1
        return np.sum(tempImgArray)

    def edit(self, filename, noisyname, fps=30, codec='libx264', bitrate='4000k'):

        global container, writer
        isFirstFrame = True

        try:

            container = av.open(filename)
            stream = container.streams.video[0]
            writer = imageio.get_writer(noisyname, fps=fps, codec=codec, bitrate=bitrate)

            for frame in container.decode(stream):
                imgArray = frame.to_rgb().to_ndarray()

                self.noise.move()
                imgArray = self.noise.draw(imgArray)

                if isFirstFrame:
                    coveredPixels = self.calculateCoveredPixels()
                    print(
                        f"Pixels covered: {coveredPixels}, coverage percent: "
                        f"{coveredPixels / (self.height * self.width) * 100}%")

                isFirstFrame = False
                writer.append_data(imgArray)

        except av.AVError as e:
            print(f"An error occurred with the AV library: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(traceback.format_exc())

        finally:
            container.close()
            writer.close()

    def editAll(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith('.mp4'):
                self.edit(os.path.join(directory, filename), "noisy_" + filename)
