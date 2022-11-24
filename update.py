import psycopg2

# Funcion Actualizar Tabla
def actualizar():
    try:
        # Conectarse a la base de datos db_crud
        conexion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="db_crud",
            port="5432"
        )
        cursor = conexion.cursor()
        # Seleccionar la tabla personas
        tabla_personas = "select * from personas"

        cursor.execute(tabla_personas)
        # Recuperamos todos los campos de la tabla personas
        personas_existentes = cursor.fetchall()

        print("Tabla Personas: ")
        # Recorrer la tabla personas e imprimir por pantalla
        for row in personas_existentes:
            print(row)
        # SQL Actualizar la tabla con todos los campos
        query = "UPDATE personas set nom_professor=%s,cognom_professor=%s,edat=%s WHERE professor_id=%s"
        # Escribir por pantalla los nuevos valores en el campo
        idpersona = input('Ingrese id de la persona a editar: ')
        nom_professor=input('ingrese nombre del Profesor: ')
        cognom_professor=input('Ingrese apellido del Professor: ')
        edat=input('Ingrese edad: ')
        # Guardar los nuevos valores
        datos=(nom_professor,cognom_professor,edat,idpersona)
        # Ejecutar el query y añadir los datos
        cursor.execute(query,datos)
        # Guardar los cambios añadidos
        conexion.commit()
        # Actualizar el contador de registros que tiene la tabla
        actualizar=cursor.rowcount
        print(f'Registro actualizado: {actualizar}')
        # SQL para mostrar la tabla y ver los cambios realizados
        tabla_personas = "select * from personas"
        # Ejecutar el sql
        cursor.execute(tabla_personas)
        # Recuperamos todos los campos de la tabla personas
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas existentes: ")
        # Recorremos la tabla y mostramos los campos que hay en ese momento
        for row in personas_existentes:
            print(row)

        cursor.close()
        conexion.close()
    # En caso de que ocurre un error al conectarse al PostgresSQL
    except(Exception, psycopg2.Error) as error:
        print("Error al conectarse con PostgresSQL: " + error)
    finally:
        # En caso de que se haga la conexion
        if conexion:
            cursor.close()
            conexion.close()
            print("PostgreSQL conexion cerrada")
actualizar()

def insert_values():
    try:
        # Conectarse a la base de datos db_crud
        conexion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="db_crud",
            port="5432"
        )
        cursor = conexion.cursor()

        # Seleccionar la tabla personas
        tabla_personas = "select * from personas"
        # Ejecutar el sql para mostrar las tablas
        cursor.execute(tabla_personas)
        # Recuperamos todos los campos de la tabla personas
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas a insertar: ")
        # Recorrer la tabla personas e imprimir por pantalla
        for row in personas_existentes:
            print(row)
        # Insertar Nuevos valores a la tabla
        sql = "INSERT INTO personas(nom_professor,cognom_professor,edat) VALUES(%s,%s,%s)"
        # Escribir por pantalla los nuevos valores en el campo
        nom_professor = input('ingrese nombre del Profesor: ')
        cognom_professor = input('Ingrese apellido del Professor: ')
        edat = input('Ingrese edad: ')
        # Guardar los nuevos valores
        datos = (nom_professor, cognom_professor, edat)
        # Ejecutar el sql y añadir los valores
        cursor.execute(sql, datos)
        # Guardar cambios
        conexion.commit()
        # SQL para mostrar la tabla persona con los
        tabla_personas = "select * from personas"
        cursor.execute(tabla_personas)
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas existentes: ")
        for row in personas_existentes:
            print(row)
        cursor.close()
        conexion.close()
    except(Exception, psycopg2.Error) as error:
        print("Error al conectarse con PostgresSQL: " + error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("PostgreSQL conexion cerrada")
insert_values()