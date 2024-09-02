# API

The functionality of the package revolvs around 3 files: shapes.py, noise.py, occlusion.py

## ```shapes``` module

```Scikit-image``` library is used to perform image manipulation. There is an abstract parent class ```Shape```, which requires the following parameters: position(```r``` and ```c```), frame resolution(```height```,     ```width```), velocity(```velocity_r```, ```velocuty_c```), and color 

Two functions need to be implemented to create child class:
* getPixelCoordinates(self)
* draw(self, frame)

There are 2 predefined shapes, but, if following structure, another child classes can be created if required.

## ```Noise``` module

There is a ```Noise ```class, which is responsible for containing all shapes to be overlayed on the video file to improve efficiency, requires frame dimensionality, velocity of motion and color to be instantiated. 

## ```Occlusion``` module

```VideoEditor``` is the main class designed for the interaction with the package. It takes velocity, shape's dimensions, number of shapes to be displayed, resolution of the file, noise coefficients, type of shape and color.

### editVideo()

This function produces new video file with overlayed occlusionary noise using ```av``` python library. It's parameters allow customizing video properties such as ```fps```, ```bitrate```, ```codec```. This function also outputs to the console some details about the occlusion, such as pixels covered and coverage percent. 

### editImage()

This function provides an option to manipulate images using ```PIL``` package. 

### showOcclusion()

```showOcclusion()``` allows to preview occlusion parameters to be applied in ```editImage()``` function without creating a new file.

### editAll()

```editAll()``` is meant to edit multiple video files of predefined extension in desired directory and create multiple files at once.