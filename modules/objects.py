import numpy as np

class Plane:
  def __init__(self, origin, normal, material):
    self.origin = origin
    self.normal = normal.normalize()
    self.material = material

  def intersects(self, ray):
    denom = ray.direction * self.normal
    if denom > 1e-6:
      v = (self.origin - ray.origin) * self.normal
      dist = v / denom
      if dist > 0:
        return dist
    return None

  def normal_at(self, surf_point):
    return self.normal

class Sphere:
  def __init__(self, origin, radius, material):
    self.origin = origin
    self.radius = radius
    self.material = material
      
  def intersects(self, ray):
    sphere_to_ray = ray.origin - self.origin
    b = 2 * (ray.direction * sphere_to_ray)
    c = sphere_to_ray * sphere_to_ray - self.radius * self.radius
    discriminant = b**2 - 4 * c

    if discriminant >= 0:
      dist = (-b - np.sqrt(discriminant)) / 2
      if dist > 0:
        return dist
    return None

  def normal_at(self, surf_point):
    return (surf_point - self.origin).normalize()