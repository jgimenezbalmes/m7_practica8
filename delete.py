import psycopg2
# Funcion Eliminar Tabla por el id
def eliminar():
    try:
        # Hacer la conexion a la base de datos
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
        # Ejecutar el sql
        cursor.execute(tabla_personas)
        # Obtener la tabla existente
        personas_existentes = cursor.fetchall()

        print("Tabla Personas: ")
        # Recorrer la tabla e imprimir los datos que tenga la tabla
        for row in personas_existentes:
            print(row)
        # Eliminar la tabla personas por el id
        sql = 'DELETE FROM personas WHERE professor_id=%s'
        # Preguntar la tabla a eliminar
        id_professor = input('Ingrese el id del registro a eliminar: ')
        # Executar el sql y el id a eliminar
        cursor.execute(sql, id_professor)
        # Guardar los cambios
        conexion.commit()
        # Hacer un conteo del registro que tiene la tabla
        registro_eliminado = cursor.rowcount

        print(f'registros eliminados: {registro_eliminado}')
        # Seleccionar la tabla personas
        tabla_personas = "select * from personas"
        # Ejecutar el sql
        cursor.execute(tabla_personas)
        # Obtener la tabla
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas existentes: ")
        # Recorrer la tabla existente e imprimir los datos que hay en ese momento
        for row in personas_existentes:
            print(row)
        # Cerrar la conexion
        cursor.close()
        conexion.close()
    # En caso de que no se conecte a la base de datos
    except(Exception, psycopg2.Error) as error:
        print("Error al conectarse con PostgresSQL: " + error)
    finally:
        # En caso de que se conecte se cierra la conexion
        if conexion:
            cursor.close()
            conexion.close()
            print("PostgreSQL conexion cerrada")
eliminar()
