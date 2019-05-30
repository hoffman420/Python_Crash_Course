robots = ["nomad","Ponginator","Alfred"]
print (robots)

print (robots [0]) #imprime la posicion 0 de la lista
print (robots [-1]) #imprime la posicion -1
print (robots [1:3]) #imprime las dos posiciones

more_bots = robots+['Roomba','Neato','InMoov'] #Concatenacion de las listas
print (more_bots)

more_bots[3] = 'ASIMO' #Agrega un nuevo elemento en la lista
print (more_bots)

more_bots[3:5] = [] #Quita elementos de la lista
print (more_bots)

a,b = more_bots[0:2]
print (a)
print (b)
