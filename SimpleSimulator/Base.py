class Base:
    def __init__(self, memory_size = 0x20000):
        self.registers = [0] * 32
        self.registers[2] = 0x0000017C
        self.pc = 0
        self.memory = bytearray(memory_size)
        
    def get_register(self, reg_idx):
        if 0 <= reg_idx < 32:
            return self.registers[reg_idx]
        return 0

    def set_register(self, reg_idx, value):
        if reg_idx == 0:
            return
        if 0 <= reg_idx < 32:
            self.registers[reg_idx] = value & 0xFFFFFFFF
            
    def get_pc(self):
        return self.pc
        
    def set_pc(self, value):
        self.pc = value
        
    def increment_pc(self, offset=4):
        self.pc += offset

    def read_memory(self, address, num_bytes=4):
        val = 0
        for i in range(num_bytes):
            val |= (self.memory[address + i] << (8 * i))
        return val

    def write_memory(self, address, value, num_bytes=4):
        for i in range(num_bytes):
            self.memory[address + i] = (value >> (8 * i)) & 0xFF

    def dump_state(self):
        pc_bin = f"0b{self.get_pc():032b}"
        reg_bins = [f"0b{(r & 0xffffffff):032b}" for r in self.registers]
        return f"{pc_bin} {' '.join(reg_bins)}"
