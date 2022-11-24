import psycopg2
# Funcion Eliminar tabla
def eliminar():
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
        # Ejecutamos el sql
        cursor.execute(tabla_personas)
        # Recuperamos todos los campos de la tabla personas
        personas_existentes = cursor.fetchall()

        print("Tabla Personas: ")
        # Recorrer la tabla personas e imprimir por pantalla
        for row in personas_existentes:
            print(row)

        # SQL Eliminamos la tabla con el id
        sql = 'DELETE FROM personas WHERE professor_id=%s'
        # Escribir por pantalla los nuevos valores en el campo
        id_professor = input('Ingrese el id del registro a eliminar: ')
        # Ejecutamos el sql y el id a eliminar
        cursor.execute(sql, id_professor)
        # Guardamos los cambios
        conexion.commit()
        # Hacemos un conteo de los registros que hay en la tabla
        registro_eliminado = cursor.rowcount

        print(f'registros eliminados: {registro_eliminado}')
        # Seleccionamos la tabla personas
        tabla_personas = "select * from personas"
        # Ejecutamos el SQL
        cursor.execute(tabla_personas)
        # Obtenemos la tabla persona con todos los campos creados en ese momento
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas existentes: ")
        # Recorremos la tabla persona e imprimimos los campos
        for row in personas_existentes:
            print(row)
        # Cerramos la conexion
        cursor.close()
        conexion.close()
    # En caso de que no se conecte a la base de datos
    except(Exception, psycopg2.Error) as error:
        print("Error al conectarse con PostgresSQL: " + error)
    finally:
        # Si se conecta cerramos la conexion
        if conexion:
            cursor.close()
            conexion.close()
            print("PostgreSQL conexion cerrada")
eliminar()
