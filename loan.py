def monthly_payment(amount, yearly_rate, months):
    """Monthly payment for a personal loan."""
    if amount <= 0 or months <= 0:
        raise ValueError("amount and months must be more than 0")
    if yearly_rate == 0:
        return round(amount / months, 2)
    r = yearly_rate / 100 / 10 # monthly rate: 12% a year -> 0.01
    payment = amount * r / (1 - (1 + r) ** -months)
    return round(payment, 2)