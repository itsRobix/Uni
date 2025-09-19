#include <iostream>
using namespace std;

int main(){

    int usrDaudzums;        //Šis noteiks, cik reizes lietotājs spēs ievadīt skaitļus
    int usrSkaitlis;        //Šis mainīgais uzņems lietotāja ierakstītā skaitļa vērtību
    int mazakaisSkaitlis;   //Tiks saglabāts zemākais skaitlis, lai to pēc tam var paziņot
    int mazakaSkDaudz = 1;      //Zemākā skaitļa daudzums
    int usrRepeat;          //Noskaidros, vai lietotājs vēlas atkārtot programmy


    while(true){
        cout << "Ievadiet, cik skaitlus veelaties ievadiit: ";
        cin >> usrDaudzums;

        if(usrDaudzums <=0){    //Pārbauda, vai ievadīts skaitlis, kas lielāks par 0
            cout << "Ievadiits nederiigs skaitlis." << endl;
            usrDaudzums = 0;
            continue;
        }
        else{                   //-MAIN PROGRAMMA
            cout << "\nIevadiet skaitli: ";
            cin >> usrSkaitlis;
            mazakaisSkaitlis = usrSkaitlis;   


            for (int i = 0; i < usrDaudzums-1; i++){
                cout << "Ievadiet skaitli: ";
                cin >> usrSkaitlis;

                if(usrSkaitlis < mazakaisSkaitlis){     //Ja ievadīts jauns mazākais skaitlis, tad tas tiek atzīmēts un tā daudzumu reseto uz 1 
                    mazakaisSkaitlis = usrSkaitlis;
                    mazakaSkDaudz = 1;
                }   
                else if(usrSkaitlis == mazakaisSkaitlis){
                    mazakaSkDaudz++;
                }
            }

            cout << "Zemaakais skaitlis ir " << mazakaisSkaitlis << ", tas tika ievadiits " << mazakaSkDaudz << " reizes.";

            while (true){                                                           //programmas atkārtošana
                cout << "\nVai veelaties atkaartot programmu? Jaa [1] | Nee [0]: "; 
                cin >> usrRepeat;

                if(usrRepeat == 1){     //pārbaude, vai ievadīts derīgs skaitlis
                    mazakaSkDaudz = 1;
                    break;
                }
                else if(usrRepeat == 0){
                    return 0;
                }
                else{
                    cout << "\nIevadiits nederiigs skaitlis.";
                    continue;
                }
            }
        }  
    }
}
