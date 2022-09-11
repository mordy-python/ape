class Interpreter:
    def __init__(self, AST):
        self.AST = AST

    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for k, v in n.items():
                    self.execute([k, v])
        elif isinstance(node, dict):
            for k, v in n.items():
                self.execute([k, v])

    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == "echo":
            self.echo(loc[1])
        elif loc[0] == "stop":
            self.stop()
        elif loc[0] == "goto":
            self.goto(loc[1])

    def echo(self, content):
        print(content)

    def stop(self):
        quit()

    def goto(self, value):
        for node in self.AST:
            if value in node:
                self.run(node[value])
