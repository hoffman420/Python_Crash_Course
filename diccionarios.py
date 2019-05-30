Nomad = {'type':'rover',
        'color':'black',
        'processor':'JetsonTX1'}
print(Nomad['type']) #imprime el type de nomad

BARB = {'type':'test-bed','color':'black','type':'wheeled'}
print (BARB) #imprime toda variable BARB

myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
print (myRobots) #imprime toda la variable y concatena a otra

myRobots['Llamabot'] = 'Getting to it'
print (myRobots) #imprime la variable mas la nueva palabra

workingRobots = myRobots.copy()
print (workingRobots) #imprime la variable y con el .copy se copia

otherRobots = {'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}
myRobots.update(otherRobots)
print (myRobots)
