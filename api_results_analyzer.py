
SUCCESS_STATUSES = (200, 201, 204)

def analyze_api_results(results):
    count_success_statuses = 0
    count_failed_statuses = 0
    max_duration = None
    slowest_endpoint = None
    for result in results:
        if max_duration is None or result['duration'] > max_duration:
            max_duration = result['duration']
            slowest_endpoint = result["endpoint"]
        if result['status'] in SUCCESS_STATUSES:
            count_success_statuses += 1
        else:
            count_failed_statuses += 1
    return {
            "passed": count_success_statuses,
            "failed": count_failed_statuses,
            "slowest_endpoint": slowest_endpoint
        }

if __name__ == "__main__":
    print(analyze_api_results([]))
    