'''
Leftover Blocks

You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

PROBLEM
    INPUT
    • No. of blocks (int)
    
    OUTPUT
    • Leftover blocks (int) after building tallest possible strucutre
    
    RULES
    • Explicit:
        - Layered structure
        - Top layer is a single block
        - Upper layer block must be supported by 4 blocks in a lower layer
        - Lower layer block can support more than 1 block in an upper layer
        - No gaps between blocks in any layer
    
    • Implicit:
        - Layer block count is the square of layer (or correlates to layer count)
        - No. of blocks in a layer: layer * layer, or layer ** 2
        - Layers are suare roots:
        print(2**2)
        print(3**2)
        print(4**2)
        print(5**2)


EXAMPLES
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

DATA STRUCTURE
No clear requirements around data structure, wireframe with nested lists for now.
[
    [x],
    [x, x, x, x],
    [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
]


ALGORYTHM

'''

def calculate_leftover_blocks(blocks):
    block_tower = []                    # []
    for num in range(1, blocks + 1):    # 1, 2, 3, 4
        block_tower.append(num**2)      # 1, 4, 9, 16
        if sum(block_tower) >= blocks:  # 5 [1, 4]
            break
    
    remaining_blocks = blocks
    
    for block in block_tower:
        if remaining_blocks >= block:
            remaining_blocks -= block 
        
    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True