init_mem={}

a={"00000110101000":[0,1,2,3,4,5,6,7]}

def store(storage, elm):
    storage.update(elm)
    return storage

# print mem, separated line by line
# this function is used to make the result looks prettier
def print_mem(storage):
    print("mem={", end="")
    for k, v in storage.items():
        print("'",k,"'",":", v)
    print("}")

mem=store(init_mem, a) # mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7]}

b={"00001110101000":[10,11,12,13,14,15,16,17]}
mem=store(init_mem, b)
# mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17]}

c={"00011110101000":[20,21,22,23,24,25,26,27]}
mem=store(init_mem, c)
# mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17],
# '00011110101000': [20, 21, 22, 23, 24, 25, 26, 27]}

d={"00111110101000":[30,31,32,33,34,35,36,37]}
mem=store(init_mem, d)
# mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17],
# '00011110101000': [20, 21, 22, 23, 24, 25, 26, 27],
# '00111110101000': [30, 31, 32, 33, 34, 35, 36, 37]}

e={"01111110101000":[40,41,42,43,44,45,46,47]}
mem=store(init_mem, e)
# mem={'00000110101000': [0, 1, 2, 3, 4, 5, 6, 7],
# '00001110101000': [10, 11, 12, 13, 14, 15, 16, 17],
# '00011110101000': [20, 21, 22, 23, 24, 25, 26, 27],
# '00111110101000': [30, 31, 32, 33, 34, 35, 36, 37],
# '01111110101000': [40, 41, 42, 43, 44, 45, 46, 47]}
print_mem(mem)

# Initialize cache
# cache format: key -> block label
# value -> tag(11bits), values of 8 words, valid(1bit)
# Assume that there are only 4 cache lines
cache={"blk0": ["00000000000", [0,0,0,0,0,0,0,0], 0],
"blk1": ["00000000000", [0,0,0,0,0,0,0,0], 0],
"blk2": ["00000000000", [0,0,0,0,0,0,0,0], 0],
"blk3": ["00000000000", [0,0,0,0,0,0,0,0], 0]}
def fully_ass_cache(cache, adr, storage):
    tag = adr[0:11]
    # check if valid bit is 0
    for blk, data in cache.items():
        if (data[2]==0):
            data[0] = tag
            data[1] = mem[adr]
            data[2] = 1
            return cache
    print("One cache line needs to be evicted")
    return cache

# print cache, separated line by line
# this function is used to make the result looks prettier
def print_cache(cache):
    print("cache={", end="")
    for k, v in cache.items():
        print("'",k,"'",":", v[0], ",", v[1])
    print("}")


adr1 = "00000110101000" # hex address: 1A8
cache=fully_ass_cache(cache, adr1, mem)
print_cache(cache)
# cache={'blk0': ['00000110101', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# 'blk1': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# 'blk2': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# 'blk3': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0]}

adr2 = "00001110101000" # hex address: 3A8
cache=fully_ass_cache(cache, adr2, mem)
print_cache(cache)
# cache={'blk0': ['00000110101', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# 'blk1': ['00001110101', [10, 11, 12, 13, 14, 15, 16, 17], 1],
# 'blk2': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0],
# 'blk3': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0]}

adr3 = "00011110101000" # hex address: 7A8
cache=fully_ass_cache(cache, adr3, mem)
print_cache(cache)
# cache={'blk0': ['00000110101', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# 'blk1': ['00001110101', [10, 11, 12, 13, 14, 15, 16, 17], 1],
# 'blk2': ['00011110101', [20, 21, 22, 23, 24, 25, 26, 27], 1],
# 'blk3': ['00000000000', [0, 0, 0, 0, 0, 0, 0, 0], 0]}

adr4 = "00111110101000" # hex address: FA8
cache=fully_ass_cache(cache, adr4, mem)
print_cache(cache)
# cache={'blk0': ['00000110101', [0, 1, 2, 3, 4, 5, 6, 7], 1],
# 'blk1': ['00001110101', [10, 11, 12, 13, 14, 15, 16, 17], 1],
# 'blk2': ['00011110101', [20, 21, 22, 23, 24, 25, 26, 27], 1],
# 'blk3': ['00111110101', [30, 31, 32, 33, 34, 35, 36, 37], 1]}

adr5 = '01111110101110' # hex address: 1FAE
cache=fully_ass_cache(cache, adr5, mem)
# One cache line needs to be evicted