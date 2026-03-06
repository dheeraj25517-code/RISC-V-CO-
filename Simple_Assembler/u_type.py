from ISA_Data import ISA, REGISTERS

def encode_u(mnemonic,rd_name,imm): #imm= immediate instruction
    #Converts an U-type instruction into its 32-bit binary string
    #for eg. lui rd, immediate
    try:   
        op=ISA[mnemonic]['opcode']
    
        rd=REGISTERS[rd_name]
        val=int(imm) 

        imm_bin=bin(val & 0xFFFFF)[2:].zfill(20) #Converting to 2's complement
         
        binary_string = imm_bin + rd+ op  # Total 20+5+7 =32 bits  #Final binary instruction
        return binary_string

    except KeyError as e:
        return f"Error: Unknown mnemonic or register: {e}"
    
    

#print(encode_u("lui","rd",15))
