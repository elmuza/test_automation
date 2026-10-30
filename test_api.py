def check_status(status_code: int) -> bool:
    return status_code == 200


assert check_status(200) is True
assert check_status(404) is False