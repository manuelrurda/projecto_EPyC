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

tA6 = {
    "ADDHL":"00ss1001",
    "ADCHL":"1110110101ss1010",
    "SBCHL":"1110110101ss0010",
    "ADDIX":"1101110100pp1001"
    #POR TERMINAR
}