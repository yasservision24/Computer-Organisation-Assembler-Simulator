################################################################################################################ sujal(2022512)
import sys
import keyword
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
Registers={"R0":["000","0000000000000000"],
           "R1":["001","0000000000000000"],
           "R2":["010","0000000000000000"],
           "R3":["011","0000000000000000"],
           "R4":["100","0000000000000000"],
           "R5":["101","0000000000000000"],
           "R6":["110","0000000000000000"],
           "FLAGS":["111","0000000000000000"]}

memory_address = {}
for i in range(128):
    bin_str = format(i, '07b')  
    memory_address[bin_str] = "0000000"

def is_valid_number(num):
    if num.isdigit():  
        num = int(num)
        if 0 <= num <= 127: 
            return True
    return False
def is_binary(value):
    value_str = str(value)
    for char in value_str:
        if char != "0" and char != "1":
            return False
    return True

def comment_or_emptyline(line):
    if line.strip() == "" or line.strip()[0] == "#":
        return True
    return False
def is_empty(line):
    if not line.strip():
        return True
    return False

def decimal_to_binary_7(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(7)

def decimal_to_binary_16(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(16) 

def binary_to_decimal(binary):
    return int(binary, 2)

def comment_or_emptyline(line):
    if line.strip() == "" or line.strip()[0] == "#":
        return True
    return False
            
def is_hlt_last(input):
    lenth=len(input)-1
    if input[lenth][-1]=="hlt":
        return True
    else:
        print("ERROR:  at line no.",lenth+1, "hlt instruction missing from last of program")
        sys.exit()

def is_hlt_only_in_last(input):
    for i in range(len(input)-1):
        if input[i][0]=="hlt":
            print("ERROR:  at line no. ",i+1, " can't execute after hlt, hlt instruction present in a line other than the last one")
            sys.exit()
    return True  
    
def is_valid_word(input):
    for i in range(len(input)):
        if input[i][0] in opcode.keys():
            continue
        elif input[i][0]=="var":
            continue
        elif input[i][0][-1]==":":
            continue
        else:
            print("Syntax ERROR,at",i+1,"not a valid opcode/literal/label")
            sys.exit()
    return True

var_name_list=[]
def is_var(input):
    for i in range(len(input)):
        if input[i][0]=="hlt" or input[i][0][-1]==":":
            continue
        if input[i][0]=="var":
            if len(input[i]) == 2:
                var_name = input[i][1]
                if keyword.iskeyword(var_name):
                    print("Error,  at line no. ",i+1, "Python keyword can not be used as var name")
                    sys.exit()
                if not var_name.isidentifier():
                    print("ERROR  at line no. ",i+1, "", words[1], "can not be a valid variable name")
                    sys.exit()
            else:
                print("syntax ERROR at line no. ",i+1, " 'var' takes only one operand as name of the var but ", str(len(input[i])-1), " was given")
                sys.exit()
        var_name_list.append(input[i][1])
    return True 
           #########################################################################################################################sahil22427
              
label_name_list=[]
def is_label(input):
    for i in range(len(input)):
        if input[i][0][-1]==":":
            label_name_list.append(input[i][0][:-1])
    return True  
             
def is_var_above(input):  
    for i in range(len(input)):
        if input[i][0]!="var":
            break    
    for j in range(i,len(input)):
        if input[j][0]=="var":
            print("ERROR, at line no. ",j+1, " variable names should be declared in the  starting of the program")
            sys.exit()        
    return True

def is_valid_syntax(input):
    for i in range(len(input)):
        if input[i][0][-1]==":":
            words=input[i][1:]
        else:
            words=input[i]
        op_code= words[0]
        if op_code in ["add", "sub", "mul", "xor", "or", "and"]:
            if len(words) == 4:
                for word in words[1:]:
                   
                    if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                        print("Syntax ERROR:  at line no. ",i+1, ""  + word+" is not a valid register name")
                        sys.exit()
                    if word=="FLAGS":
                        print("ERROR:at line no.",i+1,",  illegal use of FLAGS  register")
                        sys.exit()
               
            else:
                print("Syntax ERROR: at line no.",i+1, +   op_code + "' supports three operands, " + str(len(words)-1) + " were given")
                sys.exit()
               
               
               
        elif op_code in ["mov","rs","ls","div","not","cmp"]: #Type_B and Type_C error checking
            if words[2]  not in  ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]: #Type_B
                if len(words) == 3:
                    for word in words[1:2]:
                        if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                            print("Syntax ERROR:  at line no. ",i+1, ""  + word+"is not a valid register name")
                            sys.exit()
                        if word=="FLAGS":
                            print("ERROR:at line no.",i+1,",  illegal use of FLAGS  register")
                            sys.exit()
                    for word in words[2:3]:
                        if word[0]=="$":
                            if not is_valid_number(word[1:]):
                                print("ERROR :  at line no. ",i+1, ""  + word+"must be integer between 0 and 127")
                                sys.exit()
                        else:
                            print("Syntax ERROR:  at line no. ",i+1, " \"$\" is missing or  , out of range value,Second operand must be $imm integer between 0 and 127 ")
                            sys.exit()
                else:
                    print("Syntax ERROR:  at line no. ",i+1, "'" + op_code + "' supports 2 operands, " + str(len(words)-1) + " were given")
                    sys.exit()
                   
            else: #Type_C
                if len(words) == 3:
                    if words[0]=="mov":
                        for word in words[1:2]:
                            if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                                print("Syntax ERROR:  at line no. ",i+1, ""  + word+"is not a valid register name")
                                sys.exit()
                            if word=="FLAGS":
                                print("ERROR:at line no.",i+1,",  illegal use of FLAGS  register")
                                sys.exit()
                        for word in words[2:]:
                            if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                                print("Syntax ERROR:  at line no. ",i+1, ""  + word+"is not a valid register name")
                                sys.exit()
                    else:
                        for word in words[1:]:
                            if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                                print("Syntax ERROR:  at line no. ",i+1, ""  + word+"is not a valid register name")
                                sys.exit()
                            if word=="FLAGS":
                                print("ERROR:at line no.",i+1,",  illegal use of FLAGS  register")
                                sys.exit()
                       
                else:
                    print("Syntax ERROR:  at line no. ",i+1, "'" + op_code + "' supports 2 operands, " + str(len(words)-1) + " were given")
                    sys.exit()
           
        elif op_code in ["ld","st"]: #Type_D error checking
            if len(words) == 3:
                for word in words[1:2]:
                    if word not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]:
                        print("Syntax ERROR at line no. ",i+1, ": "  + word+"is not a valid register name")
                        sys.exit()
                    if word=="FLAGS":
                        print("ERROR:at line no.",i+1,",  illegal use of FLAGS  register")
                        sys.exit()
                for word in words[2:3]:
                    if  word in var_name_list:
                         pass
                    else:
                        print("Name ERROR: at line no.",i+1, ""  + word+" is not a defined variable ")
                        sys.exit()        
                             
               
            else:
                print("Syntax ERROR:  at line no. ",i+1, "'" + op_code + "' supports 2 operands, " + str(len(words)-1) + " were given")
                sys.exit()
               
        elif op_code in ["jmp","jlt","jgt","je"]: #Type_E error checking
            if len(words) == 2:
                for word in words[1:2]:
                    if  word in label_name_list:
                         pass
                    else:
                        print("Name ERROR: at line no.",i+1, ""  + word+" is not a defined label")
                        sys.exit()  
               
               
            else:
                print("Syntax ERROR:  at line no. ",i+1, " '" + op_code + "' supports 2 operands, " + str(len(words)-1) + " were given")
                sys.exit()
               
        elif op_code=="hlt" :
            continue
                       
       
        elif op_code=="var":
            continue
           
           
        elif op_code[-1]==":":
            continue
           
               
       
        else:
            print("Syntax ERROR:  at line no. ",i+1, "Invalid instruction! ",words[0],"is not an instruction")
            sys.exit()
    return True

        

