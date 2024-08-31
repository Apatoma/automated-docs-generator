import ast

def generate_docs_from_code(code, filename):
    """
    Parses the provided code and generates documentation.

    :param code: The code to document as a string.
    :param filename: The name of the file being documented.
    :return: A string containing the generated documentation.
    """
    tree = ast.parse(code)
    docs = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docs.append(f"### Function: `{node.name}`\n")
            docs.append(ast.get_docstring(node) or "No documentation provided.")
            docs.append("\n")
        elif isinstance(node, ast.ClassDef):
            docs.append(f"## Class: `{node.name}`\n")
            docs.append(ast.get_docstring(node) or "No documentation provided.")
            docs.append("\n")
    
    return "\n".join(docs)
