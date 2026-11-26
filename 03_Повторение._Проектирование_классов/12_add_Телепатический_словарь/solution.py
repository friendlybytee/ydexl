class TelepathicDictionary(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        return f"Телепатически угадано: {key}"

    def __setitem__(self, key, value):
        print(f"Телепатически записано: {key} = {value}")
        super().__setitem__(key, value)

    def recall(self):
        for k in sorted(self):
            print(f"{k}: {super().__getitem__(k)}")

    def __add__(self, other):
        a = TelepathicDictionary()
        a.update(other)
        a.update(self)
        return a
