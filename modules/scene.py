from modules.image import Image

class Scene:
  def __init__(self, camera, lights, objects, width, height):
    self.camera = camera
    self.lights = lights
    self.objects = objects
    self.width = width
    self.height = height
    self.image = Image(width, height)