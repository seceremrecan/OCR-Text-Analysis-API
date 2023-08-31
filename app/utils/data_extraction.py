import re

from app.utils.data_types import DataType
from config import patterns


def extract_sensitive_data(text: str):
    seen_values = set()  # Bu küme, benzersiz değerleri saklamak için kullanılacak
    findings = []

    for data_type, pattern in patterns.items():
        data_type_enum = DataType(data_type)
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]

            # Eğer bu değer daha önce görüldüyse, atla
            if match in seen_values:
                continue

            # Eğer daha önce görülmemişse, kümeye ekle
            seen_values.add(match)

            if data_type_enum.process_data(match):
                findings.append({"value": match, "type": data_type_enum.value})

    return findings
