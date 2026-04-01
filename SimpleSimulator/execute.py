def execute(decode,register,pc,memory):
    def to_signed_32(val):
        val = val & 0xFFFFFFFF
        if val & 0x80000000:
            return val - 0x100000000
        return val
    register[0] = 0
    new_pc=pc+4 
    result=None
    
    op=decode.get("op")
    ins_type=decode.get("type")
    if ins_type=="R":
        rs_1=register[decode["rs1"]]
        rs_2=register[decode["rs2"]]
        if op=="add":result=to_signed_32(rs_1+rs_2)
        elif op=="sub":result=to_signed_32(rs_1-rs_2)
        elif op=="sll":result=to_signed_32(rs_1<<(rs_2 & 0x1F))
        elif op=="slt":result=1 if rs_1<rs_2 else 0
        elif op=="sltu":result=1 if (rs_1 & 0xFFFFFFFF) <(rs_2 & 0xFFFFFFFF) else 0
        elif op=="xor":result = to_signed_32(rs_1^rs_2)
        elif op == "srl":result = to_signed_32((rs_1& 0xFFFFFFFF)>> (rs_2 & 0x1F))
        elif op == "sra":result = to_signed_32(rs_1>>(rs_2& 0x1F))
        elif op == "or":result = to_signed_32(rs_1|rs_2)
        elif op =="and":result = to_signed_32(rs_1&rs_2)
        
        if result is not None:
            register[decode["rd"]] = to_signed_32(result)

    elif ins_type=="I":
        rs_1=register[decode["rs1"]]
        imm=decode.get("imm",0)
        
        if op=="addi":result=to_signed_32(rs_1+imm)
        elif op=="slti":result =1 if rs_1<imm else 0
        elif op=="sltiu":result =1 if (rs_1 & 0xFFFFFFFF)<(imm & 0xFFFFFFFF) else 0
        elif op=="xori":result =to_signed_32(rs_1^ imm)
        elif op=="ori":result =to_signed_32(rs_1| imm)
        elif op=="andi":result =to_signed_32(rs_1& imm)
        elif op=="slli":result =to_signed_32(rs_1 << (imm &0x1F))
        elif op=="srli":result =to_signed_32((rs_1 & 0xFFFFFFFF)>> (imm &0x1F))
        elif op=="srai":result =to_signed_32(rs_1 >> (imm &0x1F))
        elif op=="jalr":
            result=to_signed_32(pc+4)
            new_pc=(rs_1+imm)& ~1
        elif op=="lw":
            addr=rs_1+imm
            result=memory.get(addr, 0) 
        
        if result is not None:
            register[decode["rd"]] = to_signed_32(result)

    