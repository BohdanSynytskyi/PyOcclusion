from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-image',
        'imageio',
        'av',
    ],
    author='Bohdan Synytskyi',
    author_email='bodiasynytskiy@gmail.com',
    description='A package for video editing with occlusion type of noise',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BohdanSynytskyi/PyOcclusion',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
