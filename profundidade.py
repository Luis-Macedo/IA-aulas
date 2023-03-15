class NodeTree:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.key)
    in_order(root.right)

def search_node(root, key):
    print(root.key if root is not None else "")
    if root is None:
        return None
    if root.key == key:
        return root
    else:
        left = search_node(root.left, key)
        return left if left is not None else search_node(root.right, key)
    

initial = [True, "green", "blue", "blue", "green"]
values = [
    ["green", True, "blue", "blue", "green"], 
    ["green", "blue", True, "blue", "green"], 
    ["blue", True, "green", "blue", "green"], 
    ["blue", True, "blue", "green", "green"]
]

possible_results = [
    ["blue", "blue", "green", True, "green"], 
    ["blue", "blue", "green", "green", True], 
    [True, "blue", "blue", "green", "green"],
    ["blue", "blue", True, "green", "green"], 
    ["blue", True, "blue", "green", "green"]
]

root = NodeTree(initial)
root.left = NodeTree(values[0])
root.left.left = NodeTree(values[1])
root.left.right = NodeTree(values[2])
root.right = NodeTree(values[3])

for key in possible_results:
    result = search_node(root, key)
    if result:
        print("Busca pela chave {}: Sucesso!".format(key))
    else:
        print("Busca pela chave {}: Falha!".format(key))

in_order(root)
