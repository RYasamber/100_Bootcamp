def format_name(age):
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False


print(format_name(12))
