#--Roberts-Novikovs--
#Studenta apliecības nr. rn25007

#Pabeigšanas datums 01.10.2025

# B25. Sastādīt programmu, kura saskaita un atņem racionālus skaitļus, racionālos skaitļus uzdodot kā divu veselu
# skaitļu pāri (1/3 tiek uzdota kā divi skaitļi 1 un 3). Rezultātam jābūt kā nesaīsināmam daļskaitlim. Uzrakstīt funkciju,
# kas saskaita 2 racionālus skaitļus un funkciju, kas pārveido racionālu skaitli par nesaīsināmu daļskaitli.

skaitlis1 = [] #Daļa, ar kurām tiks veiktas visas darbības
skaitlis2 = [] #Daļa, ar kurām tiks veiktas visas darbības
dalijumaSumma = []  #Šeit tiks saglabāta dalījuma summa
dalijumaStarpiba = [] #Šeit tiks saglabāta dalījuma starpība
dalamaisSummai = 0
dalamaisStarpibai = 0

def saisinats(x, y):
    dalijumaSumma = x
    dalijumaStarpiba = y 

    if dalijumaSumma[0] < dalijumaSumma[1]: #Noskaidro mazāko skaitli daļā & saglābā to atšķirīgā mainīgajā, lai tālāk noskaidrotu lielāko dalītāju
        dalSumLimits = dalijumaSumma[0]
    else: 
        dalSumLimits = dalijumaSumma[1]
#------------------------------------------------
    if dalijumaStarpiba[0] < dalijumaSumma[1]:  #Noskaidro mazāko skaitli daļā & saglābā to atšķirīgā mainīgajā, lai tālāk noskaidrotu lielāko dalītāju
        dalStarpLimits = dalijumaStarpiba[0]
    else: 
        dalStarpLimits = dalijumaStarpiba[1]
#------------------------------------------------
    if dalSumLimits < 0:                    #Ja summas limits ir negatīvs, to padara par pozitīvu skaitli |limits|
        dalSumLimits = dalSumLimits * -1
    if dalStarpLimits < 0:                  #Ja starpības limits ir negatīvs, to padara par pozitīvu skaitli |limits|
        dalStarpLimits = dalStarpLimits * -1
