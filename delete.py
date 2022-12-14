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
        #cursor_factory = extras.RealDictCursor

        cursor = conexion.cursor()
        # Seleccionar la tabla personas
        tabla_personas = "select * from personas"
        # Ejecutar el sql
        cursor.execute(tabla_personas)
        # Obtener la tabla existente
        personas_existentes = cursor.fetchall()

        print("Mostrar Tabla Personas: ")
        # Recorrer la tabla e imprimir los datos que tenga la tabla
        for row in personas_existentes:
            print('\tprofessor_id' + '\tnom_professor' + '\tcognom_professor' + '\tedat')
            print("\t\t" + str(row[0]) + "\t\t\t" + str(row[1]) + "\t\t\t " + str(row[2]) + "\t\t\t\t" + str(row[3]))
        # Eliminar la tabla personas por el id
        sql = "DELETE FROM personas WHERE professor_id=%s"
        # Preguntar la tabla a eliminar
        id_persona = input("Ingrese el id del registro a eliminar: ")
        # Executar el sql y el id a eliminar, dividimos el valor id_persona en cada espacio que
        # cuando el id sobrepasa el 9 ya no deja eliminar ningun profesor mas ya que hay 2 valores
        # para ello se soluciona con un .split()
        cursor.execute(sql, id_persona.split())
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
            print('\tprofessor_id' + '\tnom_professor' + '\tcognom_professor' + '\tedat')
            print("\t\t" + str(row[0]) + "\t\t\t" + str(row[1]) + "\t\t\t" + str(row[2]) + "\t\t\t" + str(row[3]))
        # Cerrar la conexion
        cursor.close()
        conexion.close()
    # En caso de que no se conecte a la base de datos
    except(Exception, psycopg2.Error) as error:
        print(error)
    finally:
        # En caso de que se conecte se cierra la conexion
        if conexion:
            valor = input("\nQuieres eliminar otro professor(Si/No) ? ")
            if(valor.lower()=="si"):
                eliminar()
            else:
                print("No se elimina ningun professor mas.")
                cursor.close()
                conexion.close()
                print("PostgreSQL conexion cerrada")