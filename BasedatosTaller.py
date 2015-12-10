import sqlite3 as dbapi
from gi.repository import Gtk


# Version de api
# print(dbapi.apilevel)
# De 0 a 3 como de seguro e o modulo paa o uso de fios
# print(dbapi.threadsafety)
# Indica a sintaxe para a insercion de parametros de forma dinamica
# print(dbapi.paramstyle)

# cursor.execute("""create table taller(matricula text primary key,vehiculo text, kilometros integer,Fechareparacion text,Cliente text, CIF text, Numero integer, Direccion text)""")
# cursor.execute(""" insert into empleados values('12345a','Johana',600,'puta')""")
# cursor.execute("""select * from empleados""")
# for resultado in cursor:
#        print("Dni: "+resultado[0]+", Nome: "+resultado[1]+", Sueldo: "+str(resultado[2])+", Departamento: "+resultado[3])
# bd.close()


class taller:
    bd = dbapi.connect("basedatos.dat")
    fichero = "Taller.glade"
    print(bd)
    cursor = bd.cursor()
    builder = Gtk.Builder()
    builder.add_from_file(fichero)
    window = builder.get_object("taller")

    def __init__(self):
        self.window.show_all();
        sinais = {"on_insertar_clicked": self.on_insertar_clicked,
                  "on_consultar_clicked": self.on_consultar_clicked,
                  "on_modificar_clicked": self.on_modificar_clicked,
                  "on_borrar_clicked": self.on_borrar_clicked,
                  "on_FiestraPrincipal_destroy": Gtk.main_quit}

        self.builder.connect_signals(sinais)
        # entrys
        self.txtmatricula = self.builder.get_object("txtmatricula")
        self.txtvehiculo = self.builder.get_object("txtvehiculo")
        self.txtkilometros = self.builder.get_object("txtkilometros")
        self.txtfecha = self.builder.get_object("txtfecha")
        self.txtcliente = self.builder.get_object("txtcliente")
        self.txtcifnif = self.builder.get_object("txtcifnif")
        self.txttelf = self.builder.get_object("txttelf")
        self.txtdireccion = self.builder.get_object("txtdireccion")
        self.fiestra = self.builder.get_object("taller")

    def on_borrar_clicked(self, txtmatricula):
        txtmatricula = self.txtmatricula.get_text()
        print("matricula recojida, procediendo a borrar")
        self.cursor.execute("delete from taller where matricula ='"+txtmatricula+"'")
        print("Borrado")
        self.bd.commit()

    def on_consultar_clicked(self, consultar):
        print("Buscando")
        buscar=self.cursor.execute("Select * from taller")
        print(buscar)
        self.bd.commit()

    def on_modificar_clicked(self, modificar):
        txtvehiculo = self.txtvehiculo.get_text()
        txtkilometros = self.txtkilometros.get_text()
        txtfecha = self.txtfecha.get_text()
        txtcliente = self.txtcliente.get_text()
        txtcifnif = self.txtcifnif.get_text()
        txttelf = self.txttelf.get_text()
        txtdireccion = self.txtdireccion.get_text()
        txtmatricula = self.txtmatricula.get_text()
        print("Esperando datos")
        self.cursor.execute("update taller set vehiculo ='"+txtvehiculo+"',kilometros='"+txtkilometros+"',fechareparacion='"+txtfecha+"'"
            ",cliente='"+txtcliente+"',cif='"+txtcifnif+"',numero='"+txttelf+"',direccion='"+txtdireccion+""
            ",cliente='"+txtcliente+"',cif='"+txtcifnif+"',numero='"+txttelf+"',direccion='"+txtdireccion+""
                                                                            "' where matricula='"+txtmatricula+"'")
        print("Buscado")
        self.bd.commit()
    def on_insertar_clicked(self, insertar):
        txtmatricula = self.txtmatricula.get_text()
        txtvehiculo = self.txtvehiculo.get_text()
        txtkilometros = self.txtkilometros.get_text()
        txtfecha = self.txtfecha.get_text()
        txtcliente = self.txtcliente.get_text()
        txtcifnif = self.txtcifnif.get_text()
        txttelf = self.txttelf.get_text()
        txtdireccion = self.txtdireccion.get_text()

        print("inserte")
        self.cursor.execute(
            "insert into taller values('"+txtmatricula+"','"+txtvehiculo+"','"+txtkilometros+"','"+txtfecha+"','"
                                       ""+txtcliente+"','"+txtcifnif+"','"+txttelf+"','"+txtdireccion+"')")
        print("Insertado")
        self.bd.commit()

taller()
Gtk.main()