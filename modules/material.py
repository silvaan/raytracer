class Material:
  def __init__(self, color, ambient=0.05, diffuse=1.0, specular=1.0):
    self.color = color
    self.ambient = ambient
    self.diffuse = diffuse
    self.specular = specular