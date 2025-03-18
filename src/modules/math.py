def add(*args):
    sum = 0
    try:
        for arg in args:
            sum += int(arg)
        return sum
    except TypeError:
        return "Error: Input must be a number"
    except ValueError:
        return "Error2: Input must be a number"
    except Exception as e:
        return f"An error occurred: {e}"


