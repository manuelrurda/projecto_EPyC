codigo_LST = []
codigo_HEX = ""

#Recibe la instruccion para almacenarla
def almacenar_codigo(CL,ins_h):
    ConL = hex(int(CL))[2:]
    Con_Loc = ConL.zfill(4)
    codigo_LST.append(Con_Loc.upper()+"    "+str(ins_h).upper())
    codigo_HEX = codigo_HEX + ins_h

#Recibe la instruccion en binario y la devuelve en hexadecimal
def transformar(instruccion):
    ins_transformada = int(instruccion, 2)
    ins_transformada = format(ins_transformada, "x")
    if len(ins_transformada)%2 != 0:
        ins_transformada = "0" + ins_transformada
    return ins_transformada
