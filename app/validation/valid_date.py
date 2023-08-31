import dateparser

def validate_date(date_str):
    try:
        parsed_date = dateparser.parse(date_str)
        if parsed_date:
            formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
            return formatted_date
        else:
            return None
    except Exception as e:
        return None