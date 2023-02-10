print("......................................")
print("....... VALOR NOTA DEFINITIVA ........")
print("......................................")

#input

np = int(input("digite el valor de la nota procedimental: "))
nc = int(input("digite el valor de la nota cognitiva: "))
na = int(input("digite el valor de la nota actitudinal: "))
au = int(input("digite el valor de la nota autoevaluación: "))
bi = int(input("digite el valor de la nota bimestral: "))

#processing

nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)

#output

print("......................................")
print("............. RESULTADOS .............")
print("......................................")

print("Resultados NOTA DEFINITIVA " + str(nd))