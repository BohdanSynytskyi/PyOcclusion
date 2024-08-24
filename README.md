# PyOcclusion
![PyPI](https://img.shields.io/pypi/v/PyOcclusion)
![License](https://img.shields.io/github/license/BohdanSynytskyi/PyOcclusion)
[![Downloads](https://static.pepy.tech/badge/pyocclusion)](https://pepy.tech/project/pyocclusion)

PyOcclusion is a Python package for adding noise of occlusionary type to video files. There is a broad range of parameters for altering in order to achieve the desirded occlusion density, coverage percent, etc. The process is automated and requires no additional prescribing.

Here is an example of what can be done with PyOcclusion:

![Description of the image](grid_image.png)

# Statement Of Need

While most of the software tends to reduce noise in the file, there are many cases when people need to add noise in order to test the new visual model, recognition software, etc. However, most of software tends to generate Gaussian noise, Salt-and-Pepper Noise and so on. PyOcclusion gives an opportunity to overlay an occlusion on both image and video files. There is a broad variety of parameters for customizing occlusionary noise to achieve desired result. 

# Installation

PyOcclusion can be installed from PyPI:

```pip install PyOcclusion```

Once installed, package can be loaded as:

```import PyOcclusion```

# Example

``` 
import PyOcclusion

# instantiate new editor

editor = PyOcclusion.VideoEditor(velocity_r=20, velocity_c=0, side_h=17, side_w=17, num=500, height=1080, width=1920)

# generate new video
editor.editVideo('video.mp4', "newVideo.mp4")
```

# Documentation

General:

[Usage Examples](PyOcclusion-Package/examples/Example1.ipynb)

# Citation

The package can be cited as follows:

```
@software{Synytskyi_PyOcclusion_2024,
  author = {Synytskyi, Bohdan and Livingstone, Steven R},
  month = {08},
  title = {{PyOcclusion}},
  url = {https://github.com/BohdanSynytskyi/PyOcclusion},
  version = {1.0.0},
  year = {2024},
}
```