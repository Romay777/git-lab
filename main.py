from geolib.plane import Circle, Rectangle
from geolib.solid import Sphere, Cylinder

shapes = [Circle(5), Rectangle(4, 6), Sphere(3), Cylinder(2, 5)]
for s in shapes:
    print(s, "→ area:", s.area())

if __name__ == "__main__":
    pass
