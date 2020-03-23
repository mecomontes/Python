import pylab
import matplotlib.pyplot as plt

class plan:
    id = 0
    tipo = ""
    destino = ""
    costo_plan = 0
    costo_vuelo = 0
    cupo = 0
    c_personas = 0
    clase_viaje = ""
    estado = ""

    def info(_self):
        print("Id: " + str(_self.id))
        print("Tipo: " + str(_self.tipo))
        print("Destino: " + str(_self.destino))
        print("Costo plan: " + str(_self.costo_plan))
        print('Costo vuelo: ' + str(_self.costo_vuelo))
        print('Cupo : ' + str(_self.cupo))
        print('Cantidad personas : ' + str(_self.c_personas))
        print('Clase del viaje : ' + str(_self.clase_viaje))
        print('Estado : ' + str(_self.estado))

    def cancelacion_de_plan(_self):
         self.estado = "cancelado"
    
    def graficos(_self):
        plt.hist(c_personas)
        



class empresa:
    nombre = ""
    ganancia = 0
    planes = {}
    clientes = {}
    vuelos={}


    def cargarplanes(_self):
        f = open('empresa.csv')
        ls = f.readline()
        ls = f.readlines()
        print(ls)
        f.close()
        
        for l in ls:
            data = l.split(";")
            idd = data[0]
            tipo = data[1]
            destino = data[2]
            cplan = data[3]
            cvuelo = data[4]
            cupo = data[5]
            c_personas = data[6]
            class_viaje = data[7]
            estado = data[8]
            
            plan1 = plan()
            plan1.id = int(idd)
            plan1.tipo = tipo
            plan1.destino = destino
            plan1.costo_plan = int(cplan)
            plan1.costo_vuelo = int(cvuelo)
            plan1.cupo = int(cupo)
            plan1.c_personas = int(c_personas)
            plan1.clase_viaje = class_viaje
            plan1.estado = estado

            _self.planes[plan.id] = plan1

    def guardar(_self):
        f = open("empresa.csv", "w")
        for i in _self.planes:
            cc = _self.planes[i]
            f.write('id'+";"+'tipo'+";"+'destino'+";"+'costo del plan'+";"+'costo del vuelo'+";"+'cupo max'+";"+'cantidad'+";"+'clase viaje'+";"+'estado'+"\n")
            f.write(str(cc.id) + ";" + cc.tipo + ";" + cc.destino + ";" + str(cc.costo_plan) + ";" + str(
                cc.costo_vuelo) + ";" + str(cc.cupo) + ";" + str(
                cc.c_personas) + ";" + cc.clase_viaje + ";" + cc.estado + "\n")
        f.close()

    def mostrarPlanes(_self):
        for i in _self.planes:
            print(30*"-")
            _self.planes[i].info()
            print(30*"-")

    def crear_plan(_self):
        try:
            idd = int(input("Identificador: "))
            tipo = input("Tipo (p o e): ")
            destino = input("Destino: ")
            cplan = input("Costo del plan: ")
            cvuelo = int(input('Costo del vuelo'))
            cupo = int(input('Cupo (max): '))
            c_personas = int(input('Cantidad de personas en el plan: '))
            class_viaje = input('Clase de viaje (n o i): ')
            estado = input('Estado del plan (abierto, ejecutado, cancelado): ')

            if (idd in _self.planes.keys()):
                print("Error: Plan ya existe")
            else:
                plan1 = plan()
                plan1.id = int(idd)
                plan1.tipo = tipo
                plan1.destino = destino
                plan1.costo_plan = int(cplan)
                plan1.costo_vuelo = int(cvuelo)
                plan1.cupo = int(cupo)
                plan1.c_personas = int(c_personas)
                plan1.clase_viaje = class_viaje
                plan1.estado = estado

                _self.planes[plan.id] = plan1

        except(ValueError):
            print("Error: Valor invalido")

    def paseo_excursion(_self):
        p=paseo
        ee=Excursion

        cli=int(input("quiere irse de paseo o excursion "))

        if cli==p:
            print("escoja la opcion 5")
        elif cli==ee:
            print("escoja la opcion 9")


    def cargar_clientes(_self):
        f = open("clientes.csv")
        ls = f.readlines()

        iddc=[]
        ccc=[]
        nombrec=[]
        edadc=[]
        
        for l in ls:
            data = l.split(";")
            iddc.append(data[0])
            ccc.append(data[1])
            nombrec.append(data[2])
            edadc.append(data[3])
        
        for i in range(len(iddc)):
            for j in range(i,len(iddc)):
                if edadc[j]>edadc[i]:
                    auxn=edadc[i]
                    edadc[i]=edadc[j]
                    edadc[j]=auxn
                    
                    auxn=iddc[i]
                    iddc[i]=iddc[j]
                    iddc[j]=auxn
                    
                    auxs=nombrec[i]
                    nombrec[i]=nombrec[j]
                    nombrec[j]=auxs
                    
                    auxn=ccc[i]
                    ccc[i]=ccc[j]
                    ccc[j]=auxn
                
        for i in range(len(iddc)):
            c = paseo()
            c.nombre = nombrec[i]
            c.cc = int(ccc[i])
            c.id_plan = int(iddc[i])
            c.edad = int(edadc[i])
            _self.clientes[c.id_plan] = c

    def guardarclientes(_self):
        f = open("clientes.csv", "w")
        for i in _self.clientes:
            cc = _self.clientes[i]
            f.write(str(cc.id_plan) + ";" + str(cc.edad) + ";" + str(cc.nombre) + ";" + "\n")
        f.close()

    def crear_cliente_paseo(_self):
        try:
            idd = int(input("Identificador del plan: "))
            cc = int(input("cc del cliente: "))
            nombre1 = input("ingrese su nombre:")
            edadd = int(input("ingrese su edad"))



            if (idd not in _self.planes.keys()):
                print("Error: Plan no existe")
            else:
                c = paseo()
                c.id_plan = int(idd)
                c.cc=int(cc)
                c.nombre = nombre1
                c.edad = edadd

                _self.clientes[paseo.id_plan] = plan

        except(ValueError):
            print("Error: Valor invalido")

    def mostrarcli(_self):
        for i in _self.clientes:
            _self.clientes[i].infocli()
            print("-----------------")

    def cargar_Excursiones(_self):
        f = open("excursiones.csv")
        ls = f.readlines()
        
        idde=[]
        cce=[]
        nombree=[]
        edade=[]
        
        for l in ls:
            data = l.split(";")
            idde.append(data[0])
            cce.append(data[1])
            nombree.append(data[2])
            edade.append(data[3])
        
        for i in range(len(idde)):
            for j in range(i,len(idde)):
                if edade[j]>edade[i]:
                    auxn=edade[i]
                    edade[i]=edade[j]
                    edade[j]=auxn
                    
                    auxn=idde[i]
                    idde[i]=idde[j]
                    idde[j]=auxn
                    
                    auxs=nombree[i]
                    nombree[i]=nombree[j]
                    nombree[j]=auxs
                    
                    auxn=cce[i]
                    cce[i]=cce[j]
                    cce[j]=auxn
       
        for i in range(len(idde)):
            e = Excursion()
            e.idexcursion = int(idde[i])
            e.nombre = nombree[i]
            e.cc = int(cce[i])
            e.edad = int(edade[i])
            _self.excursiones[e.idd] = e

    def mostrarExcursiones(_self):
        for i in _self.excursiones:
            _self.excursiones[i].info()
            print("-----------------")

    def guardarExcursiones(_self):
        f = open("excursiones.csv", "w")
        for i in _self.excursiones:
            c = _self.excursiones[i]
            f.write(str(c.idd) + ";" + str(c.nombre) + ";" + str(c.cc) + ";" + str(c.edad) + "\n")
        f.close()

    def crearExcursion(_self):
        try:
            idd = int(input("Identificador de la excursion: "))
            cc = int(input("ingrese su cedula: "))
            nombre = input('Ingrese el nombre de la excursion: ')
            edad = int(input("ingrese su edad: "))


            if (idd in _self.excursiones.keys()):
                print("Error: Excursion ya existe")

            else:
               e = Excursion()
               e.idexcursion = int(idd)
               e.nombre = nombre
               e.cc = int(cc)
               e.edad = int(edad)

               _self.excursiones[e.idexcursion] = e  # revisar

        except(ValueError):
            print("Error: Valor invalido")

    def cargarVuelos(_self):
        f = open("vuelos.csv")
        ls = f.readlines()
        for l in ls:
            data = l.split(";")
            idd = data[0]
            cupo_max = data[1]
            cupo_personas = data[2]
            destino = data[3]
            estado = data[4]
            puestos_libres = data[5]

            vuelo = Vuelo()
            vuelo.id = idd
            vuelo.cupo_max = int(cupo_max)
            vuelo.cupo_personas = int(cupo_personas)
            vuelo.destino = destino
            vuelo.estado = estado
            vuelo.puestos_libres = int(puestos_libres)

            _self.vuelo[vuelo.id] = vuelo

    def mostrarVuelos(_self):
        for i in _self.vuelos:
            _self.vuelos[i].info()
            print("-----------------")

    def guardarVuelos(_self):
        f = open("vuelos.csv", "w")
        for i in _self.vuelos:
            cc = _self.vuelos[i]
            f.write(
                str(cc.id) + ";" + str(cc.cupo_max) + ";" + str(cc.cupo_personas) + ";" + str(cc.destino) + ";" + str(
                    cc.estado) + ";" + str(cc.puestos_libres) + "\n")
        f.close()

    def crearVuelo(_self):
        try:
            idd = input("Identificador: ")
            cupo_max = int(input(' cupo máximo del avión'))
            cupo_personas = int(input('Cuántas personas  han abordado: '))
            destino = input('Destino: ')
            estado = input('Estado (en espera o lleno): ')
            puestos_libres = int(input('Cuántos puestos libres tiene: '))
            costo_pasaje = int(input("costo del pasaje: "))

            if (idd in _self.vuelos.keys()):
                print("Error: Vuelo ya existe")
            else:
                vuelo = Vuelo()
                vuelo.id = idd
                vuelo.cupo_max = int(cupo_max)
                vuelo.cupo_personas = int(cupo_personas)
                vuelo.destino = destino
                vuelo.estado = estado
                vuelo.puestos_libres = int(puestos_libres)
                vuelo.costo=int(costo_pasaje)

                _self.vuelos[vuelo.id] = vuelo

        except(ValueError):
            print("Error: Valor invalido")

