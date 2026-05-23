# run.py


from parser import build_ast
from compiler import compile_ast
from vm import VM


def load_source(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def print_section(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


def main():
    # 1. Charger le code source PainScript
    source = load_source("example.pain")

    print_section("SOURCE CODE")
    print("".join(source))

    # 2. Parser → AST
    ast = build_ast(source)

    print_section("AST")
    for node in ast:
        print(node)

    # 3. Compiler AST → Bytecode
    bytecode = compile_ast(ast)

    print_section("BYTECODE")
    for instr in bytecode:
        print(instr)

    # 4. Exécuter avec la VM
    print_section("VM OUTPUT")

    vm = VM()
    vm.run(bytecode)


if __name__ == "__main__":
    main()