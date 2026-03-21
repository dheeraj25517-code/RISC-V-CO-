from ISA_Data import ISA, REGISTERS

def encode_b(mnemonic,rs1_name, rs2_name,imm):
         #Converts an B-type instruction into its 32-bit binary string
         # for eg. - (blt rs1, rs2, imm[12:1])
    try:

        
        f3=ISA[mnemonic]['func3']
        op=ISA[mnemonic]['opcode']
        
        
        rs1=REGISTERS[rs1_name]
        rs2=REGISTERS[rs2_name]

        val=int(imm) 

        imm_bin=bin(val & 0x1FFF)[2:].zfill(13) 
        
        binary_string = imm_bin[0]+imm_bin[2:8]+rs2+rs1+f3+imm_bin[8:12]+imm_bin[1]+op  # Total=7+5+5+3+5+7=32 bits
        return binary_string

    except KeyError as e:
        return f"Error: Unknown mnemonic or register: {e}"
    
    

#print(encode_b("blt","a4","a5",200))
