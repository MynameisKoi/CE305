init_mem={}
# Take memory address as the key and all values in the block as key's value
a={"00000110101010":[0,1,2,3,4,5,6,7]} # change to 00000110101010 which is
# binary 00000110101010 is 1AA in Hex
# "0000011": 7-bit tag;
# "0101": 4-bit block;
# "000": 1st address in the current block
# value = 0 at Address 0000011_0101_000 in main memory
# value = 1 at Address 0000011_0101_001 in main memory
# ... ...
# value = 7 at Address 0000011_0101_111 in main memory
def store(storage, elm):
    storage.update(elm)
    return storage
mem=store(init_mem, a)
print(mem)
# mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7]}

b={"00001110101000":[10,11,12,13,14,15,16,17]}
# bin 00001110101000 is 3A8 in Hex
mem=store(mem, b)
print(mem)
# {'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17]}

# cache link format:
# 1. key -> block label;
# 2. value -> tag(7bits), values of 8 words, valid(1bit)]
cache={"0000": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0001": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0010": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0011": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0100": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0101": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0110": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "0111": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1000": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1001": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1010": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1011": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1100": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1101": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1110": ["0000000", [0,0,0,0,0,0,0,0], 0],
        "1111": ["0000000", [0,0,0,0,0,0,0,0], 0]}

adr1 = "00000110101010" # hex address: 1AA
def dir_map_cache(cache, adr, storage):
    tag = adr[0:7]
    block = adr[7:11]
    # print(block)
    # print(cache[block][2])
    if cache[block][2] == 0:
        # print("Block in the cache is empty")   # used for debug
        cache[block][0] = tag
        cache[block][1] = storage[adr]
        cache[block][2] = 1
        return cache
    else:
        print("Block in the cache is occupied")
        return cache

cache=dir_map_cache(cache, adr1, mem)
print(cache)
# cache
# {'0000': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0001': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0010': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0011': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0100': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0101': ['0000011', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# '0110': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0111': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1000': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1001': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1010': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1011': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1100': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1101': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1110': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1111': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0]}

adr2 = "00001110101010" # hex address: 3AA

cache=dir_map_cache(cache, adr2, mem)
# Block in the cache is occupied

c={"00001110111111":[20,21,22,23,24,25,26,27]}
# bin 00001110111111 is 3BF in Hex
mem=store(mem, c)
print(mem)
# Store block values in c to main memory
# mem
# {'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17],
# '00001110111111': [20, 21, 22, 23, 24, 25, 26, 27]}

adr3 = "00001110111111" # hex address: 3BF
cache=dir_map_cache(cache, adr3, mem)
print(cache)
# cache
# {'0000': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0001': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0010': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0011': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0100': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0101': ['0000011', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# '0110': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '0111': ['0000111', [20, 21, 22, 23, 24, 25, 26, 27], 1],
# '1000': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1001': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1010': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1011': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1100': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1101': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1110': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# '1111': ['0000000', [0, 0, 0, 0, 0, 0, 0, 0], 0]}

def check_cache(cache, adr):
    tag = adr[0:7]
    block = adr[7:11]
    if cache[block][0] == tag:
        print("Hit")
    else:
        print("Miss")
check_cache(cache, adr1) # Check if adr1="00000110101010" is saved in cache or not
# Hit
check_cache(cache, adr2) # Check if adr2="00001110101010" is saved in cache or not
# Miss
check_cache(cache, adr3) # Check if adr3="00001110111111" is saved in cache or not
# Hit