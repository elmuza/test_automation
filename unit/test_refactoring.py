from practice_refactoring import count_test_results

tests1 = []

# Случай 2: все тесты успешные
tests2 = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_profile", "status": "passed"}
]

# Случай 3: статусы в разном регистре
tests3 = [
    {"name": "test_login", "status": "PASSED"},
    {"name": "test_logout", "status": "Failed"},
    {"name": "test_profile", "status": "passed"}
]

def test_empty_list():
    assert count_test_results(tests1) == {"passed": 0, "failed": 0}

def test_all_passed():
    assert count_test_results(tests2) == {'passed': 2, 'failed': 0}

def test_mixed_statuses():
    assert count_test_results(tests3) == {'passed': 2, 'failed': 1}
    
