import numpy as np
from modules.vector import Point, Vector
from modules.color import Color
from modules.light import Light
from modules.material import Material
from modules.objects import Sphere
from modules.scene import Scene
from modules.engine import Engine
from PIL import Image

camera = Point(0, 0, -1)

lights = [
  Light(Point(-5, -15, -2), Color('#ffffff'), 1.0),
]

objects = [
  Sphere(Point(0, 104, 35), 100, Material(Color('#ffffff'), specular=0.5)),
  Sphere(Point(-4.5, 1, 10), 3, Material(Color('#880000'), specular=0.6)),
  Sphere(Point(0, -4, 18), 5, Material(Color('#008800'), specular=0.6)),
  Sphere(Point(4.5, 1, 10), 3, Material(Color('#000088'), specular=0.6)),
]

scene = Scene(
  camera = camera,
  lights = lights,
  objects = objects,
  width = 800,
  height = 600
)

engine = Engine(scene, reflection_depth=5)
engine.render()

pixels = scene.image.pixels
image = Image.fromarray(pixels.astype(np.uint8))

image.save('output.png')