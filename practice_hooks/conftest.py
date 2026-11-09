import pytest
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        file_path = Path("practice_hooks/failed_tests.txt")

        with file_path.open("a", encoding="utf-8") as file:
            file.write(f"FAILED: {item.nodeid}\n")

        print(f"\nОшибка записана в файл: {file_path}")
        print(f"Обнаружен упавший тест: {item.name}")