import math

# my files
import data
import vector_math

def sphere_intersection_point(ray, sphere):
    # Multiply two vectors aka dot product.  We multiply the same vector
    # against itself in order to square it
    a = dot_vector(ray.dir, ray.dir)

    # Use difference_point to make a struct vector for the points r.p and s.center
    # and then multiply that with the vector r.dir.  Again we use the dot product
    # to multiply the two vectors.  Finally, multiply the return value by 2.
    b = (2 * dot_vector(difference_point(ray.pt, shere.center), ray.dir))

    # Find the difference between r.p and s.center again to make a vector and
    # square that vector ie use the dot product on the same vector. Then subtract
    # the radois of the circle squared.
    c = (dot_vector(difference_point(ray.p, s.center), difference_point(r.pt, s.center)) - pow(s.radius, 2))

    discriminant = pow(b, 2) - 4 * (a * c)

    # find the roots
    t1 = ((-b + sqrt(discriminant)) / 2 * a)
    t2 = ((-b - sqrt(discriminant)) / 2 * a)

    # No real roots, One real root, and Two real roots
    if discriminant < 0:
        return None
    elif discriminant == 0:
        if t1 < 0 and t2 < 0:
            return None
        elif t1 > 0 and t2 > 0:
            return translate_point(r.pt, scale_vector(r.dir, t1))
    elif discriminant > 0:
        if t1 > 0 and t2 > 0:
            if t1 > t2:
                return translate_point(r.pt, scale_vector(r.dir, t1))
            elif t2 > t1:
                return translate_point(r.pt, scale_vector(r.dir, t2))
            elif t1 == t2:
                return translate_point(r.pt, scale_vector(r.dir, t1))
            else:
                return "Error: invalid roots"
        elif t1 < 0 and t2 < 0:
            return None
        elif t1 > 0 and t2 < 0:
            return translate_point(r.pt, scale_vector(r.dir, t1))
        elif t1 < 0 and t2 > 0:
            return translate_point(r.pt, scale_vector(r.dir, t2))
    else:
        return "Error: invalid discriminant"



def find_intersection_points(sphere_list, ray):
   newlist = []
   for sphere in sphere_list:
      int_pt = sphere_intersection_point(ray, sphere)
      if isinstance(int_pt, data.Point):
         newlist.append((sphere, int_pt))
   return newlist


def sphere_normal_at_point(sphere, point):
   nonscaled = vector_math.vector_from_to(sphere.center, point)
   return vector_math.normalize_vector(nonscaled)
