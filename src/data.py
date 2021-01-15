
def epsilon_eq(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

class Point:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

class Vector:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

class Ray:
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir

   def __eq__(self, other):
      return (self.pt == other.pt and self.dir == other.dir)

class Sphere:
   def __init__(self, center, radius):
      self.center = center
      self.radius = radius

   def __eq__(self, other):
      return (self.center == other.center
         and epsilon_eq(self.radius, other.radius)
         and self.color == other.color
         and self.finish == other.finish)
