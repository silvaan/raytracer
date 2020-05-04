class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = direction.normalize()

  def point(self, dist):
    return self.origin + dist*self.direction