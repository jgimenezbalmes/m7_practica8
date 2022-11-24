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

        datos=(nom_professor,cognom_professor,edat,idpersona)
        cursor.execute(query,datos)
        conexion.commit()
        actualizar=cursor.rowcount
        print(f'Registro actualizado: {actualizar}')

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
actualizar()