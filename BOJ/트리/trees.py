lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]

preans, inans, postans = [], [], []

def preorder(cur):
	preans.append(cur)
	if lc[cur] != 0:
		preorder(lc[cur])
	if rc[cur] != 0:
		preorder(rc[cur])
		

def inorder(cur):
	if lc[cur] != 0:
		inorder(lc[cur])
	inans.append(cur)
	if rc[cur] != 0:
		inorder(rc[cur])
		

def postorder(cur):
	if lc[cur] != 0:
		postorder(lc[cur])
	if rc[cur] != 0:
		postorder(rc[cur])
	postans.append(cur)
	
preorder(1)
inorder(1)
postorder(1)

print(' '.join(map(str, preans)))
print(' '.join(map(str, inans)))
print(' '.join(map(str, postans)))