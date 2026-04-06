
def execute(decoded, registers, pc, memory):

    def to_signed_32(val):
        val = val & 0xFFFFFFFF
        if val & 0x80000000:
            return val - 0x100000000
        return val

    registers[0] = 0
    new_pc = pc + 4
    result = None

    op = decoded.get("op")
    ins_type = decoded.get("type")

    # ================= R TYPE =================
    if ins_type == "R":

        rs1 = registers[decoded["rs1"]]
        rs2 = registers[decoded["rs2"]]
        rd = decoded["rd"]

        if op == "add":
            result = rs1 + rs2
        elif op == "sub":
            result = rs1 - rs2
        elif op == "sll":
            result = rs1 << (rs2 & 0x1F)
        elif op == "slt":
            result = 1 if rs1 < rs2 else 0
        elif op == "sltu":
            result = 1 if (rs1 & 0xFFFFFFFF) < (rs2 & 0xFFFFFFFF) else 0
        elif op == "xor":
            result = rs1 ^ rs2
        elif op == "srl":
            result = (rs1 & 0xFFFFFFFF) >> (rs2 & 0x1F)
        elif op == "sra":
            result = rs1 >> (rs2 & 0x1F)
        elif op == "or":
            result = rs1 | rs2
        elif op == "and":
            result = rs1 & rs2

        if result is not None:
            registers[rd] = to_signed_32(result)

    # ================= I TYPE =================
    elif ins_type == "I":

        rs1 = registers[decoded["rs1"]]
        rd = decoded["rd"]
        imm = decoded.get("imm", 0)

        if op == "addi":
            result = rs1 + imm
        elif op == "slti":
            result = 1 if rs1 < imm else 0
        elif op == "sltiu":
            result = 1 if (rs1 & 0xFFFFFFFF) < (imm & 0xFFFFFFFF) else 0
        elif op == "xori":
            result = rs1 ^ imm
        elif op == "ori":
            result = rs1 | imm
        elif op == "andi":
            result = rs1 & imm
        elif op == "slli":
            result = rs1 << (imm & 0x1F)
        elif op == "srli":
            result = (rs1 & 0xFFFFFFFF) >> (imm & 0x1F)
        elif op == "srai":
            result = rs1 >> (imm & 0x1F)

        elif op == "lw":
            addr = rs1 + imm
            result = memory.read_memory(addr, 4)

        elif op == "jalr":
            result = pc + 4
            new_pc = (rs1 + imm) & ~1

        if result is not None:
            registers[rd] = to_signed_32(result)

    # ================= S TYPE =================
    elif ins_type == "S":

        rs1 = registers[decoded["rs1"]]
        rs2 = registers[decoded["rs2"]]
        imm = decoded.get("imm", 0)

        if op == "sw":
            addr = rs1 + imm
            memory.write_memory(addr, rs2, 4)

    # ================= B TYPE =================
    elif ins_type == "B":

        rs1 = registers[decoded["rs1"]]
        rs2 = registers[decoded["rs2"]]
        imm = decoded.get("imm", 0)

        take = False

        if op == "beq":
            take = rs1 == rs2
        elif op == "bne":
            take = rs1 != rs2
        elif op == "blt":
            take = rs1 < rs2
        elif op == "bge":
            take = rs1 >= rs2
        elif op == "bltu":
            take = (rs1 & 0xFFFFFFFF) < (rs2 & 0xFFFFFFFF)
        elif op == "bgeu":
            take = (rs1 & 0xFFFFFFFF) >= (rs2 & 0xFFFFFFFF)

        if take:
            new_pc = pc + imm

    # ================= U TYPE =================
    elif ins_type == "U":

        rd = decoded["rd"]
        imm = decoded.get("imm", 0)

        if op == "lui":
            registers[rd] = to_signed_32(imm)

        elif op == "auipc":
            registers[rd] = to_signed_32(pc + imm)

    # ================= J TYPE =================
    elif ins_type == "J":

        rd = decoded["rd"]
        imm = decoded.get("imm", 0)

        if op == "jal":
            registers[rd] = to_signed_32(pc + 4)
            new_pc = pc + imm

    registers[0] = 0
    return new_pc
