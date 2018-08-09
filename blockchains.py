from blocks import Block
import datetime

num_blocks_to_add = 10 #all blocks depend on the previous block except the genisis block

block_chain = [Block.create_genesis_block()] #gives us 1st blocks hash value

print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)

for i in range(1, num_blocks_to_add): #from 1-10 create blocks
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)