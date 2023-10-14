class Commentary:
    def __init__(self, txt: str):
        self.txt = txt

    def exec(self):
        return {'commentary': f' -> {self.txt}'}