#ESTRUCTURA IF
robots = ["Nomad","Ponginator","Alfred"]
for robot in robots:
        if robot=="Nomad":
                print("This is Nomad")
        else:
                print(robot + " is not Nomad")
#LOOPS

#FOR LOOP
robots = ["Nomad","Ponginator","Alfred"]
for robot in robots: print(robot)

for num,robot in enumerate(robots): print(num,robot) #Enumera los robots

#WHILE LOOPS
count = 1
while count < 5: print(count)
count = count + 1
