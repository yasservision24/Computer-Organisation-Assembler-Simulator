import sys
# opcode_={"instruction name":["binary of opcode instruction","Type of instruction"]}
opcode={
    "add": "00000",
    "sub": "00001",
    "mov": "00010",     
    "mov": "00011",     
    "ld" : "00100",
    "st" : "00101",
    "mul": "00110",
    "div": "00111",
    "rs" : "01000",
    "ls" : "01001",
    "xor": "01010",
    "or" : "01011",
    "and": "01100",
    "not": "01101", 
    "cmp": "01110",
    "jmp": "01111",
    "jlt": "11100",
    "jgt": "11101",
    "je" : "11111",
    "hlt": "11010",} 
Registers={"000":"0000000000000000",
           "001":"0000000000000000",
           "010":"0000000000000000",
           "011":"0000000000000000",
           "100":"0000000000000000",
           "101":"0000000000000000",
           "110":"0000000000000000",
           "111":"0000000000000000"}

memory_address = {}
for i in range(128):
    bin_str = format(i, '07b')  
    memory_address[bin_str] ="0000000000000000"
    


def decimal_to_binary_7(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(7)

def decimal_to_binary_16(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(16) 

def binary_to_decimal(binary):
    return int(binary, 2)

input = []
for line in sys.stdin:
    line = line.rstrip() 
    words = line.split()
    input.append(words)
memory_address_pointer=0   
for m in input:
    memory_address[decimal_to_binary_7 (memory_address_pointer)]=m[0]
    memory_address_pointer+=1
pc=0
while pc<len(input):
    op=input[pc][0]
    op=op[0:5]
    i=input[pc][0]
    
    
    
    ## Type A
    if op=="00000":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        
        if binary_to_decimal(Registers[reg1])+binary_to_decimal(Registers[reg1])>65535:
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_binary_16(    binary_to_decimal(Registers[reg1])  +   binary_to_decimal(Registers[reg2])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
            
       
    
    elif op=="00001":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        if binary_to_decimal(Registers[reg1])<binary_to_decimal(Registers[reg2]):
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_binary_16(    binary_to_decimal(Registers[reg1])  -   binary_to_decimal(Registers[reg2])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
        
    elif op=="00110":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        
        if binary_to_decimal(Registers[reg1])*binary_to_decimal(Registers[reg2])>65535:
            Registers["111"]="0000000000001000"
            Registers[i[1]][1]="0000000000000000"
        else:
            Registers[reg]=decimal_to_binary_16(    binary_to_decimal(Registers[reg1])  *   binary_to_decimal(Registers[reg2])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
        
        
    elif op=="01010":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
       
        Registers[reg]=(bin(int(Registers[reg1], 2) ^ int(Registers[reg2], 2))[2:].zfill(16))
        pc=pc+1
        
        
       
        
    elif op=="01011":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
      
        Registers[reg]=(bin(int(Registers[reg1], 2) | int(Registers[reg2], 2))[2:].zfill(16))
        pc=pc+1
        
       
        
    elif op=="01100":
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
       
        Registers[reg]=(bin(int(Registers[reg1], 2) & int(Registers[reg2], 2))[2:].zfill(16))
        pc=pc+1
        
     
        
    
    ## Type B and C    
    elif op=="00010":    # Type B
        p=pc
        
        reg=i[6:9]
        imm_val=i[9:16]            
        Registers[reg]="000000000"+(imm_val)
        pc=pc+1
       
    elif op=="00011":   ## Type C
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]  
        Registers[reg1]=(Registers[reg2])
        Registers[reg2]="0000000000000000" 
        pc=pc+1
        
    ## Type B
    elif op=="01000":
        p=pc
        reg = i[5:9]     
        val = i[9:16]
      
        shifted=((int(Registers[reg],2))>>(int(val))) & 0xFFFF
        Registers[reg]=(bin(shifted)[2:].zfill(16))
        pc=pc+1
        
    
    elif op=="01001":
        p=pc
        reg = i[6:9]     
        val = i[9:16]
        
        shifted=((int(Registers[reg],2))<<(int(val))) & 0xFFFF
        Registers[reg]=(bin(shifted)[2:].zfill(16))
        pc=pc+1
        
        
    
    
     ### Type C
    elif op=="00111":
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
       
        if binary_to_decimal(binary_to_decimal(Registers[reg2]))==0:
            Registers["111"]=="0000000000001000"
            Registers["000"]="0000000000000000"
            Registers["001"]="0000000000000000"
        else:
            Registers["000"]=decimal_to_binary_16(    binary_to_decimal(Registers[reg1])  //   binary_to_decimal(Registers[reg2])   )
            Registers["001"]=decimal_to_binary_16(    binary_to_decimal(Registers[reg1])  %   binary_to_decimal(Registers[reg2])   )
            Registers["111"]="0000000000000000"
       
        pc=pc+1
       
    elif i[0]=="01101":
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
        
        Registers[reg1]=bin(~(binary_to_decimal(Registers[reg2])))[3:].zfill(16)
       
        pc=pc+1
        
    elif op=="01110":
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
        
        if binary_to_decimal(Registers[reg1])>binary_to_decimal(Registers[reg2]):
            Registers["111"]="0000000000000010"
        elif binary_to_decimal(Registers[reg1])<binary_to_decimal(Registers[reg2]):
            Registers["111"]="0000000000000100"
        elif binary_to_decimal(Registers[reg1])==binary_to_decimal(Registers[reg2]):
            Registers["111"]="0000000000000001"
        
        pc=pc+1
        
    
    
    ###### Type D
    elif op=="00100":
        p=pc
        reg=i[6:9]
        mem_add=i[9:16]
        Registers[reg]=(memory_address[mem_add])
        pc=pc+1
        
    elif op=="00101":
        p=pc
        reg=i[6:9]
        mem_add=i[9:16]
        memory_address[mem_add]=Registers[reg]
        pc=pc+1
      
        
    
    
     ######### Type E
    elif op=="01111":
        p=pc
        pc=int(i[9:16],2)
       
        
    elif op=="11101":
        p=pc
       
        if Registers["111"][-2]=="1":
            pc=int(i[9:16],2)
        else:
            pc=pc+1
        Registers["111"]="0000000000000000"
        
    elif op=="11100":
        p=pc
       
        if Registers["111"][-3]=="1":
            pc=int(i[9:16],2)
        else:
            pc=pc+1
        Registers["111"]="0000000000000000"  
        
    elif op=="11111":
        p=pc
       
        if Registers["111"][-1]=="1":
            pc=int(i[9:16],2)
        else:
            pc=pc+1
        Registers["111"]="0000000000000000"
        
        
    ### Type F
    elif op=="11010":
        p=pc
        pc=len(input)
       
    print(decimal_to_binary_7(p),end="        ")
    for j in Registers.values():
        print(j,end=" ")
    print()
for k in memory_address.values():
    print(k)

 
