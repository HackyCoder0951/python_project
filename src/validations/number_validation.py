def get_valid_number(num):
    try:
        result = float(num)
        return result
    except Exception:
        raise Exception("Please enter valid input as number")
