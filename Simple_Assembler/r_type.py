from ISA_Data import ISA, REGISTERS


def encode_r(mnemonic, rd_name, rs1_name, rs2_name):#Converts an R-type instruction into its 32-bit binary string (Example: add x1, x2, x3)
    try:
        #Look up the bit patterns for this specific instruction from ISA dictionary
        #These come from your essentials_(Assembler).txt file which is the read me file 
        f7=ISA[mnemonic]['func7']
        f3=ISA[mnemonic]['func3']
        op=ISA[mnemonic]['opcode']
        #Convert register names to 5-bit strings using your reg_map which is the REGISTERS function in ISA_Data
        rd=REGISTERS[rd_name]
        rs1=REGISTERS[rs1_name]
        rs2=REGISTERS[rs2_name]
        binary_string = f7+rs2+rs1+f3+rd+op
        return binary_string

    except KeyError as e:
        return f"Error: Unknown mnemonic or register: {e}"
    
    

#print(encode_r("add","x1","x2","x3"))
