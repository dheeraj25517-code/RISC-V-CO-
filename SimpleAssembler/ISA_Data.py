def ISA_initializer(f_path):
    ISA={}
    with open(f_path, 'r') as f:
        for l in f:
            d_parts=[p.strip() for p in l.split('|') if p.strip()]
            if (not d_parts or len(d_parts)<3):
                continue
            ins_type=d_parts[0]
            name=d_parts[-1]

            ISA[name]={"type": ins_type}
            if (ins_type=='R'):
                ISA[name].update({"func7":d_parts[1],"func3":d_parts[4],"opcode":d_parts[6]})
            elif (ins_type=='B'):
                ISA[name].update({"func3":d_parts[5],"opcode":d_parts[8]})
            elif (ins_type=='J'):
                ISA[name].update({"opcode":d_parts[6]})
            elif (ins_type=='I'):
                ISA[name].update({"func3":d_parts[3],"opcode":d_parts[5]})
            elif (ins_type=='S'):
                ISA[name].update({"func3":d_parts[4],"opcode":d_parts[6]})
            elif (ins_type=='U'):
                ISA[name].update({"opcode":d_parts[3]})
        return ISA
def register_mapping():#The register_map acts as a translator that instantly turns human-friendly names like x10 or a0 into the exact 5-bit binary strings required to build a machine-code instruction.
    reg_map={f"x{i}": format(i, '05b') for i in range(32)}#converts integer i into binary and makes the string 5 character long
    abi_names={ 
        'zero': 0, 'ra': 1, 'sp': 2, 'gp': 3, 'tp': 4, 't0': 5, 't1': 6, 't2': 7,
        's0': 8, 'fp': 8, 's1': 9, 'a0': 10, 'a1': 11, 'a2': 12, 'a3': 13, 
        'a4': 14, 'a5': 15, 'a6': 16, 'a7': 17, 's2': 18, 's3': 19, 's4': 20, 
        's5': 21, 's6': 22, 's7': 23, 's8': 24, 's9': 25, 's10': 26, 's11': 27,
        't3': 28, 't4': 29, 't5': 30, 't6': 31
    }
    for name, index in abi_names.items():
        reg_map[name] = format(index, '05b')

    return reg_map

inp=r"C:\Users\DHEERAJ KUMAR THOTA\Desktop\Academics\CO\co_2026_evaluation_framework_release\SimpleAssembler\essentials_(Assember).txt"
REGISTERS=register_mapping()# Global variable
ISA=ISA_initializer(inp)
"""structure of the dictionary is like this  {'add': {'type': 'R', 'func7': '0000000', 'func3': '000', 'opcode': '0110011'},
'sub': {'type': 'R', 'func7': '0100000', 'func3': '000', 'opcode': '0110011'}, 'sll': {'type': 'R', 'func7': '0000000', 'func3': '001', 'opcode': '0110011'},
'slt': {'type': 'R', 'func7': '0000000', 'func3': '010', 'opcode': '0110011'},
'sltu': {'type': 'R', 'func7': '0000000', 'func3': '011', 'opcode': '0110011'},
'xor': {'type': 'R', 'func7': '0000000', 'func3': '100', 'opcode': '0110011'},
'srl': {'type': 'R', 'func7': '0000000', 'func3': '101', 'opcode': '0110011'},
'sra': {'type': 'R', 'func7': '0100000', 'func3': '101', 'opcode': '0110011'},
'or': {'type': 'R', 'func7': '0000000', 'func3': '110', 'opcode': '0110011'},
'and': {'type': 'R', 'func7': '0000000', 'func3': '111', 'opcode': '0110011'},
'addi': {'type': 'I', 'func3': '000', 'opcode': '0010011'},
'slti': {'type': 'I', 'func3': '010', 'opcode': '0010011'},
'sltiu': {'type': 'I', 'func3': '011', 'opcode': '0010011'},
'xori': {'type': 'I', 'func3': '100', 'opcode': '0010011'},
'ori': {'type': 'I', 'func3': '110', 'opcode': '0010011'},
'andi': {'type': 'I', 'func3': '111', 'opcode': '0010011'},
'lw': {'type': 'I', 'func3': '010', 'opcode': '0000011'},
'jalr': {'type': 'I', 'func3': '000', 'opcode': '1100111'},
'sb': {'type': 'S', 'func3': '000', 'opcode': '0100011'},
'sh': {'type': 'S', 'func3': '001', 'opcode': '0100011'},
'sw': {'type': 'S', 'func3': '010', 'opcode': '0100011'},
'beq': {'type': 'B', 'func3': '000', 'opcode': '1100011'},
'bne': {'type': 'B', 'func3': '001', 'opcode': '1100011'},
'blt': {'type': 'B', 'func3': '100', 'opcode': '1100011'},
'bge': {'type': 'B', 'func3': '101', 'opcode': '1100011'},
'bltu': {'type': 'B', 'func3': '110', 'opcode': '1100011'},
'bgeu': {'type': 'B', 'func3': '111', 'opcode': '1100011'},
'lui': {'type': 'U', 'opcode': '0110111'},
'auipc': {'type': 'U', 'opcode': '0010111'},
'jal': {'type': 'J', 'opcode': '1101111'}}"""


"""the structure of reg_map would look like this {
    'x0':  '00000',
    'x1':  '00001',
    'x2':  '00010',
    'x3':  '00011',
    'x4':  '00100',
    'x5':  '00101',
    'x6':  '00110',
    'x7':  '00111',
    'x8':  '01000',
    'x9':  '01001',
    'x10': '01010',  # Common for a0
    'x11': '01011',  # Common for a1
    ...
    'x30': '11110',
    'x31': '11111'
}"""



