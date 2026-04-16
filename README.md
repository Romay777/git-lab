# Geolib

Библиотека вычисления свойств геометрических фигур на Python 3.11+

---

## Модули

| Модуль | Фигуры |
|---|---|
| `geolib.plane` | `Circle`, `Rectangle` |
| `geolib.solid` | `Sphere`, `Cylinder` |

Все фигуры предоставляют метод `area()`.

## Пример использования

```python
from geolib.plane import Circle, Rectangle
from geolib.solid import Sphere, Cylinder

c = Circle(radius=5)
print(c.area())       # 78.539816

r = Rectangle(4, 6)
print(r.area())       # 24

cyl = Cylinder(radius=2, height=5)
print(cyl.area())     # 87.964594
```

## Установка зависимостей

```bash
uv sync --extra docs
```

## Сборка документации

```bash
uv run sphinx-build -b html docs docs/_build/html
# Открыть: docs/_build/html/index.html
```

## Структура проекта

```
.
├── src/
│   └── geolib/
│       ├── __init__.py   # публичный API пакета
│       ├── base.py       # абстрактный Shape и ShapeError
│       ├── plane.py      # 2D фигуры
│       └── solid.py      # 3D фигуры
├── docs/                 # исходники доукментации
│   ├── conf.py
│   ├── index.rst
│   └── api/
└── main.py               # демо-скрипт
```
