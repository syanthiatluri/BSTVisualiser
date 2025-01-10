from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def construct_tree_structure(node):
    if not node:
        return None
    return {
        'key': node.key,
        'left': construct_tree_structure(node.left),
        'right': construct_tree_structure(node.right)
    }


root = None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_values():
    global root
    values = request.json['values']
    for value in values:
        root = insert(root, value)  
    tree_structure = construct_tree_structure(root)
    return jsonify(tree=tree_structure)

@app.route('/delete', methods=['POST'])
def delete_values():
    global root
    values = request.json['values']
    for value in values:
        root = delete(root, value)
    tree_structure = construct_tree_structure(root)
    return jsonify(tree=tree_structure)

if __name__ == '__main__':
    app.run(debug=True)
