#vm.py

class VM:
    def __init__(self):
        self.vars = {}
        self.stack = []
        self.pc = 0
        self.bytecode = []

    def run(self, bytecode):
        self.bytecode = bytecode
        self.pc = 0

        while self.pc < len(self.bytecode):
            instr = self.bytecode[self.pc]
            op = instr[0]

            # LOAD CONST
            if op == "LOAD_CONST":
                self.stack.append(instr[1])

            # LOAD VAR
            elif op == "LOAD_VAR":
                self.stack.append(self.vars[instr[1]])

            # STORE VAR
            elif op == "STORE_VAR":
                value = self.stack.pop()
                self.vars[instr[1]] = value

            # ADD
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

            # SUB
            elif op == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)

            # PRINT
            elif op == "PRINT":
                value = self.stack.pop()
                print(value)

            # CMP >
            elif op == "CMP_GT":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a > b)

            # JUMP IF FALSE
            elif op == "JUMP_IF_FALSE":
                cond = self.stack.pop()
                if not cond:
                    self.pc = instr[1]
                    continue

            # JUMP
            elif op == "JUMP":
                self.pc = instr[1]
                continue

            self.pc += 1