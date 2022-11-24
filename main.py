#Importem els quatre arxius que hem creat per a fer el CRUD
import create
import delete
import read
import update

#Cridem a la funcio que crea la taula...
create.crea_taula()
#La funcio que llegeix els valors... (la repetim per a que surti la taula)
read.read()
#Cridem a la funcio que inserta valors...
update.insert_values()
read.read()
#La que fa un update...
update.actualizar()
read.read()
#I la que elimina valors
delete.eliminar()
read.read()