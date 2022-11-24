import psycopg2
def eliminar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="db_crud",
            port="5432"
        )
        cursor = conexion.cursor()

        tabla_personas = "select * from personas"
        cursor.execute(tabla_personas)
        personas_existentes = cursor.fetchall()

        print("Tabla Personas: ")
        for row in personas_existentes:
            print(row)

        sql = 'DELETE FROM personas WHERE professor_id=%s'
        id_professor = input('Ingrese el id del registro a eliminar: ')
        cursor.execute(sql, id_professor)
        conexion.commit()

        registro_eliminado = cursor.rowcount

        print(f'registros eliminados: {registro_eliminado}')
        tabla_personas = "select * from personas"
        cursor.execute(tabla_personas)
        personas_existentes = cursor.fetchall()

        print("\nTabla Personas existentes: ")
        for row in personas_existentes:
            print(row)git 

        cursor.close()
        conexion.close()

    except(Exception, psycopg2.Error) as error:
        print("Error al conectarse con PostgresSQL: " + error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("PostgreSQL conexion cerrada")
eliminar()
