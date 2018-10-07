#include<bits/stdc++.h>
#include<fstream>
#include<cstdio>
#include<string.h>
#include "show.h"

using namespace std;

class person
{
    int age;
    char gender,prof[50],locality[50];
    public:
        void setData()
        {
            cout << "\nEnter your age ";
            cin >> age;
            cout << "Enter your Gender(M,m/F,f) : ";
            cin>>gender;
	        cout<<"Enter your Profession : ";
	        cin>>prof;
            cout<<"Enter your locality : ";
            cin>>locality;
        }

        void showData()
        {
            cout << "\nAge : " << age;
            cout << "\nGender : " << gender;
	        cout << "\nProfession : " << prof;
            cout << "\nlocality : " << locality;
        }

        string local()
        {
            return locality;
        }
};

void display()
{
    getchar();
    system("clear");
    ifstream inFile;
    inFile.open("h.dat", ios::binary);

    person obj;
    cout<<"\n";

    while(inFile.read((char*)&obj, sizeof(obj)))
    {
        obj.showData();
        cout<<"\n";
    }

    inFile.close();
}
