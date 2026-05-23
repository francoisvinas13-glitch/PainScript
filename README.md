PainScript is a custom programming language inspired by baking concepts.  
It is implemented in Python and features a full execution pipeline:

**Source Code → AST → Bytecode → Virtual Machine**

The goal of this project is to understand how programming languages work under the hood.

---

# 🚀 Features

- 🧠 Custom parser (source → AST)
- ⚙️ Bytecode compiler
- 🧱 Virtual machine execution
- 🍞 Bakery-themed syntax
- 🔁 Variables, conditions, loops
- 📦 Extensible design (functions, scope planned)

---

# 🧱 Architecture


PainScript code
↓
Parser
↓
AST
↓
Compiler
↓
Bytecode
↓
VM
↓
Output


---

# 📜 Language Example

```txt
prendre farine = 100
prendre eau = 50
prendre levain = 10

sortir_du_four("Début de la recette 🥐")

prendre pate = farine + eau + levain

si pate > 120 alors
    sortir_du_four("Pâte trop grosse 🥖")
sinon
    sortir_du_four("Pâte parfaite 🥐")
fin

prendre i = 0

tant_que i < 5
    sortir_du_four(i)
    prendre i = i + 1
fin

sortir_du_four("Cuisson terminée 🔥")
⚙️ Installation
git clone https://github.com/yourname/painscript.git
cd painscript
python run.py
▶️ Run
python run.py
