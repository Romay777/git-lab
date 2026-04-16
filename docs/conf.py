"""Конфигурация Sphinx для проекта Geolib."""

import os
import sys

# Добавляем src/ в path, чтобы autodoc нашёл пакет
sys.path.insert(0, os.path.abspath("../src"))

# -- Метаданные проекта -----------------------------------------------------
project = "Geolib"
author = "Просто человек"
copyright = "2026"
release = "0.1.0"
version = "0.1"

# -- Общая конфигурация -------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",       # авто-генерация из docstring
    "sphinx.ext.napoleon",      # поддержка Google-стиля docstring
    "sphinx.ext.viewcode",      # ссылки «посмотреть исходный код»
    "sphinx.ext.todo",          # блоки .. todo::
    "sphinx.ext.autosummary",   # таблицы-сводки API
    "sphinx.ext.intersphinx",   # перекрёстные ссылки на внешние проекты
]

# Показывать блоки .. todo:: в выводе
todo_include_todos = True

# Настройки napoleon для Google-стиля docstring
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False

# Intersphinx: ссылки на документацию Python stdlib
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Autodoc: порядок членов и настройки
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
    "special-members": "__init__",
}

# -- HTML вывод ---------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = f"{project} {release}"
html_show_sourcelink = True

# Логотип и фавиконка (файлы кладём в docs/_static/)
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"

# Параметры темы ReadTheDocs
html_theme_options = {
    "navigation_depth": 4,
    "titles_only": False,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
}

