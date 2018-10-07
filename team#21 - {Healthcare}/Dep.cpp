#include <bits/stdc++.h>
#include <iostream>
#include <fstream> 
#include"Dep.h"

using namespace std;

void Dep()
{
system("clear");
ofstream fout;
fout.open( "goldep.txt", ios::out );

int a[18], i;
int sum = 0;
printf("\nThe following questions make up the standardised Goldberg\'s test.");
printf("\nThese are your options for each question: ");
printf("\n");
printf("\n\t\t1) Not at all."); //Standard replies, first option = 0, second =1, so on.
printf("\n\t\t2) Only slightly.");
printf("\n\t\t3) Partly.");
printf("\n\t\t4) A lot.");
printf("\n\t\t5) Quite a lot.");
printf("\n\t\t6) To a great extent.");
printf("\n");
printf("\nFor each of the following question, enter a number corresponding to the above list."); //The test questions start.
printf("\n1) I do everything slowly. ");
scanf("%d", &a[0]);
printf("\n2) My future seems hopeless. ");
scanf("%d", &a[1]);
printf("\n3) I find it hard to concenterate when I read. ");
scanf("%d", &a[2]);
printf("\n4) All joy and pleasure seem to have disappeared from my life. ");
scanf("%d", &a[3]);
printf("\n5) I find it hard to make decisions. ");
scanf("%d", &a[4]);
printf("\n6) I have lost interest in things that used to mean a lot to me. ");
scanf("%d", &a[5]);
printf("\n7) I feel sad, depressed and unhappy. ");
scanf("%d", &a[6]);
printf("\n8) I feel restless and cannot relax. ");
scanf("%d", &a[7]);
printf("\n9) I feel tired. ");
scanf("%d", &a[8]);
printf("\n10) I find it hard to do even trivial things. ");
scanf("%d", &a[9]);
printf("\n11) I feel guilty and deserve to be punished. ");
scanf("%d", &a[10]);
printf("\n12) I feel like a failure. ");
scanf("%d", &a[11]);
printf("\n13) I feel empty - more dead than alive. ");
scanf("%d", &a[12]);
printf("\n14) My sleep is disturbed: too little, too much, or disturbed sleep. ");
scanf("%d", &a[13]);
printf("\n15) I wonder how I would commit suicide. ");
scanf("%d", &a[14]);
printf("\n16) I feel confined and imprisoned. ");
scanf("%d", &a[15]);printf("\n17) I feel down even when something good happens to me. ");
scanf("%d", &a[16]);
printf("\n18) I have lost or gained weight without being on a diet. ");
scanf("%d", &a[17]);

for(i=0;i<18;i++) //Finding results.
{
    sum = sum + a[i] - 1; //Minus 1 because 'not at all' has value zero, so on.
}

/*
if(sum>=0 && sum<10) //The result categories.
{
    printf("\n\nDepression unlikely.");
}
else if(sum>=10 && sum<18)
{
    printf("\n\nPossible minor depression.");
}
else if(sum>=18 && sum<22)
{
    printf("\n\nOn the verge of depression.");
}
else if(sum>=22 && sum<36)
{
    printf("\n\nMinor to moderate depression.");
}
else if(sum>=36 && sum<54)
{
    printf("\n\nModerate to severe depression.");
}
else if(sum>=54)
{
    printf("\n\nSevere depression.");
}
*/

printf("\n");

fout<<sum;
fout<<"\n";

fout.seekp(ios::beg);
fout.close();


};