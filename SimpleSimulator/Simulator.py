from Base import Base
from Decoder import decode
from Execute import execute
from ISA_Data import ISA


def load_instructions(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                instructions.append(line)
    return instructions


def run_simulator(input_file, output_file):
    cpu = Base()
    instructions = load_instructions(input_file)
    # load instructions into memory
    for i, instr in enumerate(instructions):
        value = int(instr, 2)
        addr = i * 4
        cpu.memory[addr] = value & 0xff
        cpu.memory[addr + 1] = (value >> 8) & 0xff
        cpu.memory[addr + 2] = (value >> 16) & 0xff
        cpu.memory[addr + 3] = (value >> 24) & 0xff
    max_steps = 10000
    steps = 0
    with open(output_file, "w") as out:
        while steps < max_steps:
            pc = cpu.get_pc()
            instr_val = cpu.read_memory(pc, 4)
            instr_bin = format(instr_val, "032b")
            
            decoded = decode(instr_bin, ISA)
            if decoded.get("type") in ["Error", "Unknown"]:
                break
            new_pc = execute(decoded, cpu.registers, pc, cpu)
            cpu.registers[0] = 0
            cpu.set_pc(new_pc)
            pc_bin = f"0b{cpu.get_pc():032b}"
            regs = [f"0b{(r & 0xffffffff):032b}" for r in cpu.registers]
            out.write(" ".join([pc_bin] + regs) + "\n")
            if instr_bin == "00000000000000000000000001100011":
                break
            steps += 1
        print("steps=",steps)
        for addr in range(0x10000, 0x10080, 4):
            val = cpu.read_memory(addr, 4)
            out.write(f"0x{addr:08X}:0b{val:032b}\n")


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        print("Usage: python Simulator.py <input_file> <output_file>")
        exit(1)

    run_simulator(sys.argv[1], sys.argv[2])
