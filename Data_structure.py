
def merge_after_sum(self, tree1, tree2):
    t1 = tree1
    t2 = tree2
    if t1 is None and t2 is None:
        return None 
    if t1 is None:
        t1 = Node(t2.value)
    if t2 is None :
        return t1
    if t1.left or t2.left:
        merge_after_sum(t1.left, t2.left)
    if t1.right or t2.right:
         merge_after_sum(t1.right, t2.right)
    return t1 

# Convert From list To BST:
# 1. Create a function that receive a sorted list 
# 2. Create inner_fun that receive left , right  as prameters while left 0 for the first time 
# and the last index for the list.
# 3. Creat middle val to reach the middel index by devieding (lastidx - firstidx) by 2
# 4. Create tree node with midle idx as a value 
# 5. Add left node by recur with first and midle-1
# 6. Add right node by recur with midle+1 and last idx as a param
# 7. Return the root.

def sortedArrayToBST(self, nums):
        def inner(left, right):
            if left > right :
                return None 
            midel = (left + right)//2
            root = TreeNode(nums[midel])
            root.left = inner(left, midel-1)
            root.right = inner(midel + 1, right)
            return root
        return inner(0, len(nums)-1)
# ++++++++++++++++++++++++++++++++
# SYmmetric
# 1.Define a function that recevie the root 
# 2.Check if the root is none return False.
# 3.Create another function that receive the same root towice.
# 4.Check for the left and the right if they are both none return True 
# 5.If only one of them is none return False.
# 6. recur in the inner function with sending t1.left t2.right and t1.right t2.left

def isSymmetric(self, root):

        if root is None:
            return False 
        return self.mirro(root, root) 
    
def mirro(self,left , right ):
        if left is None and right is None :
            return True 
        if left is None or right is None :
            return False
        else:
            return left.val == right.val and self.mirro(left.left, right.right) and self.mirro(left.right, right.left)
###
# In range :
# Check If the root is None return 0
# Check if the current node is in range then include it in the sum 
# Call the function for it for the left and the right 
# If the current is smaller return Fun(root.right) 
# If larger Fun(root.right)  
def getCount(root, low, high):
    # Base case
    if root == None:
        return 0
    # Special Optional case for improving
    # efficiency
    if root.data == high and root.data == low:
        return 1
 
    # If current node is in range, then
    # include it in count and recur for
    # left and right children of it
    if root.data <= high and root.data >= low:
        return (1 + getCount(root.left, low, high) +
                    getCount(root.right, low, high))
 
    # If current node is smaller than low,
    # then recur for right child
    elif root.data < low:
        return getCount(root.right, low, high)
 
    # Else recur for left child
    else:
        return getCount(root.left, low, high)
 
        

## Search in a Binary Search Tree
#1. Create a function called search that receive a tree and value to search for.
# 2. Loop throw the tree.
# 3. Compar the current.val with received value and return it if equle 
# 4. If current.val larger than the value make the current quel to the right (current= cureent.right)
# 5. if curretn.val smaller than the value make the current quel to the left (current= cureent.left) 
def searchBST(self, root, val):
    current = root
    while current:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left
    return None
 
# O(N)
# Space: O(1)
 
 
 # Second Minimum:
def findSecondMinimumValue(self, root):
    def inorder(n):
        if n:
            if smallest < n.val < self.second:
                self.second = n.val
            elif smallest == n.val: # bcuz of the property of this special bt 
                inorder(n.left)
                inorder(n.right)
    smallest = root.val
    self.second = float('inf')
    inorder(root)
    return self.second if self.second != float('inf') else -1


# Sum Path:
# Check the root if none return the root
# Subtract the value for the root from the targeted_sum 
# If no left or right for the root return the targted sum == 0
# Recur on the same function with sending the right and the left for the root with targted sum.
def sum_path(root, targeted_sum):
    if root is None:
        return root
    
    targeted_sum-=root.val
    
    if not root.left and not root.right:
        return targeted_sum==0
    
    return  self.sum_path(root.right, targeted_sum) or self.sum_path(root.left, targeted_sum)

# Balcnced 

def solve(self,root):
        if root is None:
            return 0
        lh=self.solve(root.left)
        rh=self.solve(root.right)
        if lh==-1 or rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        return max(lh,rh)+1
def isBalanced(self, root):
        if self.solve(root)!=-1:
            return True
        return False






def isBalanced(self, root):
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        left_height = root.left.val if root.left else 0
        right_height = root.right.val if root.right else 0
        root.val = max(left_height, right_height) + 1
        return False if abs(left_height-right_height) > 1 else (left and right)


def isBalanced(self, root):
        
        if not root:
            return True
        
        def areSubTreesBalanced(node, height):
            if not node:
                return 0
            
            left_height = areSubTreesBalanced(node.left, 1 + height)
            right_height = areSubTreesBalanced(node.right, 1 + height)
            
            if abs(left_height - right_height) > 1:
                return float('inf')
            
            return 1 + max(left_height, right_height)
        
        
        return areSubTreesBalanced(root, 0) != float('inf')




def diameterOfBinaryTree(self, root):

    def recurse(node):
        if not node: 
            return 0
        left, right = recurse(node.left), recurse(node.right)
        self.result = max(self.result, left+right)
        return 1 + max(left, right)

    self.result = 0
    recurse(root)
    return self.result

# Max Depth :

# 1. Define a function that receive a tree
# 2. If there is no root return 0
# 3. return the max one from recure the left and the right.


def maxDepth(self, root):
        if root == None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))



# invert Tree 

# DFT
# 1.Create a function that receive a tree as prameter
# 2. Swap the left and the right elemnt 
# 3. recure for the left if exist 
# 4. recure for the Right if exist
# 5. return the root. 
def invertTree(self, root):
        
        if root:
            # General case:
            # invert child node of current root
            root.left, root.right = root.right, root.left
            # invert subtree with DFS
            if root.left:
                self.invertTree( root.left )
            if root.right:
                self.invertTree( root.right )
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None


## BFT 
def invertTree(self, root):        
        
        traversal_queue = deque([root]) if root else None
        
		# lanuch BFS, aka level-order-traversal to carry out invertion
        while traversal_queue:
            
            cur_node = traversal_queue.popleft()
            
			# Invert child node of current node
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            
			# push left child into queue to invert left subtree
            if cur_node.left:
                traversal_queue.append( cur_node.left )
            
			# push right child into queue to invert right subtree
            if cur_node.right:
                traversal_queue.append( cur_node.right )                
        
        return root

## Sum left nodes:
# Define a function that receive a tree 
# define a variable to save the sum in it and give 0 as initial value 
# Define another function that check for the left node and add the value recure and for the left again.
# If no left  check the right and recure.
# return the total.
# call the inner function.

def sum_left_nodes(root):
	sum_all_left = 0
	if root is None:
		return 0
	def sum_left(root):
		nonlocal sum_all_left
		if root.left:
			sum_all_left += int(root.left.value)
			sum_left(root.left)
		if root.right:
			sum_left(root.right)
		return sum_all_left 
	return sum_left(root)