#------------------------------------------------
    print("dalSumLimits", dalSumLimits, "  dalStarpLimits", dalStarpLimits)

    for i in range(1, dalSumLimits+1):
        if(float(dalijumaSumma[0]) / i == float(dalijumaSumma[0]) // i and 
           float(dalijumaSumma[1]) / i == float(dalijumaSumma[1]) // i ):         #atrod lielāko kopīgo dalītāju summai
            dalamaisSummai = i
    for i in range(1, dalStarpLimits+1):
        if(float(dalijumaStarpiba[0]) / i == float(dalijumaStarpiba[0]) // i and 
           float(dalijumaStarpiba[1]) / i == float(dalijumaStarpiba[1]) // i ):         #atrod lielāko kopīgo dalītāju starpībai
            dalamaisStarpibai = i
        
    saisinataDalaSum = dalijumaSumma.copy()         #Pārkopē saīsināto daļu atsevišķā listā
    saisinataDalaStarp = dalijumaStarpiba.copy()    #Pārkopē saīsināto daļu atsevišķā listā

    saisinataDalaSum = [dalijumaSumma[0] / dalamaisSummai, dalijumaSumma[1] / dalamaisSummai]               #Izdala daļu ar kopīgo summas dalītāju
    saisinataDalaStarp = [dalijumaStarpiba[0] / dalamaisStarpibai, dalijumaStarpiba[1] / dalamaisStarpibai] #Izdala daļu ar kopīgo starpības dalītāju
    return(saisinataDalaSum, saisinataDalaStarp, dalamaisSummai, dalamaisStarpibai) #Atgriež abas saīsinātas daļas, kā arī abus dalītājus, lai tos paziņotu lietotājam

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

while True:
    while True:
        skaitlis1.append(int(input("Ievadiet 1. daļas skaitītāju: ")))
        skaitlis1.append(int(input("Ievadiet 1. daļas saucēju: ")))
        skaitlis2.append(int(input("Ievadiet 2. daļas skaitītāju: ")))
        skaitlis2.append(int(input("Ievadiet 2. daļas saucēju: ")))
        if(skaitlis1[0] == 0 or skaitlis1[1] == 0
            or skaitlis2[0] == 0 or skaitlis2[1] ==0):
            print("Tika ievadīta 0. Atkārtojiet skaitļu ievadi.")
            skaitlis1.clear()
            skaitlis2.clear()
            continue
        else:
            break


    vienadSk1 = skaitlis1.copy() #vienādots skaitlis 1
    vienadSk2 = skaitlis2.copy() #vienādots skaitlis 2

    print("Sākotnējās daļas: ", skaitlis1, skaitlis2)

    if skaitlis1[1] != skaitlis2[1]:  #ja ir atšķirīgi mainīgie, tad abas daļas reizina ar otras mainīgo, lai tos novienādotu
        vienadSk1[0] = skaitlis1[0] * skaitlis2[1]
        vienadSk1[1] = skaitlis1[1] * skaitlis2[1]
        vienadSk2[0] = skaitlis2[0] * skaitlis1[1]
        vienadSk2[1] = skaitlis2[1] * skaitlis1[1]

    dalijumaSumma = saskaitit(vienadSk1, vienadSk2) #Tiek izsaukta funkcija, kurā noskaidro daļu summu
    dalijumaStarpiba = atnemt(vienadSk1, vienadSk2) #Tiek izsaukta funkcija, kurā noskaidro daļu starpību

    print("Novienādotas daļas: ", vienadSk1, vienadSk2)
    print(vienadSk1, " + ", vienadSk2, " = ", dalijumaSumma)        #Printē darbības
    print(vienadSk1, " - ", vienadSk2, " = ", dalijumaStarpiba)

    saisinataDalaSum, saisinataDalaStarp, dalamaisSummai, dalamaisStarpibai = saisinats(dalijumaSumma, dalijumaStarpiba)    #Izsauc funkciju, kura saīsina abas daļas

    print("Kopīgais dalītājs summai = ", dalamaisSummai, " | Starpībai = ", dalamaisStarpibai)  #Paziņo lietotājam daļu kopīgos dalītājus  

    if dalijumaSumma[0] < 0 and dalijumaSumma[1] < 0:
        dalijumaSumma[0] *= -1 #Ja tiek dalīti 2 negatīvi skaitļi,...
        dalijumaSumma[1] *= -1 #...padara daļu pozitīvu
    if saisinataDalaStarp[0] < 0 and saisinataDalaStarp[1] < 0:
        saisinataDalaStarp[0] *= -1 #Ja tiek dalīti 2 negatīvi skaitļi,...
        saisinataDalaStarp[1] *= -1 #...padara daļu pozitīvu
    print("Saīsināta sumētā daļa = ", saisinataDalaSum)         #Izprintē rezultātus
    print("Saīsināta daļu starpība = ", saisinataDalaStarp)
    print("-----------------------------------------------")

    while True:
        usrRetry = input("Vai vēlaties izmantot programmu vēlreiz? Jā [1], Nē [0] ") #Tiek noskaidrots, vai lietotājs vēlas izmantot programmu atkārtoti
        try:
            usrRetryCheck = int(usrRetry)       #Tiek pārbaudīts, vai lietotājs ievadīja derīgu vērtību
            if usrRetryCheck == 1:
                skaitlis1.clear()
                skaitlis2.clear()
                dalijumaSumma.clear()
                dalijumaStarpiba.clear()
                break
            elif usrRetryCheck == 0:            #Ja nē, tad programma aizveras, ja jā tad tā atsākas, ja tiek ievadīta [..]
                exit()                          #[..] nederīga vērtība, tas tiek paziņots
            else:
                print("Ievadīta nederīga vērtība")
                continue
        except:
            print("Ievadīta nederīga vērtība")
            continue
        break
