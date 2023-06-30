from datetime import datetime

Nombre=[] #ValidarNombre
Rut=[] #ValidarNumero
FechaNacimiento=[] #ValidarFecha
Categoria=[] #ValidarCategoria
NombreContrincante=[]#ValidarNombre
Correo=[] #ValidarCorreo
Edad=[] #Validaredad
RutContrincante=[]
Telefono=[]

def ValidarNumero(tipo,texto,valormin=None,valormax=None):
    while True:
        try:
            valor=tipo(input(texto))
            if valormin!=None and valormax!=None:
                if valormin<=valor<=valormax:
                    break
                else:
                    print("Rango incorrecto!")
            elif valormin!=None:
                if valormin<=valor:
                    break
                else:
                    print(f"Ingrese un valor mayor o igual a {valormin}")
            elif valormax!=None:
                if valormax>=valor:
                    break
                else:
                    print(f"Ingresa un valor menor o igual a {valormax}")
            else:
                break
        except:
            print("Ingresa solamente numeros!")
    return valor

def ValidarEdad(tipo,texto,valormin=None,valormax=None):
    while True:
        try:
            valor=tipo(input(texto))
            if valormin!=None and valormax!=None:
                if valormin<=valor<=valormax:
                    break
                else:
                    print("Rango de edad incorrecto!")
            elif valormin!=None:
                if valormin<=valor:
                    break
                else:
                    print(f"Ingrese una edad mayor o igual a {valormin}")
            elif valormax!=None:
                if valormax>=valor:
                    break
                else:
                    print(f"Ingresa una edad menor o igual a {valormax}")
            else:
                break
        except:
            print("Ingresa solamente numeros!")
    return valor

def ValidarTelefono(tipo,texto,lmin=None):
    while True:
        try:
            telefono=tipo(input(texto))
            if len(str(telefono))==lmin:
                break
            else:
                print(f"El telefono debe tener {lmin} digitos!")
        except:
            print("Ingresa solo numeros!")
    return telefono
    
    
def ValidarNombre(texto,valormin=None):
    while True:
        nombre=input(texto).upper()
        if valormin!=None:
            if valormin<=len(nombre):
                break
            else:
                print(f"El nombre debe tener como minimo {valormin} caracteres!")
    return nombre

def ValidarCorreo(texto,valormin=None):
    while True:
        correo=input(texto).lower()
        flag=False
        for i in correo:
            if i=="@":
                flag=True
        if flag:
            if valormin!=None:
                if valormin<=len(correo):
                    break
                else:
                    print(f"Por favor ingresa un correo con minimo {valormin} caracteres de largo!")
        else:
            print("Todo correo tiene un @. Vuelve a ingresarlo!")
    return correo

def ValidarCategoria(texto):
    while True:
        categoria=input(texto).upper()
        if categoria=="ORO" or categoria=="PLATA" or categoria=="BRONCE":
            break
        else:
            print("Ingresa una categoria correcta!")
    return categoria

def ValidarFecha(texto):
    while True:
        try:
            fecha=(input(texto))
            datetime.strptime(fecha,'%d-%m-%Y')
            break
        except:
            print("Ingrese la fecha como se te pide!")
    return fecha

def ValidarContrincante(run): 
    if run not in Rut:
        RutContrincante.append(run)
    else:
        print("Ya hay un jugador con ese rut")

def BuscarParticipante(run):
    if run in Rut:
        indice=Rut.index(run)
        print(f" Los datos de este participante son:\nRut: {Rut[indice]}\nNombre: {Nombre[indice]}\nCategoria: {Categoria[indice]}\nTelefono: {Telefono[indice]}\nCorreo: {Correo[indice]}")
    else:
        print("No hay datos con el rut ingresado")

def BuscarPareja(run):
    if run in Rut:
        indice=Rut.index(run)
        print(f"De acuerdo a tu rut: {run}. Tu pareja es: rut: {RutContrincante[indice]}\t Nombre: {NombreContrincante[indice]}")
    else:
        print("No hay registro con ese rut!")
    
def menuprincipal():
    while True:
        print("- Campeonato -")
        print("1.- Grabar")
        print("2.- Buscar Datos")
        print("3.- Imprimir Parejas")
        print("4.- Salir")
        opc=ValidarNumero(int,"Ingrese su opcion --> ",1,4)
        if opc==1:
            print(" - Ingreso de participante - ")
            nombre=ValidarNombre("Imgrese su nombre: ",2)
            Nombre.append(nombre) 
            run=ValidarNumero(int,"Ingrese su rut sin puntos ni guiones ni digito verificador: ",3000000,25999999)
            Rut.append(run)
            telefono=ValidarTelefono(int,"Ingrese su telefono (9 digitos): ",9)
            Telefono.append(telefono)
            edad=ValidarEdad(int," Ingrese su edad: ",None,80)
            Edad.append(edad)
            fecha=ValidarFecha("Ingrese su fecha de nacimiento (DD-MM-YYYY): ")
            FechaNacimiento.append(fecha)
            correo=ValidarCorreo("Ingresa tu correo electronico: ",6)
            Correo.append(correo)
            categoria=ValidarCategoria("Ingrese la categoria por la que compite [ORO-PLATA-BRONCE]: ")
            Categoria.append(categoria)
            runcontrincante=ValidarNumero(int,"Ingrese el rut de su contrincante sin puntos ni guiones ni digito verificador: ",3000000,25999999)
            ValidarContrincante(runcontrincante)
            nombrecontrincante=ValidarNombre("Ingrese el nombre de su contrincante: ",2)
            NombreContrincante.append(nombrecontrincante)
            print("Datos ingresados correctamente!")
        elif opc==2:
            if len(Nombre)!=0:
                rut=ValidarNumero(int,"Ingrese el rut a consultar sin puntos ni guiones ni digito verificador: ",3000000,25999999)
                BuscarParticipante(rut)
            else:
                print("No se ha ingresado ningun concursante aun")
        elif opc==3:
            if len(Nombre)!=0:
                rut1=ValidarNumero(int,"Ingrese el rut para consultar pareja sin puntos ni guiones ni digito verificador: ",3000000,25999999)
                BuscarPareja(rut1)
            else:
                print("No hay registro de jugadores aun")
        else:
            print("Saliendo el sistema...")
            break

menuprincipal()



                

            

