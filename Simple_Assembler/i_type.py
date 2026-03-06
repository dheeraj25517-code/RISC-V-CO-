from ISA_Data import ISA, REGISTERS

def encode_i(mnemonic, rd_name, rs1_name,imm_inst):        #imm_inst=immediate instructions
    try:
        f3=ISA[mnemonic]['func3']
        op=ISA[mnemonic]['opcode']
        
        rd=REGISTERS[rd_name]
        rs1=REGISTERS[rs1_name]
        val=int(imm_inst) 
        imm_bin=bin(val & 0xFFF)[2:].zfill(12)           #get 2's complement
        binary_string=f"{imm_bin}{rs1}{f3}{rd}{op}"               #total bit=12+5+3+5+7=32
        return binary_string

    except KeyError as e:
        return f"Error: Unknown mnemonic or register: {e}"
    
    


#print(encode_i("addi","x1","x2","10"))

