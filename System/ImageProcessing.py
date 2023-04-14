import bm4d as bm4d
import cv2
import numpy as np
import skimage
from skimage.util import img_as_float
from PIL import Image

def DenoiseImage(ImagePath):
    image = cv2.imread(ImagePath, 0)
    image_fload = img_as_float(image)
    imagef_bm4d = bm4d.bm4d(image_fload, sigma_psd=0.1)
    image_byte = ((imagef_bm4d - imagef_bm4d.min()) * (1 / (imagef_bm4d.max() - imagef_bm4d.min()) * 255)).astype('uint8')
    #cv2.imshow('bm4d', image_byte)
    return image_byte

def Segment(image_byte):
    image_float = skimage.filters.gaussian(image_byte, sigma=1)
    triangle_tresh = skimage.filters.threshold_triangle(image_float)
    triangle_byte = ((image_float > triangle_tresh) * 255).astype('uint8')
    #cv2.imshow('triangle_byte', triangle_byte)
    return triangle_byte