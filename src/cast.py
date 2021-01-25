import sys
import math

# my files
import data
import vector_math
import collisions

#returns color or closest sphere intersected, or the color white
def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
   return False

def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
   eye_point, sphere_list, ambient_color, light):
   y_interval = (max_y - min_y) / float(height)
   x_interval = (max_x - min_x) / float(width)

   outfile = open("image.ppm", "w")

   print >> outfile, "P3"
   print >> outfile, "%d %d" % (width, height)
   print >> outfile, "255"


   for i in range(height):
      for j in range(width):
         y = max_y - (i * y_interval)
         x = min_x + (j * x_interval)
         viewpoint = data.Point(x, y, 0)
         ray_dir = vector_math.difference_point(viewpoint, eye_point)
         ray_to_cast = data.Ray(eye_point, ray_dir)
         spherecolor = cast_ray(ray_to_cast, sphere_list, ambient_color, light,
            eye_point)
         print >> outfile, "%d %d %d" % (spherecolor.r * 255,
                             spherecolor.g * 255,
                             spherecolor.b * 255)
