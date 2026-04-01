def sign_extend(bit_str, length):
    val = int(bit_str, 2)
    if bit_str[0] == '1':
        return val - (1 << length)
    return val


def decode(instr_bin, ISA):
    if len(instr_bin) != 32:
        return {"type": "Error", "msg": "Invalid instruction length"}

    opcode = instr_bin[25:32]
    rd = int(instr_bin[20:25], 2)
    funct3 = instr_bin[17:20]
    rs1 = int(instr_bin[12:17], 2)
    rs2 = int(instr_bin[7:12], 2)
    funct7 = instr_bin[0:7]

    for name, info in ISA.items():
        if info["opcode"] != opcode:
            continue

        t = info["type"]

        if t == "R":
            if info["funct3"] == funct3 and info["funct7"] == funct7:
                return {"type": "R", "op": name, "rd": rd, "rs1": rs1, "rs2": rs2}

        elif t == "I":
            if info["funct3"] == funct3:
                if "funct7" in info:
                    if info["funct7"] != funct7:
                        continue
                    imm = int(instr_bin[7:12], 2)
                else:
                    imm = sign_extend(instr_bin[0:12], 12)

                return {"type": "I", "op": name, "rd": rd, "rs1": rs1, "imm": imm}

        elif t == "S":
            if info["funct3"] == funct3:
                imm = sign_extend(instr_bin[0:7] + instr_bin[20:25], 12)
                return {"type": "S", "op": name, "rs1": rs1, "rs2": rs2, "imm": imm}

        elif t == "B":
            if info["funct3"] == funct3:
                imm = sign_extend(
                    instr_bin[0] +
                    instr_bin[24] +
                    instr_bin[1:7] +
                    instr_bin[20:24] +
                    "0", 13
                )
                return {"type": "B", "op": name, "rs1": rs1, "rs2": rs2, "imm": imm}

        elif t == "U":
            imm = int(instr_bin[0:20], 2) << 12
            if imm >= 0x80000000:
                imm -= (1 << 32)
            return {"type": "U", "op": name, "rd": rd, "imm": imm}

        elif t == "J":
            imm = sign_extend(
                instr_bin[0] +
                instr_bin[12:20] +
                instr_bin[11] +
                instr_bin[1:11] +
                "0", 21
            )
            return {"type": "J", "op": name, "rd": rd, "imm": imm}

    return {"type": "Unknown"}