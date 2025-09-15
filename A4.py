usrNum = 0          #Šeit tiks ievadīti skaitļi pārbaudei, pirms tie tiek pievienoti sarakstam
usrNumList = []     #Šeit tiks glabāti visi lietotāja ievadītie skaitļi
lowNumAmount = 0

while True:

    usrAmount = input("Izvēlaties, cik skaitļus ievadīsiet: ")

    try:
       usrAmount = int(usrAmount)               #Tiek pārbaudīts, vai ievadītais ir skaitlis
    except:
        print("Ievadīts nederīgs daudzums")
        continue

    if usrAmount <= 0:                          #Tiek pārbaudīts, vai ievadītais ir pozitīvs skaitlis
        print("Ievadīts nederīgs skaitlis")
        continue
    else:
        #for x in range(usrAmount):
        while usrAmount > 0:                      
            usrNum = input("Ievadiet skaitli: ")
            try:
                usrNum= int(usrNum)               #Tiek pārbaudīts, vai ievadītais ir skaitlis
                usrNumList.append(usrNum)
                usrAmount = usrAmount-1
            except:
                print("Ievadīts nederīgs daudzums")

    usrNumList.sort()                                   #Tiek sakārtots saraksts, noskaidrots mazākais skaitlis un informācija tiek atgriezta lietotājam
    lowNumAmount = usrNumList.count(usrNumList[0])
    print("Mazākais ievadītais skaitlis ir ", usrNumList[0], " un tas tika ievadīts ", lowNumAmount, " reizi(-es).")

    while True:                                                                 #Tiek noskaidrots, vai lietotājs vēlas izmantot programmu atkārtoti
        usrRetry = input("Vai vēlaties atkārtot programmu? Jā [1], Nē [0]: ") 
        
        try:
            usrRetry = int(usrRetry)
        except:
            print("Ievadīts nederīgs skaitlis")
            continue

        if usrRetry == 0:
            exit()
        elif usrRetry == 1:
            break
        else:
            print("Ievadīts nederīgs skaitlis")
            continue
        break
        


