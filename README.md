# QA Automation Project

Учебный проект по автоматизации тестирования на Python.

## О проекте

В этом репозитории я изучаю Python, Pytest, Git и основы QA Automation.

Проект содержит учебные автоматизированные тесты и практические задания.

## Технологии

- Python
- Pytest
- Git
- GitHub
- VS Code

## Структура проекта

- `api/local/` — локальное FastAPI-приложение и тесты товаров.
- `api/jsonplaceholder/` — тесты внешнего JSONPlaceholder API.
- `unit/` — небольшие модули и тесты к ним: калькулятор, анализатор API-результатов и рефакторинг.
- `pytest_basics/` — упражнения по assertions, fixtures, scopes и авторизации.
- `bank_account/` — модель банковского счёта, тесты и тестовые данные.
- `shopping_cart/` — модель корзины и её тесты.
- `practice_ddt/` — упражнения по DDT с JSON/CSV и тестовые данные.
- `practice_hooks/` — упражнения по pytest hooks.
- `requests_practice/` — примеры работы с HTTP-запросами.
- `practice_cli/` — упражнения по работе с командной строкой.

## Установка

1. Скачать репозиторий.
2. Создать виртуальное окружение:

   `python -m venv .venv`

3. Активировать виртуальное окружение в Windows PowerShell:

   `.\.venv\Scripts\Activate.ps1`

4. Установить Pytest:

   `python -m pip install pytest`

## Запуск тестов

Выполнить команду:

`python -m pytest -v`

## Цель проекта

Научиться писать, запускать и поддерживать автоматизированные тесты на Python.