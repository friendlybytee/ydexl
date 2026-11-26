class GalaxyGuideError(Exception):
    pass


class PageNotFoundError(GalaxyGuideError):
    pass


class BabbleFishError(GalaxyGuideError):
    pass


class InvalidCoordinatesError(GalaxyGuideError):
    pass


def search_planet(guide, planet_name, coordinates):
    if planet_name not in guide:
        raise PageNotFoundError(f"Страница о планете '{planet_name}' не найдена в путеводителе.")
    description, correct_coords = guide[planet_name]
    if coordinates != correct_coords:
        raise InvalidCoordinatesError(f"Неверные координаты для планеты '{planet_name}'. Ожидалось {correct_coords}, получено {coordinates}")
    if not description:
        raise BabbleFishError(f"Не удалось перевести описание планеты '{planet_name}': язык не распознан.")
    return f"Описание планеты {planet_name}: {description}"
