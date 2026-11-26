from dataclasses import make_dataclass

GuideEntry = make_dataclass('GuideEntry', [('planet', str), ('entry', str), ('danger_level', int, 0)])
magrathea = GuideEntry("Магратея", "Планета, созданная специально для строительства...", 10)
