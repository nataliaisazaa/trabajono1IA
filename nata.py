#Adgoritmos - Natalia Isaza

l = [1, 10, 4, 2, 4, 3, 3, 1, 1, 3]

#Calcular el promedio
promedio = sum(l) / len(l)
print('Calculando la moda y el promedio')
print (l)
print ("largo ", len(l), ", promedio:", promedio)

# Calcular la moda
repeticiones = 0
for i in l:
    apariciones = l.count(i)
    if apariciones > repeticiones:
        repeticiones = apariciones

modas = []
for i in l:
    apariciones = l.count(i)
    if apariciones == repeticiones and i not in modas:
        modas.append(i)

print ("moda:", modas)

#Calcular la mediana
l.sort()

if len(l) % 2 == 0:
    n = len(l)
    mediana = ((l[n//2-1] + l[n // 2]) // 2)
else:
    mediana = l[len(l) // 2]
print('\n')
print('Calculando la mediana')
print (l)
print ('mediana:', mediana)

#calcular la varianza
def print_grades(grades):
    for grade in grades:
        print (grade)


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = float(sum_of_grades) // len(grades)
    return average


# Para calcular la varianza restamos a cada puntancion la media y
# los sumamos, lo elevamos al cuadrado y lo divimos entre 2
def grades_variance(scores, average):
    sumatorio = 0
    for data in scores:
        sumatorio += (average - float(data)) ** 2
    variance = float(sumatorio) // len(grades)
    return variance


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print('\n')
print('Calculando la varianza')
print (grades)
print ('varianza:',grades_variance(grades, grades_average(grades)))

#calcular la covarianza
import statistics as stats #El módulo statistics agrupa un conjunto de funciones para cálculo estadístico.
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print('\n')
print('Calculando la covarianza')
print (edades)
print('Covarianza',stats.pstdev(edades))

