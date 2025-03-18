def take_user_input(prompt="Enter a input: ", inputType=str):
    try:
        user_input = inputType(input(prompt))

        if type(user_input) == inputType:
            return user_input

    except Exception:
        raise Exception("Invalid input. Please try again.")