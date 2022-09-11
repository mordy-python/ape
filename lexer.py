import io
from typing import List


class Lexer:
    def __init__(self, data: io.TextIOWrapper):
        self.data: List[str] = data.readlines()
        # Add newline to last line in file
        self.data[-1] = self.data[-1] + "\n"
        self.tokens = []
        self.keywords = ["echo", "stop", "goto"]

    def tokenizer(self):
        for loc in self.data:
            tmp = []
            tid = ""
            for l in loc:
                if l == '"' and tid == "":
                    tid = "char"
                    tmp = []
                elif l == '"' and tid == "char":
                    self.tokens.append({"id": tid, "value": "".join(tmp)})
                    tid = ""
                    tmp = []
                elif l == ":" and tid != "char":
                    self.tokens.append({"id": "label", "value": "".join(tmp)})
                    tmp = []
                elif l == "\n":
                    if len(tmp) > 0:
                        self.tokens.append({"id": "atom", "value": "".join(tmp)})
                        tmp = []
                elif "".join(tmp) in self.keywords:
                    self.tokens.append({"id": "keyword", "value": "".join(tmp)})
                    tmp = []
                elif l == " " and tid != "char":
                    continue
                else:
                    tmp.append(l)