class paseo:
    id_plan = 0
    cc  = 0
    nombre = ''
    edad = 0

    def infocli(_self):
        print("Id: " + str(_self.id_plan))
        print("cc: " +str(_self.cc))
        print("nombre: " + str(_self.nombre))
        print("edad: " + str(_self.edad))


class Excursion:
    idd= 0
    nombre = ''
    cc = 0
    edad = 0

    def infocli(_self):
        print("Id: " + str(_self.id_plan))
        print("cc: " +str(_self.cc))
        print("nombre: " + str(_self.nombre))
        print("edad: " + str(_self.edad))


class Vuelo:
    id = ''
    cupo_max = 0
    cupo_personas = 0
    destino = ''
    estado = ''
    puestos_libres = 0
    costo_pasaje = 0

    def info(_self):
        print("Id: " + str(_self.id))
        print("Cupo maximo: " + str(_self.cupo_max))
        print("Puestos ocupados: " + str(_self.cupo_personas))
        print("Destino: " + str(_self.destino))
        print('Estado: ' + str(_self.estado))
        print(('Puesto libres : ' + str(_self.puestos_libres)))
        print("costo del vuelo es: "+str(_self.costo_pasaje))





a = empresa()
a.nombre = "avianca"

op = -1

while (op != 0):
    print("avianca.com")
    print("1. Agregar Plan")
    print("2. Listar planes")
    print("3. guardar planes")
    print("4. cargar planes")
    print("5.escoga que tipo de viaje quiere")
    print("6. cargar cliente ")
    print("7.listar clientes ")
    print("8.guardar clientes ")
    print("9. agregar cliente a la excursion")
    print("10.listar clientes excursion")
    print("11.guardar excursion")
    print("12.cargar excursion")
    print("13. Agregar vuelo")
    print("14.listar vuelo ")
    print("15. cargar vuelos")
    print("16.guardar vuelos")
    print("17. Agregar cliente al paseo")
    print("0. Salir")
    try:
        op = int(input("Escoger opcion: "))
        if (op == 1):
            a.crear_plan()
        elif (op == 2):
            a.mostrarPlanes()
        elif (op == 3):
            a.guardar()
        elif (op == 4):
            a.cargarplanes()
        elif (op == 5):
            a.paseo_excursion()
        elif (op == 5):
            a.crear_cliente_paseo()
        elif (op == 6):
            a.cargar_clientes()
        elif (op == 7):
            a.mostrarcli()
        elif (op == 8):
            a.guardarclientes()
        elif (op == 9):
            a.crearExcursion()
        elif (op == 10):
            a.mostrarExcursiones()
        elif (op == 11):
            a.cargar_Excursiones()
        elif (op == 12):
            a.guardarExcursiones()
        elif (op == 13):
            a.crearVuelo()
        elif (op == 14):
            a.mostrarVuelos()
        elif (op == 15):
            a.cargarVuelos()
        elif (op == 16):
            a.guardarVuelos()
    except(ValueError):
        print("Error: Opcion invalida")