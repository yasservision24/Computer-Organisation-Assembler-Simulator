
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
    "hlt": "11010",
# bonus instructions
    "sqr": "10000",   # square R1 R2       square the contecnt of R2 and store in R1
    "cube": "10100",   # cube R1 R2       cube the contecnt of R2 and store in R1
    "arc" : "11000",    # area_of_circle R1 R2        finde the area of circle  and store in R1and R2 contains radius of circle 
    "spd": "10010",    # speed  R1 R2 R3    store the speed in R1 R2 has distance R3 has time
    "art": "10001"}   # square_root R1 R2 R3      find area of traingle store in R1   R2 has base R3 has height
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
    


def floating_to_decimal(binary):
    exp=binary[:3]
    exp = int(exp, 2)
    e=exp-3
    mantissa=binary[3:]
    n=0
    p=-1
    for i in mantissa:
        n=n+int(i)*(2**p)
        p=p-1
    return ((1+n)*(2**e))
    

    
def decimal_to_floating(num) :  
    num = float(num)
    bn=bin(int(num)).replace("0b","")
    n=num-int(num)
    a=1
    s=""
    while (n!=1 and a!=10):
        n=n*2
        a=a+1
        if (n<1):
            s=s+"0"
        elif (n>1):
            s=s+"1"
            n=n-1
        elif (n==1):
            s=s+"1"
    s1=bn+"."+s
    #print(f"the binary representation of {num} is {s1}")

    if (len(bn)>5):
        print("error")
    elif (bn!="0"):
        bias=3
        E=3+len(bn)-1
        #print(f"Exponent in decimal={E}")
        #print(f'Exponent in binary={bin(E).replace("0b","")}')
        b2=bin(E).replace("0b","")
        if (len(b2)<3):
            b2="0"+b2
        ment=s1[1::]
        menti=ment.replace(".","")
        
        #print(f"fractional part : {menti}")
        if (len(menti)>=5):
            mentisa=menti[0:5]
        elif (len(menti)==4):
            mentisa=menti+"0"
        elif (len(menti)==3):
            mentisa=menti+"00"
        elif (len(menti)==2):
            mentisa=menti+"000"
        elif (len(menti)==1):
            mentisa=menti+"0000"
            
    elif (bn=="0"):
        index=s1.index("1")
        #print(f"Exponent is {4-index}")
        
        fraction=s1[index+1:]
        #print(f"fraction : {fraction}")
        E=4-index
        b2=bin(E).replace("0b","")
        
        if (len(b2)==1):
            b2="00"+b2
        elif (len(b2)==2):
            b2="0"+b2
        
        
        if (len(fraction)>=5):
            mentisa=fraction[0:5]
        elif (len(fraction)==4):
            mentisa= fraction+"0"
        elif (len(fraction)==3):
            mentisa=fraction+"00"
        elif (len(fraction)==2):
            mentisa=fraction+"000"
        elif (len(fraction)==1):
            mentisa=fraction+"0000"
        elif (len(fraction)==0):
            mentisa=fraction+"00000"
    string = f"{b2}{mentisa}"
    padded_string = "0" * 8 + string
    return (padded_string)






