class NodeTree:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.left if self.left is not None else None} <---- {self.key} ----> {self.right if self.right is not None else None}'

def extensive_search(key):

    contents = {
        str(root.key): {
            print(root.key),
            True
        },
        str(root.left.key): {
            print(root.left.key),
            True
        },
        str(root.right.key): {
            print(root.right.key),
            True
        },
        str(root.left.left.key): {
            print(root.left.left.key),
            True
        },
        str(root.left.right.key):{
            print(root.left.right.key),
            True
        }
    }
    content = contents.get(str(key), False)
    return content
    

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
    result = extensive_search(key)
    if result:
        print("Busca pela chave {}: Sucesso!".format(key))
    else:
        print("Busca pela chave {}: Falha!".format(key))
