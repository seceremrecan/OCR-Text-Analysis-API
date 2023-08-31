from enum import Enum

import validators

from app.validation import valid_credit_card, valid_email, valid_phone_number,valid_date,valid_id_number


class DataType(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    EMAIL = "EMAIL"
    URL = "URL"
    DOMAIN = "DOMAIN"
    HASH="HASH"
    PHONE_NUMBER = "PHONE_NUMBER"
    COMBOLIST = "COMBOLIST"
    DATE = "DATE"
    ID_NUMBER = "ID_NUMBER"
    PLATE = "PLATE"
    # Diğer veri türlerini buraya ekleyebilirsiniz

    def process_data(self, match):
        if self in data_processing_functions:
            return data_processing_functions[self](match)
        else:
            return True


# Veri türlerine özel işlemleri saklayan sözlük
data_processing_functions = {
    DataType.CREDIT_CARD: lambda match: valid_credit_card.is_valid_credit_card(
        match.replace(" ", "").replace("-", "")
    ),
    DataType.DATE: lambda match: valid_date.validate_date(match),
    DataType.ID_NUMBER: lambda match: valid_id_number.tc_validate(match),
    DataType.EMAIL: lambda match: valid_email.process_email(match),
    DataType.URL: lambda match: validators.url(match),
    DataType.DOMAIN: lambda match: validators.domain(match),
    DataType.HASH: lambda match: validators.md5(match)
    or validators.sha1(match)
    or validators.sha256(match),
}
