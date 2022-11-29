import psycopg2

connexio = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="db_crud",
    port="5432"
)

cursor = connexio.cursor()

def read():
    try:
        # Seleccionamos la BD personas
        sql = ("SELECT * FROM personas")
        # Ejecutamos nuestro SQL
        cursor.execute(sql)

        personas_existentes = cursor.fetchall()

        print("Tabla Personas: ")
        for row in personas_existentes:
            print(row)
        # Cerramos el Curso en suo
        cursor.close()
        # Hacemos un cambio de los cambios realizados (en este caso, la selección de la Tabala "personas")
        connexio.commit()
    # En cas que es doni error, guardem el text d'error que ens dona a la variable "error", i fem print
    # Si se da el caso de saltarnos un error, guardaremos el mensaje de error
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # Finalment, si la connexió no s'ha tancat, la tanquem
    finally:
        if connexio is not None:
            connexio.close()

