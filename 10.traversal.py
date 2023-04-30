class Node:
    def __init__(self,key)  :
        self.key=key
        self.left=None
        self.right=None
def inorder ( root):
        if root!=None:
            inorder(root.left)
            print(root.key)
            inorder(root.right)    
def preorder ( root):
        if root!=None:
            print(root.key)
            preorder(root.left)
            preorder(root.right)    
def postorder ( root):
        if root!=None:
            postorder(root.left)
            postorder(root.right)       
            print(root.key)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(38)
root.right.right=Node(50)
print("preorder)")
inorder(root)
print("inorder")
preorder(root) 
print("postorder")

postorder(root) 