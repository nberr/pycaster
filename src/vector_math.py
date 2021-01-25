import math

# my files
import data

# This function creates (and returns) a new vector with components
# equal to the original vector scaled (i.e., multiplied) by the
# scalar argument.
def scale_vector(vector, scalar):
   return data.Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)

# This function performs a type of multiplication (product) on vectors
def dot_vector(vector1, vector2):
   return ((vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z))

# length of the vector; magnitude
def length_vector(vector):
   return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

# The function creates (and returns) a new vector by normalizing
# the input vector. This means that the resulting vector has the
# same direction but a magnitude of 1. In short, the new vector
# is the original vector scaled by the inverse of its length.
def normalize_vector(vector):
   return scale_vector(vector, (1. / length_vector(vector)))

# This function creates (and returns) a new vector obtained by
# subtracting from point point1 the point point2
# (i.e., point1 - point2). This is computed by subtracting
# the corresponding x-, y-, and z-components.
# This gives a vector, conceptually, pointing from point2 to point1.
def difference_point(point1, point2):
   return data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)

# This functions creates (and returns) a new vector obtained by
# subtracting from vector vector1 the vector vector2
# (i.e., vector1 - vector2). This is computed by subtracting the
# corresponding x-, y-, and z-components.
# (Yes, this is very similar to the previous function;
# the types, however, are conceptually different.)
def difference_vector(vector1, vector2):
   return data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

# This function creates (and returns) a new point created by
# translating (i.e., moving) the argument point in the direction
# of and by the magnitude of the argument vector.
# You can think of this as the argument vector directing the new
# point where and how far to go from the argument point.
def translate_point(point, vector):
   return data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)

# This function is simply added to improve readability (and,
# thereby, to reduce confusion in later assignments). A vector
# in the direction from one point (from_point) to
# another (to_point) can be found by subtracting
# (i.e., point difference) from_point from to_point
# (i.e., to_point - from_point).
def vector_from_to(from_point, to_point):
   return data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)

# helper functions
# distance between 2 points
def distance(point1, point2):
   dx = point2.x - point1.x
   dy = point2.y - point1.y
   dz = point2.z - point1.z
   return math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))