def decimal_to_binary_7(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(7)

def decimal_to_binary_16(decimal):
    decimal=int(decimal)
    return bin(decimal)[2:].zfill(16) 

def binary_to_decimal(binary):
    return int(binary, 2)

input = []

for i in sys.stdin:
    i = i.rstrip() 
    words = i.split()
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
    if op=="00000": #add
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        
        if floating_to_decimal(Registers[reg1][8:])+floating_to_decimal(Registers[reg2][8:])>31.5 or floating_to_decimal(Registers[reg1][8:])+floating_to_decimal(Registers[reg2][8:])<0.125:
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  +   floating_to_decimal(Registers[reg2][8:])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
        
        
    
    if op=="10010": #spd     

        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        if floating_to_decimal(Registers[reg1][8:])==0:
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        elif floating_to_decimal(Registers[reg1][8:])/floating_to_decimal(Registers[reg2][8:])>31.5 or floating_to_decimal(Registers[reg1][8:])/floating_to_decimal(Registers[reg2][8:])<0.125 :
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  /   floating_to_decimal(Registers[reg2][8:])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
        
        
    
    if op=="10001": # art
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        
        if 1/2*floating_to_decimal(Registers[reg1][8:])*floating_to_decimal(Registers[reg2][8:])>31.5 or 1/2*floating_to_decimal(Registers[reg1][8:])*floating_to_decimal(Registers[reg2][8:])<0.125:
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_floating(  1/2 *floating_to_decimal(Registers[reg1][8:])  *  floating_to_decimal(Registers[reg2][8:])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
        
            
       
    if op=="00001": #sub
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        if floating_to_decimal(Registers[reg1][8:])<floating_to_decimal(Registers[reg2][8:]):
            Registers["111"]="0000000000001000"
            Registers[reg]="0000000000000000"
            if floating_to_decimal(Registers[reg1][8:])-floating_to_decimal(Registers[reg2][8:])>31.5 or floating_to_decimal(Registers[reg1][8:])+floating_to_decimal(Registers[reg2][8:])<0.125 :
                Registers["111"]="0000000000001000"
                Registers[reg]="0000000000000000"
        else:
            Registers[reg]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  -   floating_to_decimal(Registers[reg2][8:])   )
        pc=pc+1
        Registers["111"]="0000000000000000"
    

        
    elif op=="00110": #mul
        p=pc
        reg=i[7:10]
        reg1=i[10:13]
        reg2=i[13:16]
        
        if floating_to_decimal(Registers[reg1][8:])*floating_to_decimal(Registers[reg2][8:])>31.5 or floating_to_decimal(Registers[reg1][8:])*floating_to_decimal(Registers[reg2][8:])<0.125:
            Registers["111"]="0000000000001000"
            Registers[i[1]][1]="0000000000000000"
        else:
            Registers[reg]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  *   floating_to_decimal(Registers[reg2][8:])   )
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
        imm_val=i[8:16]            
        Registers[reg]="00000000"+(imm_val)
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
    elif op=="00111": #divide
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
       
        if binary_to_decimal(binary_to_decimal(Registers[reg2]))==0:
            Registers["111"]=="0000000000001000"
            Registers["000"]="0000000000000000"
            Registers["001"]="0000000000000000"
        else:
            Registers["000"]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  //   floating_to_decimal(Registers[reg2][8:])   )
            Registers["001"]=decimal_to_floating(    floating_to_decimal(Registers[reg1][8:])  %   floating_to_decimal(Registers[reg2][8:])   )
            Registers["111"]="0000000000000000"
       
        pc=pc+1
       
       
       
    elif op=="10000":   #sqr
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
       
        if floating_to_decimal(Registers[reg2][8:])**2>31.5 or floating_to_decimal(Registers[reg2][8:])**2<0.125 :
            Registers["111"]="0000000000001000"
            Registers[reg1]="0000000000000000"
        else:
            Registers[reg1]=decimal_to_floating(floating_to_decimal(Registers[reg2][8:])**2   )
        pc=pc+1
        Registers["111"]="0000000000000000"
       
       
    elif op=="10100":   #cube
        p=pc
        reg1=i[10:13]
        reg2=i[13:16]
       
        if floating_to_decimal(Registers[reg2][8:])**3>31.5 or floating_to_decimal(Registers[reg2][8:])**3<0.125 :
            Registers["111"]="0000000000001000"
            Registers[reg1]="0000000000000000"
        else:
            Registers[reg1]=decimal_to_floating(floating_to_decimal(Registers[reg2][8:])**3   )
        pc=pc+1
        Registers["111"]="0000000000000000" 
      
    
    
    elif op=="11000":   #arc
        p=pc      
        reg1=i[10:13]
        reg2=i[13:16]
       
        if 3.14*floating_to_decimal(Registers[reg2][8:])**2>31.5 or 3.14*floating_to_decimal(Registers[reg2][8:])**2<0.125 :
            Registers["111"]="0000000000001000"
            Registers[reg1]="0000000000000000"
        else:
            Registers[reg1]=decimal_to_floating(3.14*floating_to_decimal(Registers[reg2][8:])**2   )
        pc=pc+1
        Registers["111"]="0000000000000000"
     
       
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
        
        if floating_to_decimal(Registers[reg1][8:])>floating_to_decimal(Registers[reg2][8:]):
            Registers["111"]="0000000000000010"
        elif floating_to_decimal(Registers[reg1][8:])<floating_to_decimal(Registers[reg2][8:]):
            Registers["111"]="0000000000000100"
        elif floating_to_decimal(Registers[reg1][8:])==floating_to_decimal(Registers[reg2][8:]):
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
