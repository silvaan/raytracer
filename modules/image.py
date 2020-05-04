import numpy as np

class Image:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pixels = np.zeros((height, width, 3))

  def set_pixel(self, x, y, color):
    self.pixels[y, x] = color