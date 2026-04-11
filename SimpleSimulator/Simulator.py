import sys
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
    # Load instructions into memory
    for i, instr in enumerate(instructions):
        value = int(instr, 2)
        addr = i * 4
        cpu.memory[addr] = value & 0xFF
        cpu.memory[addr + 1] = (value >> 8) & 0xFF
        cpu.memory[addr + 2] = (value >> 16) & 0xFF
        cpu.memory[addr + 3] = (value >> 24) & 0xFF

    max_steps = 10000
    steps = 0
    trace_output = []
    try:
        while steps < max_steps:

                pc = cpu.get_pc()
                # Fetch instruction
                instr_val = cpu.read_memory(pc, 4)
                instr_bin = format(instr_val, "032b")
                # Decode
                decoded = decode(instr_bin, ISA)
                if decoded.get("type") in ["Error", "Unknown"]:
                    raise RuntimeError("Invalid instruction encountered")
                #print("PC: ",pc)
                # Execute
                new_pc = execute(decoded, cpu.registers, pc, cpu)

                cpu.registers[0] = 0
                cpu.set_pc(new_pc)
                # Write trace
                pc_bin = f"0b{cpu.get_pc():032b}"
                regs = [f"0b{(r & 0xFFFFFFFF):032b}" for r in cpu.registers]
                out.write(" ".join([pc_bin] + regs) + "\n")
                #print(decoded)
                print("PC: ",pc)
                trace_output.append(" ".join([pc_bin] + regs))
                if decoded["type"] == "B" and decoded["op"] == "beq" and int(decoded["rs1"]) == 0 and int(decoded["rs2"]) == 0 and decoded["imm"] == 0:
                    break
                steps += 1

    except IndexError as e:
        print("Simulation terminated due to error:", e)
        return

    except RuntimeError as e:
        print("Simulation terminated due to error:", e)
        return

    # Only write file if execution completed successfully
    with open(output_file, "w") as out:
        for line in trace_output:
            out.write(line + "\n")
        # Memory dump
        for addr in range(0x10000, 0x10080, 4):
            val = cpu.read_memory(addr, 4)
            out.write(f"0x{addr:08X}:0b{val:032b}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python Simulator.py <input_file> <output_file>")
        exit(1)

    run_simulator(sys.argv[1], sys.argv[2])
