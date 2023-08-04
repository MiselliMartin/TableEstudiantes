import sqlite3

def conectar():
    conexion = sqlite3.connect('estudiantes.db')
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion,cursor = conectar()
    sentencia = "CREATE TABLE IF NOT EXISTS Estudiantes(id INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL, nota INTEGER NOT NULL)"
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()
    return True

def consultarTabla():
    conexion, cursor = conectar()
    sentencia = "SELECT * FROM Estudiantes"
    resultado = cursor.execute(sentencia)
    return resultado

def consultarEstudiante(id):
    conexion, cursor = conectar()
    sentencia = f"SELECT * FROM Estudiantes WHERE id = {id}"
    resultado = cursor.execute(sentencia)
    resultado = resultado.fetchone()
    return resultado

def insertarDatos(datos):
    conexion, cursor = conectar()
    sentencia = "INSERT INTO Estudiantes VALUES(NULL,?,?,?)"
    cursor.execute(sentencia,datos)
    conexion.commit()
    return True

def actualizarNota(id, nota):
    conexion, cursor = conectar()
    sentencia = f"UPDATE Estudiantes SET nota = {nota} WHERE id = {id}"
    cursor.execute(sentencia)
    conexion.commit()
    return True

def eliminarDatos(id):
    conexion, cursor = conectar()
    sentencia = f"DELETE FROM Estudiantes WHERE id = {id}"
    cursor.execute(sentencia)
    conexion.commit()
    return True

def menu():
    conexion, cursor = conectar()
    print("""
    0: Salir
    1: Consultar tabla
    2: Consultar estudiante
    3: Insertar datos
    4: Actualizar nota
    5: Eliminar datos
    """)
    opcion = int(input("¿Qué desea hacer?: "))
    while True:
        if opcion == 0:
            conexion.close()
            print("Adiós.")
            break
        elif opcion == 1:
            resultado = consultarTabla()
            for estudiante in resultado:
                print(f"""
                Id: {estudiante[0]}
                Nombre: {estudiante[1]}
                Email: {estudiante[2]}
                Nota: {estudiante[3]}
                """)
        elif opcion == 2:
            id = int(input("Id del estudiante: "))
            resultado = consultarEstudiante(id)
            print(f"""
            Id: {resultado[0]}
            Nombre: {resultado[1]}
            Email: {resultado[2]}
            Nota: {resultado[3]}
            """)
        elif opcion == 3: 
            nombre=input("Ingrese el nombre del estudiante: ")
            email=input("Ingrese el email del estudiante: ")
            nota= int(input("Ingrese la nota del estudiante: "))
            datos = (nombre, email, nota)
            insertarDatos(datos)
        elif opcion == 4:
            id = int(input("Id del estudiante a actualizar: "))
            nota=input("Ingrese la nueva nota: ")
            actualizarNota(id, nota)
        elif opcion == 5:
            id = int(input("Ingrese el Id del estudiante a eliminar: "))
            eliminarDatos(id)
        print("""
        0: Salir
        1: Consultar tabla
        2: Consultar estudiante
        3: Insertar datos
        4: Actualizar nota
        5: Eliminar datos
        """)
        opcion = int(input("¿Qué desea hacer?: "))
        
def principal():
    menu()

if __name__ == "__main__":
    principal()