##################################################################################################### udbhav
input = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        break  # Exit the loop if an empty line is entered
    if comment_or_emptyline(line):
        continue
    else:
        words = line.split()
        input.append(words)
            

if is_hlt_only_in_last(input):
    pass
if is_hlt_last(input):
    pass
if is_var_above(input):
    pass
if is_valid_word(input):
    pass
if is_label(input):
    pass
if is_var(input):
    pass
if is_valid_syntax(input):
    pass


var_counter=0
total_instruction=0
for i in input:

    if i[0]=="var":
        var_counter+=1
        continue
        
    elif i[0][-1]==":":
        j=decimal_to_binary_7(total_instruction)
        temp_list=[j,i[1]]
        memory_address[i[0][:-1]]=temp_list
        total_instruction+=1
        
    else:
        total_instruction+=1

for i in input:
    if i[0]=="var":
        j=decimal_to_binary_7(total_instruction)
        temp_list=j
        memory_address[i[1]]=temp_list
        total_instruction+=1
                     
machine_code=[]  
for i in range(len(input)):
    if input[i][0][-1]==":":
        input[i].remove(input[i][0])
memory_address_pointer=0    
for i in input:
    
    if i[0]=="var":
        continue
   
    ## Type A
    elif i[0]=="add":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        if binary_to_decimal(Registers[i[2]][1])+binary_to_decimal(Registers[i[3]][1])>65535:
            Registers["FLAGS"][1]="0000000000001000"
            Registers[i[1]][1]="0000000000000000"
        else:
            Registers[i[1]][1]=decimal_to_binary_16(    binary_to_decimal(Registers[i[2]][1])  +   binary_to_decimal(Registers[i[3]][1])   )
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
    
    elif i[0]=="sub":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        if binary_to_decimal(Registers[i[2]][1])<binary_to_decimal(Registers[i[3]][1]):
            Registers["FLAGS"][1]="0000000000001000"
            Registers[i[1]][1]="0000000000000000"
        else:
            Registers[i[1]][1]=decimal_to_binary_16(    binary_to_decimal(Registers[i[2]][1])  -   binary_to_decimal(Registers[i[3]][1])   )
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
    
    elif i[0]=="mul":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        if binary_to_decimal(Registers[i[2]][1])*binary_to_decimal(Registers[i[3]][1])>65535:
            Registers["FLAGS"][1]="0000000000001000"
            Registers[i[1]][1]="0000000000000000"
        else:
            Registers[i[1]][1]=decimal_to_binary_16(    binary_to_decimal(Registers[i[2]][1])  *   binary_to_decimal(Registers[i[3]][1])   )
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="xor":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        Registers[i[1]][1]=(bin(int(Registers[i[2]][1], 2) ^ int(Registers[i[3]][1], 2))[2:].zfill(16))
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="or":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        Registers[i[1]][1]=(bin(int(Registers[i[2]][1], 2) | int(Registers[i[3]][1], 2))[2:].zfill(16))
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="and":
        m=(opcode[i[0]]+"00"+Registers[i[1]][0]+Registers[i[2]][0]+Registers[i[3]][0])
        machine_code.append(m)
        Registers[i[1]][1]=(bin(int(Registers[i[2]][1], 2) & int(Registers[i[3]][1], 2))[2:].zfill(16))
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    
    ## Type B and C
    elif i[0]=="mov":
        if i[2] not in ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]: ## Type B
            m="00010"+"0"+Registers[i[1]][0]+decimal_to_binary_7((i[2][1:]))
            machine_code.append(m)
            Registers[i[1]][1]="000000000"+decimal_to_binary_7(i[2][1:])
            j=decimal_to_binary_7(memory_address_pointer)
            memory_address[j]=m
            
        else: 
            m=opcode[i[0]]+"00000"+Registers[i[1]][0]+Registers[i[2]][0]  ## Type C
            machine_code.append(m)
            Registers[i[1]][1]=Registers[i[2]][1]
            Registers[i[2][1]]="0000000000000000"
            j=decimal_to_binary_7(memory_address_pointer)
            memory_address[j]=m
  ##########################################################################################################Syed Yasser       
    ## Type B
    elif i[0]=="rs":
        m="00010"+"0"+Registers[i[1]][0]+decimal_to_binary_7((i[2][1:]))
        machine_code.append(m)
        shifted=((int(Registers[i[1]][1],2))>>(int(i[2][1:]))) & 0xFFFF
        Registers[i[1]][1]=(bin(shifted)[2:].zfill(16))
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
    
    elif i[0]=="ls":
        m="00010"+"0"+Registers[i[1]][0]+decimal_to_binary_7((i[2][1:]))
        machine_code.append(m)
        shifted=((int(Registers[i[1]][1],2))<<(int(i[2][1:]))) & 0xFFFF
        Registers[i[1]][1]=(bin(shifted)[2:].zfill(16))
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    
    
     ### Type C
    elif i[0]=="div":
        m=opcode[i[0]]+"00000"+Registers[i[1]][0]+Registers[i[2]][0]
        machine_code.append(m)
        if binary_to_decimal(binary_to_decimal(Registers[i[2]][1]))==0:
            Registers["FLAGS"][1]=Registers["FLAGS"][1]
            Registers["R0"]="0000000000000000"
            Registers["R1"]="0000000000000000"
        else:
            Registers["R0"]=decimal_to_binary_16(    binary_to_decimal(Registers[i[2]][1])  //   binary_to_decimal(Registers[i[3]][1])   )
            Registers["R1"]=decimal_to_binary_16(    binary_to_decimal(Registers[i[2]][1])  %   binary_to_decimal(Registers[i[3]][1])   )
        j=decimal_to_binary_7(memory_address_pointer)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
       
    elif i[0]=="not":
        m=opcode[i[0]]+"00000"+Registers[i[1]][0]+Registers[i[2]][0]
        machine_code.append(m)
        Registers[i[1]][1]=bin(~(binary_to_decimal(Registers[i[2]][1])))[3:].zfill(16)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="cmp":
        m=opcode[i[0]]+"00000"+Registers[i[1]][0]+Registers[i[2]][0]
        machine_code.append(m)
        if binary_to_decimal(Registers[i[1]][1])>binary_to_decimal(Registers[i[2]][1]):
            Registers["FLAGS"][1]="0000000000000010"
        elif binary_to_decimal(Registers[i[1]][1])<binary_to_decimal(Registers[i[2]][1]):
            Registers["FLAGS"][1]="0000000000000100"
        elif binary_to_decimal(Registers[i[1]][1])==binary_to_decimal(Registers[i[2]][1]):
            Registers[i[1]][1]="0000000000000001"
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    
    
    ###### Type D
    elif i[0]=="ld":
        m=(opcode[i[0]]+"0"+Registers[i[1]][0]+memory_address[i[2]])
        machine_code.append(m)
        a=memory_address[i[2]]
        Registers[i[1]][1]=memory_address[a]
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="st":
        m=(opcode[i[0]]+"0"+Registers[i[1]][0]+memory_address[i[2]])
        machine_code.append(m)
        a=memory_address[i[2]]
        memory_address[a]=Registers[i[1]][1]
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
        
    
    
     ######### Type E
    elif i[0]=="jmp":
        m=opcode[i[0]]+"0000"+memory_address[i[1]][0]
        machine_code.append(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="jgt":
        m=opcode[i[0]]+"0000"+memory_address[i[1]][0]
        machine_code.append(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="jlt":
        m=opcode[i[0]]+"0000"+memory_address[i[1]][0]
        machine_code.append(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
    elif i[0]=="je":
        m=opcode[i[0]]+"0000"+memory_address[i[1]][0]
        machine_code.append(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=m
        
        
        
    ### Type E
    elif i[0]=="hlt":
        m=opcode[i[0]]+"00000000000"
        machine_code.append(m)
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=(m)
    
    elif i[0][-1]==":":
        op=memory_address[i[0][:-1]][1]
        machine_code.append(opcode[op]+"00000000000")
        j=decimal_to_binary_7(memory_address_pointer)
        memory_address[j]=(opcode[op]+"00000000000")
    
    
    memory_address_pointer+=1

for i in machine_code:
    print(i)
