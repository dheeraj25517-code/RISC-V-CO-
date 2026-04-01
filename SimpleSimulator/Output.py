def dump_simulator_state(registers, pc, memory, filename="simulation_output.txt"):
    try:
        with open(filename, "w") as f:
            f.write("="*45 + "\n")
            f.write("RISC-V SIMULATOR FINAL STATE\n")
            f.write("="*45 + "\n\n")

            f.write(f"Final PC Value: 0x{pc:08x}\n\n")

            f.write("--- Register File (Hex and Signed Decimal) ---\n")
            for i in range(32):
                reg_val = registers[i]
                hex_val = f"0x{reg_val & 0xFFFFFFFF:08x}"
                f.write(f"x{i:02d}: {hex_val:<10} ({reg_val:>11d})")
                
                if (i + 1) % 2 == 0:
                    f.write("\n")
                else:
                    f.write("    |    ")

            f.write("\n--- Memory Content (Non-Zero Only) ---\n")
            if not memory:
                f.write("Memory is empty/no writes occurred.\n")
            else:
                sorted_addresses = sorted(memory.keys())
                has_data = False
                for addr in sorted_addresses:
                    val = memory[addr]
                    if val != 0:
                        f.write(f"Address [0x{addr:08x}] : 0x{val & 0xFFFFFFFF:08x} ({val})\n")
                        has_data = True
                if not has_data:
                    f.write("All initialized memory addresses contain zero.\n")

            f.write("\n" + "="*45 + "\n")
            f.write("END OF SIMULATION REPORT\n")
            f.write("="*45 + "\n")
            
        print(f"Simulation state successfully saved to {filename}")
        
    except IOError as e:
        print(f"Error: Could not write to file. {e}")

if __name__ == "__main__":
    regs=[0]*32
    regs[1]=100
    regs[2]=-50
    regs[10]=0xABC
    
    mem={0x1000: 0xFF, 0x1004: 0xDEADBEEF}
    current_pc=0x00000044
    
    dump_simulator_state(regs, current_pc, mem, "riscv_results.txt")
