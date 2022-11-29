#Importem els quatre arxius que hem creat per a fer el CRUD
import create
import delete
import read
import update

valor = int(input("Quina funcio vols provar? \n1) Crear taula \n2) Llegir taula \n3)Modificar dades \n4)Inserir dades \n5)Borrar dades\n"))

if (valor == 1):
    #Cridem a la funcio que crea la taula...
    create.crea_taula()
    read.read()

elif (valor ==2):
    #La funcio que llegeix els valors... (la repetim per a que surti la taula)
    read.read()

elif (valor==3):
    #La que fa un update...
    update.actualizar()

elif (valor==4):
    #Cridem a la funcio que inserta valors...
    update.insert_values()

elif (valor==5):
    #I la que elimina valors
    delete.eliminar()

else:
    print("Siusplau introdueix un valor entre 1 i 5")
