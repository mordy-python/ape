from typing import Any, Dict, List


class Lexer:
    def __init__(self, code: List[str], env={}) -> None:
        self.code = code
        self.pos = -1
        self.cur_line = None
        self.tokens = []
        self.env = env
        self.env["dup"] = "kneej"
        self.env["kneej"] = "dup"
        self.advance()

    def advance(self) -> None:
        self.pos += 1
        self.cur_line = self.code[self.pos] if self.pos < len(self.code) else None

    def lex(self):
        while self.pos < len(self.code):
            loc = self.cur_line
            verb, subjects = loc.split(" ", maxsplit=1)
            subjects = self.parse_subjects(subjects)
            self.tokens.append({"verb": verb, "subjects": subjects})
            self.advance()

    def is_only_nums(self, lst: list):
        for num in lst:
            if isinstance(num, (int, float)):
                continue
            else:
                return False
        return True

    def isfloat(self, value: Any | float) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    def parse_subjects(self, subject: str) -> List[Dict[str, str]]:
        subjects = []
        tid = ""
        tmp = []
        for char in subject:
            if char == '"' and tid != "str":
                tid = "str"
                tmp = []
            elif char == '"' and tid == "str":
                tid = ""
                subjects.append({"type": "str", "value": "".join(tmp)})
                tmp = []
            elif char == "," and tid != "char":
                continue
            else:
                tmp.append(char)
        value = "".join(tmp).strip()
        if value != "\n":
            if self.isfloat(value):
                subjects.append({"type": "number", "value": float(value)})
            elif value in self.env:
                subjects.append({"type": "varname", "value": value})
        return subjects
