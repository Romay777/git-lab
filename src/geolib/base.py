"""
Базовые классы (:mod:`geolib.base`)
====================================

Определяет абстрактный интерфейс для всех фигур

.. note::
    Создать :class:`Shape` напрямую нельзя — используйте подклассы
    из :mod:`geolib.plane` или :mod:`geolib.solid`
"""

from abc import ABC, abstractmethod


class ShapeError(ValueError):
    """Исключение для некорректных параметров фигуры

    Args:
        field: Название параметра с недопустимым значением
        message: Описание ошибки

    Example:
        >>> raise ShapeError("radius", "должен быть > 0")
    """

    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(f"{field} — {message}")


class Shape(ABC):
    """Абстрактный базовый класс для всех геометрических фигур

    .. todo::
        Добавить метод ``concat()``.

    .. seealso::
        :mod:`geolib.plane`, :mod:`geolib.solid`
    """

    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь

        Returns:
            Площадь в квадратных единицах
        """

    @abstractmethod
    def describe(self) -> str:
        """Возвращает текстовое описание фигуры

        Returns:
            Строка вида ``"ИмяКласса(param=value, ...)"``
        """

    def __repr__(self) -> str:
        return self.describe()
