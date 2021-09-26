# QRcode_using_python

Let's learn how to create our own QR code using python.

This program I'm going to use numpy and qrcode modules.

Before that let's see what actually is a QR-code.

A Quick Response code(Q-R code) is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity.
The code consists of black modules arranged in a square pattern on a white background.
The information encoded can be made up of any kind of data (e.g., binary, alphanumeric,etc...)

Required instructions for installing the modules!

For QRcode module:

    pip install qrcode[pil]

For numpy module:

    pip install numpy
    
Here 'pil' is included because in order to make the qrcode module work we need another module called pillow.
Hence [pil] is included to make concurrent downloads with single command.

    Output:
    Enter data for the barcode: ***********************
    Dimensions of the QR code: (33, 33)
   ![Screenshot 2021-09-26 225947](https://user-images.githubusercontent.com/71930013/134817877-7ed1532b-ad4b-44d0-a264-3bad35241415.png)

Scan the QRcode to check out what's inside it!
