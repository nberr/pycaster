# point contains 3 values: x, y, z
class Point:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   # comparing two points
   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

# vector contains 3 values: x, y, z
class Vector:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   # comparing two vectors
   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

# ray contains a point: pt and vector: dir
class Ray:
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir
   # comparing two rays
   def __eq__(self, other):
      return (self.pt == other.pt
         and self.dir == other.dir)

# sphere contains a point: center, radius, color, and finish
class Sphere:
   def __init__(self, center, radius, color, finish):
      self.center = center
      self.radius = float(radius)
      self.color = color
      self.finish = finish
   # comparing two spheres
   def __eq__(self, other):
      return (self.center == other.center
         and epsilon_eq(self.radius, other.radius)
         and self.color == other.color
         and self.finish == other.finish)

# color contains RGB values r, g, and b
class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b

   # comparing two colors
   def __eq__(self, other):
      return (epsilon_eq(self.r, other.r) and
              epsilon_eq(self.g, other.g) and
              epsilon_eq(self.b, other.b))



class Finish:
   def __init__(self, ambient, diffuse, specular, roughness):
      self.ambient = ambient
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness

   def __eq__(self, other):
      return (epsilon_eq(self.ambient, other.ambient) and
              epsilon_eq(self.diffuse, other.diffuse) and
              epsilon_eq(self.specular, other.specular) and
              epsilon_eq(self.roughness, other.roughness))

class Light:
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color

   def __eq__(self, other):
      return self.pt == other.pt and self.color == other.color

# helper functions
# used for comparing two objects
def epsilon_eq(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)
