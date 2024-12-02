def load_constant(A, B, C):
    # A (0-4 bits), B (5-20 bits), C (21-27 bits)
    command = (A & 0x1F) | ((B & 0xFFFFF) << 5) | ((C & 0x7F) << 21)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def read_memory(A, B, C, D):
    # A (0-4 bits), B (5-11 bits), C (12-21 bits), D (22-28 bits)
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3FF) << 12) | ((D & 0x7F) << 22)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def write_memory(A, B, C, D):
    # A (0-4 bits), B (5-11 bits), C (12-18 bits), D (19-28 bits)
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3F) << 12) | ((D & 0xFFF) << 19)
    return [(command >> (8 * i)) & 0xFF for i in range(4)]

def multiply(A, B, C, D):
    # A (0-4 bits), B (5-11 bits), C (12-18 bits), D (19-48 bits)
    command = (A & 0x1F) | ((B & 0x7F) << 5) | ((C & 0x3F) << 12) | ((D & 0xFFFFFFFFFFFF) << 19)
    return [(command >> (8 * i)) & 0xFF for i in range(7)]

# Test các hàm
print("Load Constant:", load_constant(23, 140, 82))
print("Read Memory:", read_memory(18, 24, 192, 27))
print("Write Memory:", write_memory(31, 112, 109, 763))
print("Multiply:", multiply(22, 38, 16, 530))
