import datetime
import hashlib


class Block:
    def __init__(self, prev_block_hash, data, timestamp):
        self.prev_block_hash = prev_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now()) #creates block instance

    def get_hash(self):
        header_bin = (str(self.prev_block_hash) + #data in our header stringified
                      str(self.data) +
                      str(self.timestamp))

        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode() #first layer of encry
        outer_hash = hashlib.sha256(inner_hash).hexdigest() #run inner hash in outer hash
        return outer_hash #hash value thats run twice. created a block. assigned data. time stamped.
                          # will show tampering