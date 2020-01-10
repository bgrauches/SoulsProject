from enemigos import enemigos
from moves import moves

#DECLARAMOS enemigo
e1 = enemigos("Enterrador", 1000, 100, 70, 20)
e2 = enemigos("El bromas", 500, 200, 20, 70)
e3 = enemigos("Lord Maik", 1500, 125, 50, 50)

#DEFINIMOS MOVIMIENTOS ENTERRADOR
m1E = moves("GOLPE DE PALA", 50, 50)
m2E = moves("PALA GIRATORIA", 70, 20)
m3E = moves("PUÑETAZO", 60, 30)
m4E = moves("EM-PALA-CIÓN", 90, 40)

e1.addMove(m1E, m2E, m3E, m4E)

#DEFINIMOS MOVS BROMAS
m1B = moves("PUÑALASO",)
m2B = moves("CORTE",)
m3B = moves("NAVAJASO",)
m4B = moves("",)