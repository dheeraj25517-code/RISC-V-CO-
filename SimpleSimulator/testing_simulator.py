from Base import Base

def test_simulator_state():
    # 1. Initialize
    state = Base()
    print("--- Testing Initialization ---")
    print(f"Initial PC: {state.get_pc()}")
    
    # 2. Test Register x0 (Hardwired to 0)
    print("\n--- Testing x0 Protection ---")
    state.set_register(0, 500)
    print(f"Value in x0 after trying to set 500: {state.get_register(0)} (Should be 0)")

    # 3. Test General Registers & 32-bit Masking
    print("\n--- Testing Registers & Overflow ---")
    state.set_register(1, 100)
    state.set_register(2, 0xFFFFFFFF + 1) # Should wrap to 0
    print(f"x1: {state.get_register(1)} (Should be 100)")
    print(f"x2 (Overflow test): {state.get_register(2)} (Should be 0)")

    # 4. Test Memory (Little-Endian)
    print("\n--- Testing Memory (Little-Endian) ---")
    # Store the value 0x12345678 at address 100
    # In Little-Endian: [78, 56, 34, 12]
    state.write_memory(100, 0x12345678)
    val = state.read_memory(100)
    print(f"Value read from address 100: {hex(val)} (Should be 0x12345678)")
    print(f"Raw byte at addr 100: {hex(state.memory[100])} (Should be 0x78)")

    # 5. Test PC Updates
    print("\n--- Testing PC ---")
    state.set_pc(4096)
    state.increment_pc()
    print(f"PC after set(4096) and increment: {state.get_pc()} (Should be 4100)")

    # 6. Test Grader Output Format
    print("\n--- Final Grader State Dump ---")
    print(state.dump_state())

if __name__ == "__main__":
    test_simulator_state()
