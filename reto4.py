
def salario_basico (n1,n2):
  if n1 > 40: 
    he = n1 - 40
    vhe = n2*1.5
    valorhora_extra = he*vhe
    valorhora = 40*n2
  else:
    valorhora = n1*n2
    valorhora_extra = 0
  sb = valorhora+valorhora_extra
  print(valorhora)
  print(valorhora_extra)
  print(sb)
  return (sb)

def des_psp(sb):
    parafiscales=sb*0.09
    salud= sb*0.04
    pension=sb*0.04
    total_psp= parafiscales+salud+pension
    print (parafiscales)
    print (salud)
    print (pension)
    print (total_psp)
    print (sb-total_psp)
    return (parafiscales,salud,pension,total_psp)

def proviciones(sb):
    prima=sb*0.0833
    cesantias=sb*1*0.0833
    incesantias=sb*0.01
    vacaciones=sb*0.0417
    print (prima)
    print (cesantias)
    print (incesantias)
    print (vacaciones)
    return prima,cesantias,incesantias,vacaciones 

n1 = int(input("digite el numero de horas trabajadas: "))
n2 = int(input("digite el valor de la hora: "))
s1 = salario_basico(n1, n2)
des_psp(s1)
proviciones(s1)
