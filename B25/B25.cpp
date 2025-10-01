//--Roberts-Novikovs--
//Studenta apliecības nr. rn25007

/* B25. Sastādīt programmu, kura saskaita un atņem racionālus skaitļus, racionālos skaitļus uzdodot kā divu veselu
   skaitļu pāri (1/3 tiek uzdota kā divi skaitļi 1 un 3). Rezultātam jābūt kā nesaīsināmam daļskaitlim. Uzrakstīt funkciju,
   kas saskaita 2 racionālus skaitļus un funkciju, kas pārveido racionālu skaitli par nesaīsināmu daļskaitli. */


#include <iostream>
using namespace std;

int skaitlis1[2];
int skaitlis2[2];
int saisinatasDalasKopa[4]; //Šeit saglabās saīsinātas daļas, lai pēc tam tās sadalītu savos mainīgajos

int daluSumma[2];
int daluStarp[2];

int atkartot = 0;

void novienadot(int &sk1, int &sa1, int &sk2, int &sa2){
   int x = sa1;   //saglabā 1.saucēja vērtību
   int y = sa2;   //saglabā 2.saucēja vērtību
   if(sa1 != sa2){  //ja ir atšķirīgi mainīgie, tad abas daļas reizina ar otras mainīgo, lai tos novienādotu
        sk1 *= y;
        sa1 *= y;
        sk2 *= x;
        sa2 *= x;
   }
}

int saskaitit(int &sk1, int &sk2){
   int daluSum = sk1+sk2;

   return(daluSum);
}

int atnemt(int &sk1, int &sk2){
   int daluStarp = sk1-sk2;

   return(daluStarp);
}

void saisinat(int &sumSk, int &sumSa, int &starpSk, int &starpSa){
   int dalSumLimits = 0;      //tiks saglabāts mazākais skaitlis daļā...
   int dalStarpLimits = 0;    //...to izmantos, lai atrasu lielāko kopīgo dalītāju

   int dalamaisSummai = 1;    //tiks glabāts lielākais dalāmais daļu summai
   int dalamaisStarpibai = 1; //tiks glabāts lielākais dalāmais daļu starpībai

   if(sumSk < sumSa) dalSumLimits = sumSk;   //tiek noskaidrots mazākais skaitlis daļā
   else dalSumLimits = sumSa;

   if(starpSk < starpSa) dalStarpLimits = starpSk; //tiek noskaidrots mazākais skaitlis daļā
   else dalStarpLimits = starpSa;

   if(dalSumLimits < 0) dalSumLimits *= -1;     //ja limits ir negatīvs, to...
   if (dalStarpLimits <0) dalStarpLimits *= -1; //...pārtaisa pozitīvu

   for(int i=1; i <= dalSumLimits; i++){
      if((int)sumSk % i == 0 && (int)sumSa % i == 0){
         dalamaisSummai = i;
      }
   }
   for(int i=1; i <= dalStarpLimits; i++){
      if((int)starpSk % i == 0 && (int)starpSa % i == 0){
         dalamaisStarpibai= i;
      }
   }

   cout << "lielaakais kopeejais daliitaajs summas dalai = " << dalamaisSummai << " | starpibas dalai = " << dalamaisStarpibai << endl;
   sumSk /= dalamaisSummai;      //izdalam daļas ar kopīgajiem dalītājiem
   sumSa /= dalamaisSummai;
   starpSk /= dalamaisStarpibai;
   starpSa /= dalamaisStarpibai;

}

int main(){

   while(true){
      do{
      cout << "Ievadiet 1. dalas skaitiitaaju: "; cin >> skaitlis1[0];  //iegūst lietotāja
      cout << "Ievadiet 1. dalas daliitaaju: "; cin >> skaitlis1[1];    //daļas
      cout << "Ievadiet 2. dalas skaitiitaaju: "; cin >> skaitlis2[0];
      cout << "Ievadiet 2. dalas daliitaaju: "; cin >> skaitlis2[1];
      if(skaitlis1[0] == 0 || skaitlis1[1] == 0
      || skaitlis2[0] == 0 || skaitlis2[1] == 0) cout << "Ievadiita 0. Atkaartojiet skaitlu ievadi" << endl;
      }while(skaitlis1[0] == 0 || skaitlis1[1] == 0 
         || skaitlis2[0] == 0 || skaitlis2[1] == 0); //pārliecinas, ka ievadītais skaitlis nav 0

      novienadot(skaitlis1[0], skaitlis1[1], skaitlis2[0], skaitlis2[1]);
      cout << skaitlis1[0] << "/" << skaitlis1[1] << endl << skaitlis2[0] << "/" << skaitlis2[1] << endl;

      daluSumma[0] = saskaitit(skaitlis1[0], skaitlis2[0]);
      daluSumma[1] = skaitlis1[1];

      daluStarp[0] = atnemt(skaitlis1[0], skaitlis2[0]);
      daluStarp[1] = skaitlis1[1];

      cout << "Summa = " << daluSumma[0] << "/" << daluSumma[1] << endl;
      cout << "Starpiiba = " << daluStarp[0] << "/" << daluStarp[1] << endl;

      saisinat(daluSumma[0], daluSumma[1], daluStarp[0], daluStarp[1]);
      cout << daluSumma[0] << "/" << daluSumma[1] << endl;
      cout << daluStarp[0] << "/" << daluStarp[1] << endl;

      cout << "Vai veelaties atkaartot programmu? [1] - jaa, [0] - nee: ";
      cin >> atkartot;

      while(true){
         if(atkartot == 1) break;
         else if(atkartot == 0) return 0;
         else continue;
      }
      continue;
   }
}
