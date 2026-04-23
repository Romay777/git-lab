# Модификация файлов + история изменений

## Добавить в коммит
git add (./<name>)

## Убрать файл
git rm <name>

## Commit
git commit -m 'msg'

# Управление ветками
## Create
git checkout -b <name>

## Merge
git checkout main
git merge <name>

## Слияние веток + решение коллизий

git checkout --ours some_file.txt    # взять версию main
git checkout --theirs some_file.txt  # взять версию ветки

---

## История изменений конкретного файла
git log --follow -p existing_file.txt     # патчи по файлу
git log --oneline -- existing_file.txt    # краткий лог по файлу

## Общий лог проекта
git log --oneline --graph --all --decorate

---

# Метки (теги) на ревизии

## Быстрый тег
git tag v1.0

## Аннотированный тег
git tag -a v1.0 -m "Release version 1.0"

## Тег на конкретный коммит
git tag -a v0.9 <commit-hash> -m "Pre-release"

## Просмотр тегов
git tag -l

## Перейти к тегу
git checkout v1.0

---

# Откат репозитория / файла

## Откатить файл к версии из последнего коммита
git checkout HEAD -- some_file.txt

## Откатить файл
git checkout <commit-hash> -- some_file.txt

## Откатить весь репозиторий к коммиту
git revert <commit-hash>

## Жёсткий сброс к коммиту
git reset --hard <commit-hash>

## Мягкий сброс (изменения остаются в индексе)
git reset --soft <commit-hash>

---
## Дерево проекта
tree

## История всех коммитов
git log --oneline --graph --all --decorate >> report.md

## История конкретного файла
git log --follow --stat -- README.md >> report.md

## Список всех тегов
git tag -l >> report.md

## Статистика изменений по авторам
git shortlog -sn >> report.md

## Полный diff всей истории
git log -p >> report.md

---
# Struct
```
.
├── README.md
├── main.py
├── new_file.txt
├── pyproject.toml
├── report.md
├── src
│   └── geolib
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   ├── base.cpython-311.pyc
│       │   ├── plane.cpython-311.pyc
│       │   └── solid.cpython-311.pyc
│       ├── base.py
│       ├── plane.py
│       └── solid.py
└── uv.lock

4 directories, 14 files
```