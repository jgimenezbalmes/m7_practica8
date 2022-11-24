#Importem el paquet de psycopg2
import psycopg2
#Fem la connexio amb la base de dades
connexio = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="db_crud",
    port="5432"
)

# Obrim un cursor amb la connexio que acabem de definir del servidor
cursor = connexio.cursor()

# Fem la funcio de crear taula...
def crea_taula():

    #Fem un try-catch(en aquest cas "except") per tal de poder detectar possibles errors
    try:
        #Fem un "statement" SQL, on podem ficar qualsevol comanda de SQL que volguem, en aquest cas, creem la
        #taula personas, amb les quatre columnes que es poden veure. El id sera una clau primaria que es generara
        #automaticament.
        sql = ("""CREATE TABLE personas (professor_id SERIAL PRIMARY KEY,
                        nom_professor VARCHAR(255) NOT NULL,
                        cognom_professor VARCHAR(255) NOT NULL,
                        edat INTEGER NOT NULL) 
            """)
        # Executem el sql que hem escrit abans
        cursor.execute(sql)
        # Tanquem el cursor que hem fet servir
        cursor.close()
        # Fem commit dels canvis que s'han produit (és a dir, s'ha generat la taula)
        connexio.commit()
        #Fiquem un missatge de que s'ha creat la taula de forma adient
        print("Creada taula 'personas' de forma satisfactoria")
    #En cas que es doni error, guardem el text d'error que ens dona a la variable "error", i fem print
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    #Finalment, si la connexió no s'ha tancat, la tanquem
    finally:
        if connexio is not None:
            connexio.close()

