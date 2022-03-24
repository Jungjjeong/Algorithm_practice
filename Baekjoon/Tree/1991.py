class Node():
	def __init__(self):
		self.val = None
		self.left = None
		self.right = None

	def print_val(self):
		print(self.val, end='')

n = int(input());
tree = []

for _ in range(n):
	root, l, r = map(str, input().split())
	n = Node()
	n.val = root
	n.left = l
	n.right = r
	tree.append(n)

def traverse(node, option):
	if option == "preorder":
		node.print_val()

	if node.left != '.':
		for t in tree:
			if t.val == node.left:
				traverse(t, option)

	if option == "inorder":
		node.print_val()

	if node.right != '.':
		for t in tree:
			if t.val == node.right:
				traverse(t, option)

	if option == "postorder":
		node.print_val()

	if node.left == node.right == '.':			
		return
	


traverse(tree[0], 'preorder')
print()
traverse(tree[0], 'inorder')
print()
traverse(tree[0], 'postorder')