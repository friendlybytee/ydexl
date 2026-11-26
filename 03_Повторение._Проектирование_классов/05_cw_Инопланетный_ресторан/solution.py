class DangerousDrinkError(Exception):
    pass


class HighSugarError(Exception):
    pass


class TooFizzyError(Exception):
    pass


def order(drink_name, sugar_amount):
    fizziness = len(drink_name.split()) * (sugar_amount % 3)
    a = drink_name.lower()
    if "грызлодёр" in a or "gargle blaster" in a:
        raise DangerousDrinkError("Вогоны отказались подавать грызлодёр: слишком опасно для землян!")
    if sugar_amount > 50:
        raise HighSugarError(f"Слишком много сахара! {sugar_amount} г превышает допустимую норму в 50 г.")
    if fizziness > 10:
        raise TooFizzyError(f"Напиток слишком шипучий! Шипучесть = {fizziness}")
    return "Заказ принят! Приятного аппетита!"
