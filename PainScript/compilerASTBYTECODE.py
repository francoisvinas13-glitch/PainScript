#compiler_AST_BYTECODE.py
def compile_expr(expr):
    """
    Compile une expression simple (version v1)
    """

    # NUMBER
    if expr["type"] == "number":
        return [("LOAD_CONST", expr["value"])]

    # STRING
    if expr["type"] == "string":
        return [("LOAD_CONST", expr["value"])]

    # VARIABLE
    if expr["type"] == "var":
        return [("LOAD_VAR", expr["name"])]

    return []


def compile_ast(ast):
    bytecode = []

    for node in ast:

        # --- ASSIGN ---
        if node["type"] == "assign":
            bytecode += compile_expr(node["value"])
            bytecode.append(("STORE_VAR", node["name"]))

        # --- PRINT ---
        elif node["type"] == "print":
            bytecode += compile_expr(node["value"])
            bytecode.append(("PRINT",))

        # --- IF ---
        elif node["type"] == "if":
            # condition simple (x > 5 format brut)
            cond = node["condition"].split(">")

            left = cond[0].strip()
            right = cond[1].strip()

            bytecode.append(("LOAD_VAR", left))
            bytecode.append(("LOAD_CONST", int(right)))
            bytecode.append(("CMP_GT",))

            # placeholder jump (sera patché après)
            jump_index = len(bytecode)
            bytecode.append(("JUMP_IF_FALSE", None))

            # body
            for stmt in compile_ast(node["body"]):
                bytecode.append(stmt)

            # patch jump
            bytecode[jump_index] = ("JUMP_IF_FALSE", len(bytecode))

        # --- WHILE ---
        elif node["type"] == "while":
            start = len(bytecode)

            cond = node["condition"].split("<")

            left = cond[0].strip()
            right = cond[1].strip()

            bytecode.append(("LOAD_VAR", left))
            bytecode.append(("LOAD_CONST", int(right)))
            bytecode.append(("CMP_GT",))

            jump_false = len(bytecode)
            bytecode.append(("JUMP_IF_FALSE", None))

            # body
            for stmt in compile_ast(node["body"]):
                bytecode.append(stmt)

            bytecode.append(("JUMP", start))

            bytecode[jump_false] = ("JUMP_IF_FALSE", len(bytecode))

        # --- CALL ---
        elif node["type"] == "call":
            # version simple = print hack
            if node["name"] == "pain":
                bytecode.append(("PRINT",))

    return bytecode