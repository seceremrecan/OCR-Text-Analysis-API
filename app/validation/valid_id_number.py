import re


def tc_validate(input_data):
    tcno = input_data
    if isinstance(input_data, dict) and "tcno" in input_data and input_data["tcno"]:
        tcno = input_data["tcno"]

    if isinstance(tcno, dict):
        input_keys = list(tcno.keys())
        tcno = tcno[input_keys[0]]

    if not re.match(r"^[1-9]{1}[0-9]{9}[02468]{1}$", tcno):
        return False

    odd = int(tcno[0]) + int(tcno[2]) + int(tcno[4]) + int(tcno[6]) + int(tcno[8])
    even = int(tcno[1]) + int(tcno[3]) + int(tcno[5]) + int(tcno[7])
    digit10 = (odd * 7 - even) % 10
    total = (odd + even + int(tcno[9])) % 10

    if digit10 != int(tcno[9]) or total != int(tcno[10]):
        return False

    return True