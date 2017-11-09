# Image Steganographer
##### Hide secret messages inside images

### **Description**
This script is a simple Python3 script that is able to encode **_TEXT_** messages into images. It can be used straight from the command line and has simple to use commands.

### **Disclaimer**
This script was developed for use in a school project and with academic uses in mind. Please use at your own discretion. I am now liable for loss or damage to any image or message.

### **Dependencies**
The *[Pillow](https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/)* module needs to be installed for this script to work. You can install the module right from command line using:
```
pip install Pillow
``` 

## **Development Environment**
The script was developed using Python3.6

## **Features**
- Is able to hide text messages inside images
- Is able to extract hidden messages from images
- Basic error checking to see if images are valid
The *decode* function assumes the message was hidden using this script as well, and will not work otherwise.
Basically the encode is proprietary for the decode to work

### **Usage**
##### Getting Started
To see a list of all options, use the help command:
```
python iStego.py --help
```

##### Putting text inside an image (*Encoding*)
The following sample command hides a message inside an image:
```
python iStego.py encode --image="path/to/image.png" --output="where/to/save/new/image.png" --message="What text I want to hide"
```

##### Getting a message out of an image (*Decoding*)
The following sample command extracts a message from an image:
```
python iStego.py decode --image="path/to/image.png" --output="text/file/to/save/output.txt" *--verbose*
```
**Tip:** You can use the `--verbose` parameter at the end to debug the progress of any encode or decode process

**Note:**
Due to the way certain image types are handled, the steganography seems to work best with PNG files (as it does not compress the image) however, it **does not** work on JPG, JPEG, BMP files (since they compress an image after it is saved)

### **Bugs**
There will probably be lots of bugs with a program like this, feel free to make an *issue request* if you do find a bug and I will try to see if it is fixable or not


This document was last updated: November 9, 2017

-R.N.