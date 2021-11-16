import re


def main():
    flag = [False, False, False, False, False, False]
    password = input("enter password: ")
    flag[0] = True if len(password) >= 8 else "password len must be >= 8"
    flag[1] = True if len(
        password) >= 12 else "increase password len at least to 12 digits"
    flag[2] = True if re.search(
        "[a-z]", password) is not None else "add lowercase letters"
    flag[3] = True if re.search(
        "[A-Z]", password) is not None else "add uppercase letters"
    flag[4] = True if re.search(
        "[0-9]", password) is not None else "add digits"
    flag[5] = True if re.search(
        "[@!?<>$%]", password) is not None else "add special characters"
    print("strong password") if all(flag) else [
          print(i) for i in flag if i is not True]


main()
