#--Roberts-Novikovs--
#Studenta apliecības nr. rn25007

# B25. Sastādīt programmu, kura saskaita un atņem racionālus skaitļus, racionālos skaitļus uzdodot kā divu veselu
# skaitļu pāri (1/3 tiek uzdota kā divi skaitļi 1 un 3). Rezultātam jābūt kā nesaīsināmam daļskaitlim. Uzrakstīt funkciju,
# kas saskaita 2 racionālus skaitļus un funkciju, kas pārveido racionālu skaitli par nesaīsināmu daļskaitli.

skaitlis1 = [8, 18]
skaitlis2 = [18, 6]
vienadSk1 = skaitlis1.copy() #vienādots skaitlis 1
vienadSk2 = skaitlis2.copy() #vienādots skaitlis 2
dalijumaSumma = []
dalamais1 = 0
dalamais2 = 0
saisinataDala = []
dalamaisSummai = 0
dalamaisStarpibai = 0

def saisinats(x, y):
    dalijumaSumma = x
    dalijumaStarpiba = y 
    for i in range(1, 100000):
        if(float(dalijumaSumma[0]) / i == float(dalijumaSumma[0]) // i and 
           float(dalijumaSumma[1]) / i == float(dalijumaSumma[1]) // i ):         #atrod lielāko kopīgo dalītāju
            dalamaisSummai = i
        if(float(dalijumaStarpiba[0]) / i == float(dalijumaStarpiba[0]) // i and 
           float(dalijumaStarpiba[1]) / i == float(dalijumaStarpiba[1]) // i ):         #atrod lielāko kopīgo dalītāju
            dalamaisStarpibai = i
        
        saisinataDalaSum = dalijumaSumma.copy()
        saisinataDalaStarp = dalijumaStarpiba.copy()

        saisinataDalaSum = [dalijumaSumma[0] / dalamaisSummai, dalijumaSumma[1] / dalamaisSummai]
        saisinataDalaStarp = [dalijumaStarpiba[0] / dalamaisStarpibai, dalijumaStarpiba[1] / dalamaisStarpibai]
    return(saisinataDalaSum, saisinataDalaStarp, dalamaisSummai, dalamaisStarpibai)

def saskaitit(x, y):
    skait1, sauc1 = x
    skait2, sauc2 = y
    summa = [skait1+skait2, sauc1]
    return(summa)

def atnemt(x, y):
    skait1, sauc1 = x
    skait2, sauc2 = y
    starpiba = [skait1-skait2, sauc1]
    return(starpiba)

print("Sākotnējās daļas: ", skaitlis1, skaitlis2)

if skaitlis1[1] != skaitlis2[1]:  #ja ir atšķirīgi mainīgie, tad abas daļas reizina ar otras mainīgo, lai tos novienādotu
    vienadSk1[0] = skaitlis1[0] * skaitlis2[1]
    vienadSk1[1] = skaitlis1[1] * skaitlis2[1]
    vienadSk2[0] = skaitlis2[0] * skaitlis1[1]
    vienadSk2[1] = skaitlis2[1] * skaitlis1[1]

dalijumaSumma = saskaitit(vienadSk1, vienadSk2)
dalijumaStarpiba = atnemt(vienadSk1, vienadSk2)
print("Novienādotas daļas: ", vienadSk1, vienadSk2)
print(vienadSk1, " + ", vienadSk2, " = ", dalijumaSumma)
print(vienadSk1, " - ", vienadSk2, " = ", dalijumaStarpiba)

saisinataDalaSum, saisinataDalaStarp, dalamaisSummai, dalamaisStarpibai = saisinats(dalijumaSumma, dalijumaStarpiba)

print("Kopīgais dalītājs summai = ", dalamaisSummai, " | Starpībai = ", dalamaisStarpibai)

print("Saīsināta sumētā daļa = ", saisinataDalaSum)
print("Saīsināta daļu starpība = ", saisinataDalaStarp)
print("-----------------------------------------------")
