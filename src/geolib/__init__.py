"""
Geolib — библиотека геометрических фигур.
==========================================

Модули:

- :mod:`geolib.base`  — базовый класс и исключения
- :mod:`geolib.plane` — 2D фигуры
- :mod:`geolib.solid` — 3D тела

.. code-block:: python

    from geolib.plane import Circle
    from geolib.solid import Sphere

    print(Circle(5).area())   # 78.539816
    print(Sphere(3).volume()) # 113.097336
"""

from geolib.base import Shape, ShapeError
from geolib.plane import Circle, Rectangle
from geolib.solid import Sphere, Cylinder

__all__ = ["Shape", "ShapeError", "Circle", "Rectangle", "Sphere", "Cylinder"]
__version__ = "0.1.0"
