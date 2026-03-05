# RISC-V-CO-
CO Assignment

1)essentials_(Assembler).txt- by Dheeraj 
The information regarding the instructions were stored originally in a text file "essentials_(Assembler).txt"

2)ISA_Data.py- by Dheeraj 
The instructions were then retrieved and stored as dictionaries along with ABI names in this format with the help of the code in ISA_Data.py 
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


3)R-type: by Dheeraj
Converts an R-type instruction into its 32-bit binary string (Example: add x1, x2, x3)

4)B-type: by Rudra
Converts an B-type instruction into its 32-bit binary string (Example: blt rs1, rs2, imm[12:1])

5)I-type: by Shubh
Converts an R-type instruction into its 32-bit binary string (Example: addi,x1,x2,10)

6)J-type: by Shubh
Converts an J-type instruction into its 32-bit binary string (Example: jal,x1,-1024)

7)U-type: by Rudra
Converts an U-type instruction into its 32-bit binary string (Example: lui,rd,15)

8)S-type: by Shivam
Converts an S-type instruction into its 32-bit binary string (Example: sw,ra,32(sp))

9)Read_me.md by Shivam 
The types here take in string input and gives a 32 bit.
