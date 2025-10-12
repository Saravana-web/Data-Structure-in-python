class Node:
    def __init__(self, enroll_id, name):
        self.enroll_id = enroll_id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Function to get height of a node
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Function to get balance factor
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Insert node
    def insert(self, root, enroll_id, name):
        # 1. Normal BST insertion
        if not root:
            return Node(enroll_id, name)
        elif enroll_id < root.enroll_id:
            root.left = self.insert(root.left, enroll_id, name)
        else:
            root.right = self.insert(root.right, enroll_id, name)

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Check balance
        balance = self.get_balance(root)

        # 4. Balance the tree
        # Left Left
        if balance > 1 and enroll_id < root.left.enroll_id:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and enroll_id > root.right.enroll_id:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and enroll_id > root.left.enroll_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and enroll_id < root.right.enroll_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find minimum value node
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    # Delete node
    def delete(self, root, enroll_id):
        if not root:
            return root
        elif enroll_id < root.enroll_id:
            root.left = self.delete(root.left, enroll_id)
        elif enroll_id > root.enroll_id:
            root.right = self.delete(root.right, enroll_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.enroll_id = temp.enroll_id
            root.name = temp.name
            root.right = self.delete(root.right, temp.enroll_id)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search by Enrollment ID
    def search(self, root, enroll_id):
        if not root:
            return None
        if enroll_id == root.enroll_id:
            return root
        elif enroll_id < root.enroll_id:
            return self.search(root.left, enroll_id)
        else:
            return self.search(root.right, enroll_id)

    # Inorder traversal
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(f"Enrollment ID: {root.enroll_id}, Name: {root.name}")
        self.inorder(root.right)

    # Count total enrollments
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Insert sample records
    root = tree.insert(root, 101, "Vasuu")
    root = tree.insert(root, 105, "Kavi")
    root = tree.insert(root, 102, "Ravi")
    root = tree.insert(root, 110, "Priya")

    print("Inorder Traversal (Sorted by Enrollment ID):")
    tree.inorder(root)

    print("\nTotal Enrollments:", tree.count(root))

    # Search a student
    s = 105
    res = tree.search(root, s)
    if res:
        print(f"\nStudent Found → ID: {res.enroll_id}, Name: {res.name}")
    else:
        print("\nStudent Not Found")

    # Delete a student
    root = tree.delete(root, 102)
    print("\nAfter Deletion (ID=102):")
    tree.inorder(root)
