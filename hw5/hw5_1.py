init_mem={} # Empty memory at the very beginning
a={800: 123} # 1st data with address 800 and value 123
b={900: 1000} # 2nd data with address 900 and value 1000

def store(storage,elm): # Store an element to the memory
    storage.update(elm)
    return storage

mem=store(init_mem, a) # mem = {800: 123}
mem=store(mem, b) # mem = {800: 123, 900: 1000}

c={800:900}
mem=store(mem, c) # mem = {800: 900, 900: 1000}

d={1500:700}
mem=store(mem, d) # mem = {800: 900, 900: 1000, 1500: 700}
print("mem:", mem)

def imm_load_ac(val): # Load accumulator(ac) by immediate addressing
    return val
ac = imm_load_ac(800) # ac = 800
print("Accumulator (immediate addressing):", ac)

def dir_load_ac(storage, val): # Load accumulator(ac) by direct addressing
    return storage[val]
ac = dir_load_ac(mem, 800) # ac = 900
print("Accumulator (direct addressing):", ac)

def indir_load_ac(storage, val): # Load accumulator(ac) by indirect addressing
    return storage[storage[val]]
ac = indir_load_ac(mem, 800) # ac = 1000
print("Accumulator (indirect addressing):", ac)

def idx_load_ac(storage, idx, val): # Load accumulator(ac) by Indexed addressing
    return storage[idx+val]
idxreg=700
ac=idx_load_ac(mem, idxreg, 800) # ac = 700
print("Accumulator (indexed addressing):", ac)