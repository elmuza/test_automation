from api_results_analyzer import analyze_api_results

api_results = [
    {"endpoint": "/login", "status": 200, "duration": 0.5},
    {"endpoint": "/users", "status": 201, "duration": 1.2},
    {"endpoint": "/profile", "status": 404, "duration": 0.8},
    {"endpoint": "/orders", "status": 500, "duration": 2.5},
    {"endpoint": "/logout", "status": 204, "duration": 0.3}
]
results = [
    {"endpoint": "/login", "status": 200, "duration": 0.5},
    {"endpoint": "/users", "status": 201, "duration": 1.2},
    {"endpoint": "/logout", "status": 204, "duration": 0.3}
]

def test_normal_results():
    assert analyze_api_results(api_results) == {'passed': 3, 'failed': 2, 'slowest_endpoint': '/orders'}

def test_empty_results():
    assert analyze_api_results([]) == {'passed': 0, 'failed': 0, 'slowest_endpoint': None}
    
def test_all_successful():
    assert analyze_api_results(results) ==   {"passed": 3, "failed": 0, "slowest_endpoint": "/users"}  

