from tkinter import filedialog
import Z80Table
import utils
import re
import os

# Mostramos un diálogo de selección de archivos y almacenamos la ruta del archivo seleccionado
ruta_archivo = filedialog.askopenfilename(
  filetypes=[('Archivos ASM', '*.asm')]
)
bug_flag = False
codigo = []
instruction = []
no_linea = 0
CL = 0
ins_large = 0
# Abrimos el archivo en modo lectura ('r') y lo almacenamos en una variable
with open(ruta_archivo, 'r') as archivo:
    nombre, extension = os.path.splitext(ruta_archivo)
    archivo_lst = nombre + '.lst'
    for linea in archivo:
        instruccion_binario = ""
        no_linea += 1
        subins = []
        linea = linea.strip()
        #print(linea)
        if linea == '':
            continue
        instruction.append(linea)
        coment = linea.find("#")
        if coment != -1:
            linea = linea[:coment] + linea[len(linea):]
        linea = linea.upper()
        linea = linea.strip()
        #print(linea)

        division = linea.find(" ")
        if not (division == -1):
            subins.append(linea[:division])
            subins.append(linea[division+1:])
        elif division == -1:
            subins.append(linea)

        # print(subins)
        print(subins[0])
        # print(subins[1])


        #Tabla A-1 y A-2. Grupo de carga de 8 y 16 bits
        #Separa la instruccion de los operandos
        if subins[0] == "LD":
            #Separa los operandos
            registro = subins[1].split(",")
            registro[0] = registro[0].strip()
            registro[1] = registro[1].strip()
            rAux0 = registro[0]
            rAux1 = registro[1]

        #8 bits
            #LD r,r'
            if registro[0] in Z80Table.registros and registro[1] in Z80Table.registros:
                #Se obtiene la instruccion en binario
                instruccion_binario = "01"+Z80Table.registros[registro[0]]+Z80Table.registros[registro[1]] 

            #LD r,n
            elif registro[0] in Z80Table.registros and re.match(r'^[0-9]{1,4}$',registro[1]):
                #Se obtiene el dato y se transforma a decimal
                if int(registro[1]) < 256:
                    dato = str(bin(int(registro[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "00"+Z80Table.registros[registro[0]]+"110"+dato

            #LD r,(HL)
            elif registro[0] in Z80Table.registros and registro[1] == "(HL)":
                instruccion_binario = "01"+Z80Table.registros[registro[0]]+"110"


            #LD r,(IX+d)
            elif registro[0] in Z80Table.registros and re.match(r'^\(IX\+[0-9]{1,4}\)$',registro[1]):
                registro[1] = registro[1].replace("(","")
                registro[1] = registro[1].replace(")","")
                reg_data = registro[1].split("+")
                if int(reg_data[1]) < 256:
                    dato = str(bin(int(reg_data[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "1101110101"+Z80Table.registros[registro[0]]+"110"+dato

            #LD r,(IY+d)
            elif registro[0] in Z80Table.registros and re.match(r'^\(IY\+[0-9]{1,4}\)$',registro[1]):
                registro[1] = registro[1].replace("(","")
                registro[1] = registro[1].replace(")","")
                reg_data = registro[1].split("+")
                if int(reg_data) < 256:
                    dato = str(bin(int(reg_data[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "1111110101"+Z80Table.registros[registro[0]]+"110"+dato


            #LD (HL),r
            elif registro[0] == "(HL)" and registro[1] in Z80Table.registros:
                instruccion_binario = "01110"+Z80Table.registros[registro[1]]

            #LD (IX+d),r
            elif re.match(r'^\(IX\+[0-9]{1,4}\)$',registro[0]) and registro[1] in Z80Table.registros:
                registro[0] = registro[0].replace("(","")
                registro[0] = registro[0].replace(")","")
                reg_data = registro[0].split("+")
                if int(reg_data[1]) < 256:
                    dato = str(bin(int(reg_data[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "1101110101110"+Z80Table.registros[registro[1]]+dato

            #LD (IY+d),r
            elif re.match(r'^\(IY\+[0-9]{1,4}\)$',registro[0]) and registro[1] in Z80Table.registros:
                registro[0] = registro[0].replace("(","")
                registro[0] = registro[0].replace(")","")
                reg_data = registro[0].split("+")
                if int(reg_data[1]) < 256:
                    dato = str(bin(int(reg_data[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "1111110101110"+Z80Table.registros[registro[1]]+dato

            #LD (HL),n
            elif registro[0] == "(HL)" and str.isdigit(registro[1]):
                if int(registro[1]) < 256:
                    #Se obtiene el dato y se transforma a decimal
                    dato = str(bin(int(registro[1]))[2:])
                    dato = dato.zfill(8)
                    instruccion_binario = "00110110"+dato
            
            #LD (IX+d),n
            elif re.match(r'\(IX\+[0-9]{1,4}\)',registro[0]) and str.isdigit(registro[1]):
                if int(registro[1]) < 256:
                    registro[0] = registro[0].replace("(","")
                    registro[0] = registro[0].replace(")","")
                    reg_data = registro[0].split("+")
                    if int(reg_data[1]) < 256:
                        dato_ix = str(bin(int(reg_data[1]))[2:])
                        dato_ix = dato_ix.zfill(8)
                        num = str(bin(int(registro[1]))[2:])
                        num = num.zfill(8)
                        instruccion_binario = "1101110100110110"+dato_ix+num

            #LD (IY+d),n
            elif re.match(r'^\(IY\+[0-9]{1,4}\)$',registro[0]) and str.isdigit(registro[1]):
                if int(registro[1]) < 256:
                    registro[0] = registro[0].replace("(","")
                    registro[0] = registro[0].replace(")","")
                    reg_data = registro[0].split("+")
                    if int(reg_data[1]) < 256:
                        dato_iy = str(bin(int(reg_data[1]))[2:])
                        dato_iy = dato_iy.zfill(8)
                        num = str(bin(int(registro[1]))[2:])
                        num = num.zfill(8)
                        instruccion_binario = "1111110100110110"+dato_iy+num

            #LD A,(BC)
            elif registro[0] == "A" and registro[1] == "(BC)":
                instruccion_binario = "00001010"
            
            #LD A,(DE)
            elif registro[0] == "A" and registro[1] == "(DE)":
                instruccion_binario = "00011010"

            #LD A,(nn)
            elif registro[0] == "A" and (re.match(r'^\([0-9]+\)$',registro[1]) or re.match(r'^\([0-9]+H\)$',registro[1])):
                registro[1] = registro[1].replace("(","")
                registro[1] = registro[1].replace(")","")
                #Si el numero tiene H indica que esta en binario
                regg = registro[1]
                if regg[-1] == "H":
                    registro[1] = registro[1].replace("H","")
                    regi = int(registro[1], 16)
                    nn = bin(regi)[2:]
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00111010" + nn

                #Si no tiene H indica que esta en decimal
                elif int(registro[1]) < 65355:
                    nn = bin(int(registro[1]))[2:]
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00111010" + nn
            
            #LD (BC),A
            elif registro[0] == "(BC)" and registro[1] == "A":
                instruccion_binario = "00000010"

            #LD (DE),A
            elif registro[0] == "(DE)" and registro[1] == "A":
                instruccion_binario = "00010010"

            #LD (nn),A
            elif (re.match(r'^\([0-9]+\)$',registro[0]) or re.match(r'^\([0-9]+H\)$',registro[0])) and registro[1] == "A":
                registro[0] = registro[0].replace("(","")
                registro[0] = registro[0].replace(")","")
                #Si el numero tiene H indica que esta en binario
                regg = registro[0]
                if regg[-1] == "H":
                    registro[0] = registro[0].replace("H","")
                    regi = int(registro[0], 16)
                    nn = bin(regi)[2:]
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00110010" + nn

                #Si no tiene H indica que esta en decimal
                elif int(registro[0]) < 65355:
                    nn = bin(int(registro[0]))[2:]
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00110010" + nn

            
            #LD A,I
            #LD A,R
            elif registro[0] == "A" and (registro[1] == "I" or registro[1] == "R"):
                if registro[1] == "I":
                    instruccion_binario = "1110110101010111"
                elif registro[1] == "R":
                    instruccion_binario = "1110110101011111"
            
            #LD I,A
            #LD R,A
            elif (registro[0] == "I" or registro[0] == "R") and registro[1] == "A":
                if registro[0] == "I":
                    instruccion_binario = "1110110101000111"
                elif registro[0] == "R":
                    instruccion_binario = "1110110101001111"
        
        #16 bits

            #LD dd,nn
            elif registro[0] in Z80Table.reg_par and (str.isdigit(registro[1]) or re.match(r'^[0-9A-F]{1,4}H$',registro[1])):
                regg = registro[1]
                if regg[-1] == "H":
                    regg = regg.replace("H","")
                    if len(regg) < 5:
                        nn = str(bin(int(regg, 16))[2:])
                        nn = nn.zfill(16)
                        nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                        instruccion_binario = "00" + Z80Table.reg_par[registro[0]] + "0001" + nn
                elif int(regg) < 65355:
                    dato = bin(int(registro[1]))[2:]
                    dato = dato.zfill(16)
                    dato = dato[len(dato)//2:] + dato[:len(dato)//2]
                    instruccion_binario = "00" + Z80Table.reg_par[registro[0]] + "0001" + dato
            

            #LD IX,nn
            elif registro[0] == "IX" and (re.match(r'^[0-9A-F]{1,4}H$',registro[1]) or str.isdigit(registro[1])):
                regg = registro[1]
                if regg[-1] == "H":
                    regg = regg.replace("H","")
                    if len(regg) < 5:
                        regg = int(regg,16)
                        nn = str(bin(regg)[2:])
                        nn = nn.zfill(16)
                        nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                        instruccion_binario = "1101110100100001" + nn
                elif int(regg) < 65355:
                    nn = str(bin(int(registro[1],10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1101110100100001" + nn

            #LD IY,nn
            elif registro[0] == "IY" and (re.match(r'^[0-9A-F]{1,4}H$',registro[1]) or str.isdigit(registro[1])):
                regg = registro[1]
                if regg[-1] == "H":
                    regg = regg.replace("H","")
                    if len(regg) < 5:
                        regg = int(regg,16)
                        nn = str(bin(regg)[2:])
                        nn = nn.zfill(16)
                        nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                        instruccion_binario = "1111110100100001" + nn
                elif int(regg) < 65355:
                    nn = str(bin(int(registro[1], 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1111110100100001" + nn
            
            #LD HL,(nn)
            elif registro[0] == "HL" and (re.match(r'^\([0-9A-F]{1,4}H\)',registro[1]) or re.match(r'^\([0-9]{1,5}\)',registro[1])):
                regg = registro[1]
                regg = regg[1:-1]
                if regg[-1] == "H":
                    regg = regg.replace("H")
                    if len(regg) < 5:
                        nn = str(bin(int(regg, 16))[2:])
                        nn = nn.zfill(16)
                        nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                        instruccion_binario = "00101010" + nn
                elif int(regg) < 65355:
                    nn = str(bin(int(regg, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00101010" + nn

            #LD dd,(nn)
            elif registro[0] in Z80Table.reg_par and (re.match(r'^\([0-9A-F]{1,4}H\)',registro[1]) or re.match(r'^\([0-9]{1,5}\)',registro[1])):
                rAux1 = registro[1]
                rAux1 = rAux1[1:-1]
                if rAux1[-1] == "H":
                    rAux1 = rAux1.replace("H","")
                    nn = str(bin(int(rAux1, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1110110101" + Z80Table.reg_par[registro[0]] + "1011" + nn
                elif str.isdigit(rAux1):
                    nn = str(bin(int(rAux1, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1110110101" + Z80Table.reg_par[registro[0]] + "1011" + nn
                

            #LD IX,(nn)
            elif registro[0] == "IX" and (re.match(r'^\([0-9A-F]{1,4}H\)',registro[1]) or re.match(r'^\([0-9]{1,5}\)',registro[1])):
                rAux1 = registro[1]
                rAux1 = rAux1[1:-1]
                if rAux1[-1] == "H":
                    rAux1 = rAux1.replace("H","")
                    nn = str(bin(int(rAux1, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1101110100101010" + nn
                elif str.isdigit(rAux1):
                    nn = str(bin(int(rAux1, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1101110100101010" + nn
            
            #LD IY,(nn)
            elif registro[0] == "IY" and (re.match(r'^\([0-9A-F]{1,4}H\)',registro[1]) or re.match(r'^\([0-9]{1,5}\)',registro[1])):
                rAux1 = registro[1]
                rAux1 = rAux1[1:-1]
                if rAux1[-1] == "H":
                    rAux1 = rAux1.replace("H","")
                    nn = str(bin(int(rAux1, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1111110100101010" + nn
                elif str.isdigit(rAux1):
                    nn = str(bin(int(rAux1, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1111110100101010" + nn
            
            #LD (nn),HL
            elif (re.match(r'^\([0-9A-F]{1,4}H\)',registro[0]) or re.match(r'^\([0-9]{1,5}\)',registro[0])) and registro[1] == "HL":
                regg = registro[0]
                regg = regg[1:-1]
                if regg[-1] == "H":
                    regg = regg.replace("H")
                    if len(regg) < 5:
                        nn = str(bin(int(regg, 16))[2:])
                        nn = nn.zfill(16)
                        nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                        instruccion_binario = "00100010" + nn
                elif int(regg) < 65355:
                    nn = str(bin(int(regg, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "00100010" + nn
            
            #LD (nn),dd
            elif (re.match(r'^\([0-9A-F]{1,4}H\)',registro[0]) or re.match(r'^\([0-9]{1,5}\)',registro[0])) and registro[1] in Z80Table.reg_par:
                rAux0 = registro[0]
                rAux0 = rAux0[1:-1]
                if rAux0[-1] == "H":
                    rAux0 = rAux0.replace("H","")
                    nn = str(bin(int(rAux0, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1110110101" + Z80Table.reg_par[registro[1]] + "0011" + nn
                elif str.isdigit(rAux0):
                    nn = str(bin(int(rAux0, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1110110101" + Z80Table.reg_par[registro[1]] + "0011" + nn

            #LD (nn),IX
            elif (re.match(r'^\([0-9A-F]{1,4}H\)',registro[0]) or re.match(r'^\([0-9]{1,5}\)',registro[0])) and registro[1] == " IX":
                
                rAux0 = registro[0]
                rAux0 = rAux0[1:-1]
                if rAux0[-1] == "H":
                    rAux0 = rAux0.replace("H","")
                    nn = str(bin(int(rAux0, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1101110100100010" + nn
                elif str.isdigit(rAux0):
                    nn = str(bin(int(rAux0, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1101110100100010" + nn

            #LD (nn),IY
            elif (re.match(r'^\([0-9A-F]{1,4}H\)',registro[0]) or re.match(r'^\([0-9]{1,5}\)',registro[0])) and registro[1] == " IY":
                rAux0 = registro[0]
                rAux0 = rAux0[1:-1]
                if rAux0[-1] == "H":
                    rAux0 = rAux0.replace("H","")
                    nn = str(bin(int(rAux0, 16))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1111110100100010" + nn
                elif str.isdigit(rAux0):
                    nn = str(bin(int(rAux0, 10))[2:])
                    nn = nn.zfill(16)
                    nn = nn[len(nn)//2:] + nn[:len(nn)//2]
                    instruccion_binario = "1111110100100010" + nn
            
            #LD SP,HL , LD SP,IX , LD SP,IY
            elif registro[0] == "SP":
                if registro[1] == "HL":
                    instruccion_binario = "11111001"
                elif registro[1] == "IX":
                    instruccion_binario = "1101110111111001"
                elif registro[1] == "IY":
                    instruccion_binario = "1111110111111001"

            else:
                print("Error en la linea {}".format(no_linea))
                bug_flag = True
                break
        
        #PUSH qq, PUSH IX, PUSH IY
        elif subins[0] == "PUSH":
            reg = subins[1]
            if reg in Z80Table.reg_par:
                instruccion_binario = "11" + Z80Table.reg_par[reg] + "0101"
            elif reg == "IX":
                instruccion_binario = "1101110111100101"
            elif reg == "IY":
                instruccion_binario = "1111110111100101"
        
        #POP qq, POP IX, POP IY    
        elif subins[0] == "POP":
            reg = subins[1]
            if reg in Z80Table.reg_par:
                instruccion_binario = "11" + Z80Table.reg_par[reg] + "0001"
            elif reg == "IX":
                instruccion_binario = "1101110111100001"
            elif reg == "IY":
                instruccion_binario = "1111110111100001"
        
        #Tabla A-3. Grupo de intercambio y transferencia y busqueda de bloques

        elif subins[0] == "EX":
            ins_flag = False
            reg = subins[1].split(",")
            reg0 = reg[0].strip()
            reg1 = reg[1].strip()
            instruccion = subins[0] + " " + reg0 + "," + reg1

            if instruccion in Z80Table.tA3:
                instruccion_binario = Z80Table.tA3[instruccion]
            

        elif subins[0] in Z80Table.tA3:
            instruccion_binario = Z80Table.tA3[subins[0]]

        #Tabla A-4. El grupo aritmetico y logico de 8 bits
                
        #ADD hasta CP
        elif subins[0] in Z80Table.ins_TA4 and len(subins) == 2:
            instr = subins[0]
            #ADD r
            if subins[1] in Z80Table.registros:
                instruccion_binario = Z80Table.tA4["reg"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])
                instruccion_binario = instruccion_binario.replace("r",Z80Table.registros[subins[1]])

            #ADD (HL)
            elif subins[1] == "(HL)":
                instruccion_binario = Z80Table.tA4["(HL)"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])

            #ADD (IX+d)
            elif re.match(r'\(IX\+[0-9]{1,3}\)',subins[1]) or re.match(r'\(IX\+[0-9A-F]{1,2}H\)',subins[1]):
                data = subins[1]
                data = data[4:]
                data = data[:-1]
                if data[-1] == "H":
                    data = data.replace("H","")
                    data = str(bin(int(data, 16))[2:])
                    data = data.zfill(8)
                elif data.isdigit():
                    data = str(bin(int(data, 10))[2:])
                    data = data.zfill(8)
                instruccion_binario = Z80Table.tA4["(IX+d)"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])
                instruccion_binario = instruccion_binario.replace("d",data)

            #ADD (IY+d)
            elif re.match(r'\(IY\+[0-9]{1,3}\)',subins[1]) or re.match(r'\(IY\+[0-9A-F]{1,2}H\)',subins[1]):
                data = subins[1]
                data = data[4:]
                data = data[:-1]
                if data[-1] == "H":
                    data = data.replace("H","")
                    data = str(bin(int(data, 16))[2:])
                    data = data.zfill(8)
                elif data.isdigit():
                    data = str(bin(int(data, 10))[2:])
                    data = data.zfill(8)
                instruccion_binario = Z80Table.tA4["(IY+d)"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])
                instruccion_binario = instruccion_binario.replace("d",data)

            #ADD n
            elif subins[1].isdigit or re.match(r'[0-9A-F]{1,2}H',subins[1]):
                data = subins[1]
                if subins[1].isdigit():
                    data = str(bin(int(data, 10))[2:])
                    data = data.zfill(8)
                elif data[-1] == "H":
                    data = data.replace("H","")
                    data = str(bin(int(data, 16))[2:])
                    data = data.zfill(8)
                instruccion_binario = Z80Table.tA4["num"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])
                instruccion_binario = instruccion_binario.replace("n",data)
 
        #INC y DEC
        elif subins[0] == "INC" or subins[0] == "DEC":
            idc = {"INC":"100","DEC":"101"} 
            instr = idc[subins[0]]
            #INC r
            if subins[1] in Z80Table.registros:
                instruccion_binario = Z80Table.tA4["regID"]
                instruccion_binario = instruccion_binario.replace("x",instr)
                instruccion_binario = instruccion_binario.replace("r",Z80Table.registros[subins[1]])

            #INC (HL)
            elif subins[1] == "(HL)":
                instruccion_binario = Z80Table.tA4["(HL)ID"]
                instruccion_binario = instruccion_binario.replace("x",Z80Table.ins_TA4[instr])

            #INC (IX+d)
            elif re.match(r'\(IX\+[0-9]{1,3}\)',subins[1]) or re.match(r'\(IX\+[0-9A-F]{1,2}H\)',subins[1]):
                data = subins[1]
                data = data[4:]
                data = data[:-1]
                if data[-1] == "H":
                    data = data.replace("H","")
                    data = str(bin(int(data, 16))[2:])
                    data = data.zfill(8)
                elif data.isdigit():
                    data = str(bin(int(data, 10))[2:])
                    data = data.zfill(8)
                instruccion_binario = Z80Table.tA4["IXID"]
                instruccion_binario = instruccion_binario.replace("x",instr)
                instruccion_binario = instruccion_binario.replace("d",data)

            #INC (IY+d)
            elif re.match(r'\(IY\+[0-9]{1,3}\)',subins[1]) or re.match(r'\(IY\+[0-9A-F]{1,2}H\)',subins[1]):
                data = subins[1]
                data = data[4:]
                data = data[:-1]
                if data[-1] == "H":
                    data = data.replace("H","")
                    data = str(bin(int(data, 16))[2:])
                    data = data.zfill(8)
                elif data.isdigit():
                    data = str(bin(int(data, 10))[2:])
                    data = data.zfill(8)
                instruccion_binario = Z80Table.tA4["IYID"]
                instruccion_binario = instruccion_binario.replace("x",instr)
                instruccion_binario = instruccion_binario.replace("d",data)
            

        #Tabla A-5. Grupo aritmetico y de control de la CPU de aplicacion general
        elif subins[0] in Z80Table.tA5:
            instruccion_binario = Z80Table.tA5[subins[0]]
            if len(subins) > 1:
                if subins[1] == "0":
                    instruccion_binario = instruccion_binario.replace("x","000")
                elif subins[1] == "1":
                    instruccion_binario = instruccion_binario.replace("x","010")
                elif subins[1] == "2":
                    instruccion_binario = instruccion_binario.replace("x","011")

        #Tabla A-6. Grupo aritmetico y de control de la CPU de aplicacion general
        elif subins[0] in Z80Table.ins_TA4 and len(subins) == 3:
            A=1

        #En caso de encontrar un error indica en que linea y finaliza
        else:
            print("Error en la linea {}".format(no_linea))
            bug_flag = True
            break

        if len(instruccion_binario) > 0:
            ins_hex = utils.transformar(instruccion_binario)
            print("appending: " + utils.generar_codigo(CL, ins_hex))
            codigo.append(utils.generar_codigo(CL, ins_hex))
            CL = CL + int(len(ins_hex)/2)
            if int(len(ins_hex)) > ins_large:
                ins_large = int(len(ins_hex))
        #Tabla A-3. Grupo de intercambio y transferencia y busqueda de bloques


    #Si el programa no encuentra errores finaliza y escribe el codigo
    if not bug_flag:
        print(codigo)
        print(len(codigo))
        # print(instruction)
        # print(len(instruction))
        arc_lst = open(archivo_lst,'w')
        ins_large = ins_large + 9
        lineas_escribir = len(codigo)
        escritura = ""
        for i in range(0, lineas_escribir, 1):
            #arc_lst.write(" " + codigo[i].ljust(ins_large) + "    " + instruction[i] + "\n")
            # print(i)
            cadena_arc = " " + codigo[i].ljust(ins_large) + "    " + instruction[i] + "\n"
            escritura += cadena_arc
        arc_lst.write(escritura)
        arc_lst.close()
    # else:
    #     print("Error en la linea {}".format(no_linea))
        