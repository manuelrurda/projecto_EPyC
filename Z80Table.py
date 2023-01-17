# Basura
# C_Bin={
#     "LD r,r'":"01rR",
#     "LD r,n":"00r110",
#     "LD r,(HL)":"01r110", #Revisar
#     "LD r,(IX+d)":"11011110d", #Revisar
#     "LD r,(IY+d)":"11111101", #Revisar
#     "LD (HL),r":"01110r",
#     "LD (IX+d),r":"11011101r", #Revisar
#     "LD (IY+d),r":"11111101", #Revisar
#     "LD (HL),n":"00110110", #Revisar
#     "LD (IX+d),n":"11011101", #Revisar
#     "LD (IY+d),n":"11111101", #Revisar
#     "LD A,(BC)":"00001010",
#     "LD A,(DE)":"00011010",
#     "LD A,(nn)":"00111010", #Revisar
#     "LD (BC),A":"00000010",
#     "LD (DE),A":"00010010",
#     "LD (nn),A":"00110010", #Revisar
#     "LD A,I":"1110110101010111", #Revisar
#     "LD A,R":"1110110101011111", #Revisar
#     "LD I,A":"1110110101000111", #Revisar
#     "LD R,A":"1110110101001111", #Revisar

# }


#Registros individuales
registros={
    "A":"111",
    "B":"000",
    "C":"001",
    "D":"010",
    "E":"011",
    "H":"100",
    "L":"101"
}

#Registros pares
reg_par={
    "BC":"00",
    "DE":"01",
    "HL":"10",
    "SP":"11"
}

#Tabla A-3 Grupo de intercambio y transferencia y busqueda de bloques
tA3 = {
    "EX DE,HL":"11101011",
    "EX AF,AF'":"00001000",
    "EXX":"11011001",
    "EX (SP),HL":"11100011",
    "EX (SP),IX":"1101110111100011",
    "EX (SP),IY":"1111110111100011",
    "LDI":"1110110110100000",
    "LDIR":"1110110110110000",
    "LDD":"1010110110101000",
    "LDDR":"1110110110111000",
    "CPI":"1110110110100001",
    "CPIR":"1110110110110001",
    "CPD":"1110110110101001",
    "CPDR":"1110110110111001"
}

ins_TA4 = {
    "ADD":"000",
    "ADC":"001",
    "SUB":"010",
    "SBC":"011",
    "AND":"100",
    "OR":"110",
    "XOR":"101",
    "CP":"111"
}

tA4 = {
    "reg":"10xr",
    "num":"11x110n",
    "(HL)":"10x110",
    "(IX+d)":"1101110110x110d",
    "(IY+d)":"1111110110x110d",
    "regID":"00rx",
    "(HL)ID":"00110x",
    "IXID":"1101110100110xd",
    "IYID":"1111110100110xd"
}

tA5 = {
    "DAA":"00100111",
    "CPL":"00101111",
    "NEG":"1110110101000100",
    "CCF":"00111111",
    "SCF":"00110111",
    "NOP":"00000000",
    "HALT":"01110110",
    "DI":"11110011",
    "EI":"11111011",
    "IM":"1110110101x110"
}

ins_TA6 = [
    'ADD',
    'ADC',
    'SBC',
    'INC',
    'DEC'
]

tA6 = {
    "ADDHL":"00ss1001",
    "ADCHL":"1110110101ss1010",
    "SBCHL":"1110110101ss0010",
    "ADDIX":"1101110100ss1001",
    "ADDIY":"1111110100ss1001",
    "INC":"00ss0011",
    "INCIX":"1101110100100011",
    "INCIY":"1111110100100011",
    "DEC":"00ss1011",
    "DECIX":"1101110100101011",
    "DECIY":"1111110100101011"
}

ins_TA7 = {
    "RLC":"000",
    "RL":"010",
    "RRC":"001",
    "RR":"011",
    "SLA":"100",
    "SRA":"101",
    "SRL":"111"
}

ins_TA7_P2 = {
    "RLCA":"00000111",
    "RLA":"00010111",
    "RRCA":"00001111",
    "RRA":"00011111",
    "RLD":"1110110101101111",
    "RRD":"1110110101100111"
}

tA7 = {
    "reg":"1100101100xr",
    "(HL)":"1100101100x110",
    "(IX+d)":"1101110111001011d00x110",
    "(IY+d)":"1111110111001011d00x110"
}

t8_ins = {
    "BIT":"01",
    "SET":"11",
    "RES":"10"
}

tA8 = {
    "reg":"11001011xbr",
    "(HL)":"11001011xb110",
    "(IX+d)":"1101110111001011dxb110",
    "(IY+d)":"1111110111001011dxb110",
    
}

tcc = {
    "NZ":"000",
    "Z":"001",
    "NC":"010",
    "C":"011",
    "PO":"100",
    "PE":"101",
    "P":"110",
    "M":"111"
}

extra_TA9 = [
    '(HL)',
    '(IX)',
    '(IY)'
]

tA9 = {
    "JPN":"11000011nn",
    "JPC":"11cc010nn",
    "JR":"00011000e",
    "JRC":"00111000e",
    "JRNC":"00110000e",
    "JRZ":"00101000e",
    "JRNZ":"00100000e",
    "JP(HL)":"11101001",
    "JP(IX)":"1101110111101001",
    "JP(IY)":"1111110111101001",
    "DJNZ":"00010000e"
}

tA10 = {
    "CALLN":"11001101nn",
    "CALLC":"11cc100nn",
    "RET":"11001001",
    "RETC":"11cc000",
    "RETI":"1110110101001101",
    "RETN":"1110110101000101",
    "RST":"11t111"
}

t_tA10 = {
    "00H":"000",
    "08H":"001",
    "10H":"010",
    "18H":"011",
    "20H":"100",
    "28H":"101",
    "30H":"110",
    "38H":"111"
}

