import sys
from ISA_Data import ISA, REGISTERS
from b_type import encode_b
from i_type import encode_i
from r_type import encode_r
from s_type import encode_s
from u_type import encode_u
from j_type import encode_j

def pass_1(lines):
    symbol_table={}
    pc=0
    clean_instructions=[]
    for i, line in enumerate(lines):
        line = line.split('#')[0].strip()
        if not line:
            continue
        if ":" in line:
            label_part,_,instruction_part = line.partition(":")
            label_name = label_part.strip()
            if label_name in symbol_table:
                print(f"Error at line {i+1}: Duplicate label '{label_name}'")
                return None,None
            
            #Error Check
            if " " in label_part.strip():
                 print(f"Error at line {i+1}: Invalid label format (spaces in name)")
                 return None,None

            #Mapping labels
            symbol_table[label_name]=pc
            
            #Checking for an instruction on the same line
            instr=instruction_part.strip()
            if instr:
                clean_instructions.append(instr)
                pc+=4
        else:
            clean_instructions.append(line)
            pc += 4
    return symbol_table,clean_instructions


def pass_2(clean_lines,symbol_table):
    output_binary=[]
    current_pc=0

    for i, line in enumerate(clean_lines):
        parts=line.replace(",", " ").split()
        mnemonic=parts[0]

        instr_type=ISA[mnemonic]['type']

        if instr_type=="R":
            rd, rs1, rs2 = parts[1], parts[2], parts[3]

            if rd not in REGISTERS or rs1 not in REGISTERS or rs2 not in REGISTERS:
                print(f"Error at line {i+1}: Invalid register")
                exit()

            binary=encode_r(mnemonic, rd, rs1, rs2)
            output_binary.append(binary)

        elif instr_type=="I":
            if "(" in parts[2]:
                rd = parts[1]
                imm_str, rs1_part = parts[2].split("(")
                rs1 = rs1_part.replace(")", "")
                imm = int(imm_str)
            else:

                rd, rs1, imm = parts[1], parts[2], int(parts[3])

            if not (-2048<=imm<=2047):
                print(f"Error at line {i+1}: Immediate value {imm} out of range")
                exit()
            binary = encode_i(mnemonic, rd, rs1, imm)
            output_binary.append(binary)

        elif instr_type=="S":
            rs2 = parts[1]
            imm_str,rs1_str=parts[2].replace(")", "").split("(")
            rs1,imm=rs1_str,int(imm_str)
            
            binary=encode_s(mnemonic,rs1,rs2,imm)
            output_binary.append(binary)

        elif instr_type == "B":
            rs1,rs2,label_name=parts[1],parts[2],parts[3]

            if rs1 not in REGISTERS or rs2 not in REGISTERS:
                print(f"Error at line {i+1}: Invalid register")
                exit()

            if label_name.isdigit() or (label_name.startswith('-') and label_name[1:].isdigit()):
                offset = int(label_name)
            elif label_name in symbol_table:
                target_pc = symbol_table[label_name]
                offset = target_pc - current_pc
            else:
                print(f"Error at line {i+1}: Undefined label '{label_name}'")
                exit()
            if not (-4096 <= offset <= 4094):
                print(f"Error at line {i+1}: Branch offset {offset} out of range")
                exit()
            binary = encode_b(mnemonic, rs1, rs2, offset)
            output_binary.append(binary)

        elif instr_type == "U":
            rd, imm = parts[1], int(parts[2])

            if rd not in REGISTERS:
                print(f"Error at line {i+1}: Invalid register")
                exit()

            binary=encode_u(mnemonic,rd,imm)
            output_binary.append(binary)

        elif instr_type == "J":
            rd, label_name = parts[1], parts[2]
            if rd not in REGISTERS:
                print(f"Error at line {i+1}: Invalid register '{rd}'")
                exit()
            if label_name.isdigit() or (label_name.startswith('-') and label_name[1:].isdigit()):
                offset = int(label_name)
            elif label_name in symbol_table:
                target_pc = symbol_table[label_name]
                offset = target_pc - current_pc
            else:
                print(f"Error at line {i+1}: Undefined label '{label_name}'")
                exit()
            if not (-1048576 <= offset <= 1048574):
                print(f"Error at line {i+1}: Jump offset {offset} out of range")
                exit()

            binary = encode_j(mnemonic, rd, offset)
            output_binary.append(binary)

        else:
            print(f"Error at line {i+1}: Unknown instruction '{mnemonic}'")
            exit()

        current_pc += 4

    last = clean_lines[-1].replace(",", " ").split()
    if not (last[0] == "beq" and last[1] == "zero" and last[2] == "zero"):
        print("Error: Missing virtual halt instruction")
        exit()

    return output_binary



def main():
    if len(sys.argv) < 3:
        print("Error: Please provide input and output file names.")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
            
        print(f"Reading from: {input_path}")

        
        symbol_table, clean_lines = pass_1(lines)
        if symbol_table is None:
            return

     
        binary_output = pass_2(clean_lines, symbol_table)

        # the results to the output file
        with open(output_path, 'w') as f:
            for line in binary_output:
                f.write(line + '\n')
        
        print(f"Success! Output saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Could not find file '{input_path}'")
        
    print(f"Reading from: {input_path}")
    #pass_1 and pass_2 are called here 
if __name__ == "__main__":
    main()