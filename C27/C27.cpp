// Roberts Novikovs
//Studenta apliecības nr. rn25007

//Pabeigšanas datums 05.11.2025

/* C27. Doti skaitļi a(1), a(2),  , a(2n). Aprēķināt: 1) max (a(1)+a(2n), a(2)+a(2n-1),  , a(n)+a(n+1)) un 2) min (a(1)*a(n+1), a(2)*a(n+2),  , a(n)*a(2n)) */

#include <iostream>
using namespace std;

int maxv(int a[], int n){                       //max vērtības atrašana
    int maxVal;

    int *results = new int[n*2]; //šeit tiks saglabāti rezultāti

    for(int i = 0; i<n; i++){  //tiek uztaisīts lists ar visām vērtībām no 1 līdz n*2
        results[i] = a[i] + a[n*2-i-1];
        cout << "results[" << i << "] = " << a[i] << " + " << a[n*2-i-1] << " = " << results[i] << endl; //Paziņo programmas darbības un to rezultātus
    }

    maxVal = results[0];
    for(int i = 1; i<n; i++){
        if(results[i] > results[i-1]) maxVal = results[i];      //nosaka lielako rezultatu
    }

    cout << " Max value = " << maxVal << endl;   //rezultāti
    delete [] results;
    return(maxVal);
}

int minv(int a[], int n){                     //mazākās vērtības atrašana
    int minVal;

    int *results = new int[n*2];

    for(int i = 0; i<n; i++){  //tiek uztaisīts lists ar visām vērtībām no 1 līdz n*2
        results[i] = a[i] * a[n+i];
        cout << "results[" << i << "] = " << a[i] << " * " << a[n+i] << " = " << results[i] << endl; //Paziņo programmas darbības un to rezultātus
    }

    minVal = results[0];
    for(int i = 1; i<n; i++){
        if(results[i] < minVal){
            minVal = results[i];      //nosaka mazāko rezultātu
        } 
    }

    cout << " Min value = " << minVal << endl; //rezultāti
    delete [] results;
    return(minVal);
}

int main(){

    while(true){
        int usrValue;
        int usrNumInList;
        cout << "Ievadiet n vertibu: ";
        cin >> usrValue; //pieņemsim, ka ievada 3
        int n2 = usrValue*2-1; //n = 6
        int *a = new int[n2]; //dinamiskais masīvs ar 2n vietām
        a[0] = 0; //Pirmā [0] pozīcija listā tiek iestatīta kā 0, lai programmu varētu atkārtot bez kļūdām

        int atkartot = 0; //mainīgais programmas atkārtošanai

        for(int i = 0; i<=n2; i++){  //tiek uztaisīts lists ar visām vērtībām no 1 līdz n*2
            cout << "Ievadiet " << i+1 << ". skaitli: ";
            cin >> usrNumInList;
            a[i] = usrNumInList;
        //    cout << a[i] << endl; //-----------------testing only
        }

        cout << "Jusu skaitlu virkne: ";
        for(int i = 0; i<=n2; i++){
            cout << a[i] << ", ";
        }
        cout << endl;

        int maxVal = maxv(a, usrValue);
        int minVal = minv(a, usrValue);

        delete [] a;

        while(true){    //programmas atkārtošana
            cout << "Vai veelaties atkaartot programmu? [1] - jaa, [0] - nee: ";
            cin >> atkartot;

            if(atkartot == 1) break;
            else if(atkartot == 0) return 0;
            else continue;
            break;
        }  
    }
}
