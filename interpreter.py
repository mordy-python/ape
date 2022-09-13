class Interpreter:
    def __init__(self, tokens, env: dict, builtins: dict) -> None:
        self.tokens = tokens
        self.env = env
        self.builtins = builtins

    def evaluate(self):
        for token in self.tokens:
            verb, subjects = token.values()
            if verb in self.builtins:
                self.builtins[verb](self.evaluate_subjects(subjects))
            elif verb in self.env:
                self.env[verb](self.evaluate_subjects(subjects))

    def evaluate_subjects(self, subjects):
        ret = []
        for sub in subjects:
            type_, value = sub.values()
            if type_ == "identifier":
                if value in self.env:
                    ret.append(self.env[value])
                elif value in self.builtins:
                    ret.append(self.builtins[value])
                else:
                    raise Exception(f"{value!r} was never defined")
            else:
                ret.append(value)

        return ret