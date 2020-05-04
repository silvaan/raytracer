from modules.vector import Point
from modules.ray import Ray
from modules.color import Color

class Engine:
  def __init__(self, scene, reflection_depth=3):
    self.scene = scene
    self.reflection_depth = reflection_depth

  def render(self):
    ratio = float(self.scene.width)/self.scene.height
    x0 = -1.0
    x1 = 1.0
    xstep = (x1-x0)/(self.scene.width-1)
    y0 = -1.0/ratio
    y1 = 1.0/ratio
    ystep = (y1-y0)/(self.scene.height-1)

    for j in range(self.scene.height):
      y = y0 + j*ystep
      for i in range(self.scene.width):
        x = x0 + i*xstep
        ray = Ray(self.scene.camera, Point(x, y) - self.scene.camera)
        self.scene.image.set_pixel(i, j, self.ray_trace(ray).to_list())

  def ray_trace(self, ray, depth=0):
    color = Color()

    if depth >= self.reflection_depth:
      return color

    hit_dist, hit_obj = self.find_nearest(ray)
    if hit_obj is None or hit_dist is None:
      return color

    hit_pos = ray.point(hit_dist)
    normal = hit_obj.normal_at(hit_pos)
    material = hit_obj.material
    to_cam = self.scene.camera - hit_pos

    # Ambient
    color += material.color * material.ambient

    for light in self.scene.lights:
      to_light = Ray(hit_pos, light.position - hit_pos)
      hit_dist_, hit_obj_ = self.find_nearest(to_light)

      if hit_obj_ is None:
        # Difuse Shading
        color += (material.color + 0.3 * light.color * light.intensity) * material.diffuse * max(normal*to_light.direction, 0)

    # Reflection
    reflected_ray = Ray(hit_pos, ray.direction.reflect(normal).normalize())
    color += self.ray_trace(reflected_ray, depth+1) * material.specular

    return color

  def find_nearest(self, ray):
    hit_dist = None
    hit_obj = None
    for obj in self.scene.objects:
      dist = obj.intersects(ray)
      if dist is not None and (hit_obj is None or dist < hit_dist):
        hit_dist = dist
        hit_obj = obj
    return hit_dist, hit_obj