class Color:
  def __init__(self, value=(0, 0, 0)):
    if (isinstance(value, str)):
      self.r = int(value[1:3], 16)
      self.g = int(value[3:5], 16)
      self.b = int(value[5:7], 16)
    else:
      self.r = value[0]
      self.g = value[1]
      self.b = value[2]
    self.r = round(min(255, self.r))
    self.g = round(min(255, self.g))
    self.b = round(min(255, self.b))
    self.value = (self.r, self.g, self.b)

  def __str__(self):
    return f'Color{self.value}'
  
  def __add__(self, other):
    return Color((self.r + other.r, self.g + other.g, self.b + other.b))
  
  def __sub__(self, other):
    return Color((self.r - other.r, self.g - other.g, self.b - other.b))
  
  def __mul__(self, other):
      return Color((self.r*other, self.g*other, self.b*other))
      
  def __rmul__(self, other):
    return self.__mul__(other)
  
  def __truediv__(self, other):
    return Color((self.r/other, self.g/other, self.b/other))

  def to_list(self):
    return list(self.value)