import random
"""
in1=input()
x=len(in1)
res=""
for i in range (x-1,-1,-1): #empieza ultimo digito, acaba en primer digito-1 y da salto de -1
  res=res+in1[i]
  
print(res.upper())


numeros=[[10,20,30,40]]

nombres=["Daniel","Hugo","Chino"]
print(nombres[1:3]) """

nombres=["Andrés","Sergio","Ketzali","Daniel"]
print(nombres)
nombres[2]="Sebastián"
print(nombres)
nombres_dos=["Ximena","Yazmin","Hugo"]
print(nombres_dos*3)
nombres_final=nombres+nombres_dos
print(nombres_final)
del nombres_final[0]
print(nombres_final)
del nombres_final[3]
print(nombres_final)

for i in range(0,len(nombres_final)):
  print(i)
  
for i in nombres_final:
  print(i)
  
for indice,elemento in enumerate(nombres_final):
  print(str(indice)+".- "+str(elemento))

nombres_final.append("Diego")
print(nombres_final)

nombres_final.insert(1,"Emily")
print(nombres_final)

print(nombres_final.index("Sebastián"))
random.shuffle(nombres_final)
print(nombres_final)

print(random.choice(nombres_final))


print("Sebastián" in nombres_final) #True
print("Andrés" in nombres_final) #False

perro=["Pastor Alemán","Negro","Grnade"]
perro_dos=["Pug","Blanco","Chico"]
print(perro)
print(perro_dos)

raza,color,tamanio=perro_dos
print(raza)
print(color)
print(tamanio)
