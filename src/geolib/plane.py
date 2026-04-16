"""
Двумерные фигуры (:mod:`geolib.plane`)
=======================================

Содержит плоские геометрические фигуры:
:class:`Circle` и :class:`Rectangle`

.. seealso::
    :mod:`geolib.solid` — трёхмерные тела

.. todo::
    Реализовать :class:`Triangle`
"""

from __future__ import annotations

import math

from geolib.base import Shape, ShapeError


class Circle(Shape):
    """Круг, заданный радиусом

    Args:
        radius: Радиус круга (> 0)

    Raises:
        :class:`geolib.base.ShapeError`: Если ``radius <= 0``

    Example:
        >>> c = Circle(5)
        >>> round(c.area(), 2)

    .. seealso::
        :class:`geolib.solid.Sphere` — трехмерный аналог
    """

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ShapeError("radius", f"должен быть > 0, получено {radius!r}")
        self.radius = radius

    def area(self) -> float:
        """Площадь круга (pi * r^2)."""
        return round(math.pi * self.radius ** 2, 6)

    def describe(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    """Прямоугольник, заданный шириной и высотой

    Args:
        width: Ширина (> 0)
        height: Высота (> 0)

    Raises:
        :class:`geolib.base.ShapeError`: Если ``width`` или ``height`` ≤ 0

    Example:
        >>> r = Rectangle(4, 6)
        >>> r.area()
        24

    .. seealso::
        :class:`geolib.solid.Cylinder` — тело с круглым основанием
    """

    def __init__(self, width: float, height: float) -> None:
        if width <= 0:
            raise ShapeError("width", f"должна быть > 0, получено {width!r}")
        if height <= 0:
            raise ShapeError("height", f"должна быть > 0, получено {height!r}")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Площадь прямоугольника (width * height)"""
        return self.width * self.height

    def describe(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
