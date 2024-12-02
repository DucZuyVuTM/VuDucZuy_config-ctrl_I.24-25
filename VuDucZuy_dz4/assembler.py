# assembler.py
import sys
import yaml

def load_constant(A, B, C):
    command = (A & 0x1F) | ((B & 0xFFFFF) << 5) | ((C & 0x7F) << 21)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def read_memory(A, B, C, D):
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3FF) << 12) | ((D & 0x7F) << 22)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def write_memory(A, B, C, D):
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3F) << 12) | ((D & 0xFFF) << 19)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def multiply(A, B, C, D):
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3F) << 12) | ((D & 0xFFFFFFFFFFFF) << 19)
    return [(command >> (8 * i)) & 0xFF for i in range(7)]

# Đọc chương trình và mã hóa nó
def assemble(input_file, output_file):
    with open(input_file, "r") as asm_file:
        lines = asm_file.readlines()
        
    binary = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        opcode = parts[0]
        params = list(map(int, parts[1].split(',')))
        
        if opcode == "LOAD_CONST":
            binary.extend(load_constant(*params))
        elif opcode == "READ_MEM":
            binary.extend(read_memory(*params))
        elif opcode == "WRITE_MEM":
            binary.extend(write_memory(*params))
        elif opcode == "MULTIPLY":
            binary.extend(multiply(*params))
        else:
            raise ValueError(f"Unknown instruction: {opcode}")

    with open(output_file, "wb") as bin_file:
        print(f"Binary: {binary}")
        bin_file.write(bytes(binary))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 assembler.py <input.asm> <output.bin>")
        sys.exit(1)

    assemble(sys.argv[1], sys.argv[2])
