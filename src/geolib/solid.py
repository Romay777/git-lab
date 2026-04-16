"""
Трёхмерные тела (:mod:`geolib.solid`)
======================================

Содержит пространственные тела:
:class:`Sphere` и :class:`Cylinder`.

.. seealso::
    :mod:`geolib.plane` — двумерные фигуры.
"""

from __future__ import annotations

import math

from geolib.base import Shape, ShapeError


class Sphere(Shape):
    """Шар, заданный радиусом.

    Args:
        radius: Радиус шара (> 0).

    Raises:
        :class:`geolib.base.ShapeError`: Если ``radius <= 0``.

    Example:
        >>> s = Sphere(3)
        >>> round(s.area(), 2)
        113.1

    .. seealso::
        :class:`geolib.plane.Circle` — двумерный аналог.
    """

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ShapeError("radius", f"должен быть > 0, получено {radius!r}")
        self.radius = radius

    def area(self) -> float:
        """Площадь поверхности шара (4 * pi * r^2)."""
        return round(4 * math.pi * self.radius ** 2, 6)

    def describe(self) -> str:
        return f"Sphere(radius={self.radius})"


class Cylinder(Shape):
    """Прямой круговой цилиндр.

    Args:
        radius: Радиус основания (> 0).
        height: Высота (> 0).

    Raises:
        :class:`geolib.base.ShapeError`: Если ``radius`` или ``height`` ≤ 0.

    Example:
        >>> c = Cylinder(2, 5)
        >>> round(c.area(), 2)
        87.96

    .. note::
        ``area()`` включает оба основания и боковую поверхность: 2 * pi * r * (r + h).

    .. seealso::
        :class:`geolib.plane.Circle` — основание цилиндра.
    """

    def __init__(self, radius: float, height: float) -> None:
        if radius <= 0:
            raise ShapeError("radius", f"должен быть > 0, получено {radius!r}")
        if height <= 0:
            raise ShapeError("height", f"должна быть > 0, получено {height!r}")
        self.radius = radius
        self.height = height

    def area(self) -> float:
        """Полная площадь поверхности (2 * pi * r * (r + h))."""
        return round(2 * math.pi * self.radius * (self.radius + self.height), 6)

    def describe(self) -> str:
        return f"Cylinder(radius={self.radius}, height={self.height})"
