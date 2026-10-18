def monthly_payment(amount, yearly_rate, months):
    """Monthly payment for a personal loan."""
    if amount <= 0 or months <= 0:
        raise ValueError("amount and months must be greater than 0")
    r = yearly_rate / 100 / 12  # monthly rate: 12% a year -> 0.01
    payment = amount * r / (1 - (1 + r) ** -months)
    return round(payment, 2)