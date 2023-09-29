from collections import deque
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Tree:
    val: Optional[int] = None
    left: Optional['Tree'] = None
    right: Optional['Tree'] = None
    
    @classmethod
    def build_tree(cls, nodes: List[int]) -> 'Tree':
        tree = cls()
        queue = deque([tree])
        for node in nodes:
            t = queue.popleft()
            if node != 'x':
                t.val, t.left, t.right = int(node), cls(), cls()
                queue.append(t.left)
                queue.append(t.right)
        
        return tree


nodes = input().split()
tree = Tree.build_tree(nodes)

def dfs(tree, maximum = -100):
    if tree.val is None:
        return 0
    
    maximum = max(tree.val, maximum)
    return int(tree.val >= maximum) + dfs(tree.left, maximum) + dfs(tree.right, maximum)

print(dfs(tree))