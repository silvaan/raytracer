import numpy as np

class Vector:
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
    self.norm = np.sqrt(self.x**2+self.y**2+self.z**2)
  
  def normalize(self):
    return self / self.norm
  
  def __str__(self):
    return f'Vector({self.x}, {self.y}, {self.z})'
  
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
  
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
  
  def __mul__(self, other):
    if isinstance(other, Vector):
      return self.x*other.x + self.y*other.y + self.z*other.z
    else:
      return Vector(self.x*other, self.y*other, self.z*other)
      
  def __rmul__(self, other):
    return self.__mul__(other)
  
  def __truediv__(self, other):
    return Vector(self.x/other, self.y/other, self.z/other)
  
  def __pow__(self, exp):
    return self*self

  def reflect(self, other):
    other = other.normalize()
    return self - 2 * (self * other) * other
    
Point = Vector