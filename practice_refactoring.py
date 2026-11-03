 
SUCCESS_STATUSES = (200, 201, 204)
CLIENT_ERRORS = (400, 401, 403, 404)
SERVER_ERRORS = (500, 502, 503)

def check_response(response):
    if response['status'] in SUCCESS_STATUSES:
        return 'PASSED'
    elif response['status'] in CLIENT_ERRORS:
        return "CLIENT ERROR"
    elif response['status'] in SERVER_ERRORS:
        return "SERVER ERROR"
    else:
        return "UNKNOWN STATUS"

responses = [
    {"status": 200},
    {"status": 201},
    {"status": 400},
    {"status": 404},
    {"status": 500},
    {"status": 503},
    {"status": 302}
]

# for response in responses:
#     print(check_response(response))
    
test_results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_logout", "status": "failed"},
    {"name": "test_profile", "status": "passed"},
    {"name": "test_payment", "status": "failed"},
    {"name": "test_search", "status": "passed"}
]

def count_test_results(test_results):
    count_passed = 0
    count_failed = 0
    for test in test_results:
        if test['status'].lower() == 'passed':
            count_passed +=1
        if test['status'].lower() == "failed":
            count_failed +=1
    
    return {
             "passed": count_passed,
            "failed": count_failed
    }
# print(count_test_results(test_results))

# Случай 1: пустой список
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

if __name__ == "__main__":
    print(count_test_results(tests1))
    print(count_test_results(tests2))
    print(count_test_results(tests3))