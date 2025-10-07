class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.p = p
        self.left = None
        self.right = None
        
def insert(root, name, time, p):
    if root is None:   
        return Node(name, time, p)
    if name < root.name:   
        root.left = insert(root.left, name, time, p)
    elif name > root.name:
        root.right = insert(root.right, name, time, p)
    return root

def search(root, key):
    if root is None or root.name == key:
        return root
    if key < root.name:
        return search(root.left, key)
    else:
        return search(root.right, key)

def delete(root, key):
    if root is None:
        return root
    if key < root.name:
        root.left = delete(root.left, key)
    elif key > root.name:
        root.right = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.name, root.time, root.purpose = temp.name, temp.time, temp.purpose
        root.right = delete(root.right, temp.name)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.name, root.time, root.p)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.name, root.time, root.p)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.name, root.time, root.p)

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

root = None
while True:
    print("\n1.Insert  2.Delete  3.Search  4.Inorder  5.Preorder  6.Postorder  7.Count  8.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        n = input("Visitor Name: ")
        t = input("Entry Time: ")
        p = input("Purpose: ")
        root = insert(root, n, t, p)

    elif ch == "2":
        k = input("Enter Name to Delete: ")
        root = delete(root, k)

    elif ch == "3":
        k = input("Enter Name to Search: ")
        res = search(root, k)
        if res:
            print("Found:", res.name, res.time, res.p)
        else:
            print("Not Found")

    elif ch == "4":
        print("Inorder Traversal:")
        inorder(root)

    elif ch == "5":
        print("Preorder Traversal:")
        preorder(root)

    elif ch == "6":
        print("Postorder Traversal:")
        postorder(root)

    elif ch == "7":
        print("Total Entries:", count(root))

    elif ch == "8":
        break

    else:
        print("Invalid choice")
