def is_valid_credit_card(card_number: str) -> bool:
    """Luhn algoritmasıyla kredi kartı numarasının geçerli olup olmadığını kontrol eder."""
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
