import phonenumbers


def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "TR")
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False
