#ast.py

def make_node(node_type, **kwargs):
    node = {"type": node_type}
    node.update(kwargs)
    return node