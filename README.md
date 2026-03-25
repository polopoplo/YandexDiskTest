# Автотесты для Yandex Disk API

Проект с тестами API Яндекс.Диска на Python + pytest + requests.

## Стек
- Python 3.11
- pytest
- requests


## Что тестирую
- GET /resources — список файлов/папок
- PUT /resources — создание папки
- DELETE /resources — удаление папки  
- POST /resources/publish — публикация папки

## Как запустить

1. Клонируй репозиторий:
git clone https://github.com/polopoplo/YandexDiskTest.git

2. Установи зависимости:
pip install -r requirements.txt

3. Создай `config.py` и вставь свой токен:
TOKEN = "твой_токен_от_диска"

4. Запусти:
pytest



## Author
Vladimir