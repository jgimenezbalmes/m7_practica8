import psycopg2
# Connect to your postgres DB
connexio = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="db_crud",
    port="5432"
)

# Open a cursor to perform database operations
cursor = connexio.cursor()

def crea_taula():

    try:
        """ create tables in the PostgreSQL database"""
        sql = ("""CREATE TABLE personas (professor_id SERIAL PRIMARY KEY,
                        nom_professor VARCHAR(255) NOT NULL,
                        cognom_professor VARCHAR(255) NOT NULL,
                        edat INTEGER NOT NULL) 
            """)
        # create table one by one
        cursor.execute(sql)
        #for comanda in sql:
            #cursor.execute(comanda)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connexio.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connexio is not None:
            connexio.close()

crea_taula()