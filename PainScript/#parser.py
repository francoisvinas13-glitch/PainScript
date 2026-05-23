# parser.py

def parse_value(v):
    v = v.strip()

    if v.isdigit():
        return {"type": "number", "value": int(v)}

    if v.startswith('"') and v.endswith('"'):
        return {"type": "string", "value": v[1:-1]}

    return {"type": "var", "name": v}


def build_ast(lines):
    ast = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # --- ASSIGN ---
        if line.startswith("prendre"):
            _, rest = line.split(" ", 1)
            name, value = rest.split("=")

            ast.append({
                "type": "assign",
                "name": name.strip(),
                "value": parse_value(value)
            })

        # --- PRINT ---
        elif line.startswith("sortir_du_four"):
            inside = line[line.find("(")+1 : line.rfind(")")]

            ast.append({
                "type": "print",
                "value": parse_value(inside)
            })

        # --- IF (simple version) ---
        elif line.startswith("si"):
            condition = line[3:].split("alors")[0].strip()

            body = []
            i += 1

            while i < len(lines) and lines[i].strip() != "fin":
                body.append(lines[i].strip())
                i += 1

            ast.append({
                "type": "if",
                "condition": condition,
                "body": build_ast(body)
            })

        # --- WHILE ---
        elif line.startswith("tant_que"):
            condition = line.replace("tant_que", "").strip()

            body = []
            i += 1

            while i < len(lines) and lines[i].strip() != "fin":
                body.append(lines[i].strip())
                i += 1

            ast.append({
                "type": "while",
                "condition": condition,
                "body": build_ast(body)
            })

        # --- FUNCTION CALL ---
        elif line.startswith("faire"):
            _, name = line.split(" ", 1)

            ast.append({
                "type": "call",
                "name": name.strip(),
                "args": []
            })

        i += 1

    return ast