from ISA_Data import ISA, REGISTERS

def encode_j(mnemonic, rd_name,imm_inst):        #imm_inst=immediate instructions
    try:
        op=ISA[mnemonic]['opcode']
        
        rd=REGISTERS[rd_name]
        val=int(imm_inst) 
        imm_bin=bin(val & 0x1FFFFF)[2:].zfill(21)           #get 2's complement
        bit_20=imm_bin[0]                                   # imm[20]
        bits_10=imm_bin[10:20]                              # imm[10:1]
        bit_11=imm_bin[9]                                   # imm[11]
        bits_19=imm_bin[1:9]                                # imm[19:12]
        final_imm=f"{bit_20}{bits_10}{bit_11}{bits_19}"
        binary_string=f"{final_imm}{rd}{op}"                       #total bit=20+5+7=32
        return binary_string

    except KeyError as e:
        return f"Error: Unknown mnemonic or register: {e}"
    
    


#print(encode_r("jal","x1",-1024))
