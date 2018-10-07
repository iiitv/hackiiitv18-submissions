#include <bits/stdc++.h>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include "Recomm.h"

using namespace std;

void Recomm()
{
    system("clear");
    ifstream fin;
    fin.open("goldep.txt",ios::in |ios::binary);
    int sum;
    fin.seekg (0, ios::beg);
    fin>>sum;

    if(sum>=0 && sum<10) 
    {
        cout<<"\nHallelujah! You are living the happiest life you can. There may be ups and downs which are considered normal behaviour. Keep yourself engaged in doing things you love and never let that smile of yours fade away. :-). ";
    }
    else if(sum>=10 && sum<18)
    {
        cout<<"\nYou are normally a cheerful person but may be susceptible to mild mood disturbances. These may be due to adolescence. Cultivating a hobby would do wonders in getting away from the negativities in life.";
    }
    else if(sum>=18 && sum<22)
    {
        cout<<"\nYou contemplate a lot. Which is good for a healthy mind but overthinking over an event may make you feel low at times. Live in the moment and don't delve deep on issues of the past";
        cout<<"\n\tHere's a list of music you might be interested to listen to when you feel like escaping from reality:";
        int choice;
        cout<<"\n\t\t1. Ain't No Mountain High - Marvin Gaye";
        cout<<"\n\t\t2. Hall Of Fame - The Script ft. will.i.am";
        cout<<"\n\t\t3. This Song Saved My Life - Simple Plan";
        cout<<"\n\t\t4. It’s My Life - Bon Jovi";
        cout<<"\n";
        cin>>choice;
        switch(choice)
        {
            case 1: {   
                        cout<<"\n\nPlaying Ain't No Mountain High - Marvin Gaye";
                        system("xdg-open https://www.youtube.com/watch?v=5tepYJno7rU ");
                        cout<<"\n";
                        break;
                    }
            case 2: {   
                        cout<<"\n\nPlaying Hall Of Fame - The Script ft. will.i.am";
                        system("xdg-open https://www.youtube.com/watch?v=dtgoDXEOxTM ");
                        cout<<"\n";
                        break;
                    }
            case 3: {   
                        cout<<"\n\nThis Song Saved My Life - Simple Plan";
                        system("xdg-open https://www.youtube.com/watch?v=VrTNXF741fE ");
                        cout<<"\n";
                        break;
                    }
            case 4: {   
                        cout<<"\n\nIt’s My Life - Bon Jovi";
                        system("xdg-open https://www.youtube.com/watch?v=vx2u5uUu3DE ");
                        cout<<"\n";
                        break;
                    }
            default: {
                        break;
                     }

        }
    }
    else if(sum>=22 && sum<36)
    {
        cout<<"\nYou feel more than just blue. You are on the starting stages of Depression and your symptoms can go on for days and are noticeable enough to interfere with your usual activities.";
        cout<<"\nMaintaining a healthy body and mind would help you relax in times of anxiety. Try to get enough delay and impart important nutrients in your diet.";
        cout<<"\nTrying out Yoga poses from this website can help.";
        getchar();
        cout<<"\n\nDissolve Depression (Press Enter)";
        getchar();
        system("xdg-open https://www.yogajournal.com/poses/yoga-for-depression ");
        cout<<"\n";
    }
    else if(sum>=36 && sum<54)
    {
        cout<<"\nYou are having problems with self-esteem that is resulting in low productivity, increased sensitiveness and excessive worrying. You are in the region of Severe Depression.";
        cout<<"\nYou should see a therapist as soon as possible. Spend more time with friends and family and hit the Gym regularly. Drink lots of water and meditate on a daily basis.";
        cout<<"\n\tMeanwhile, here's a list of music you might be interested to listen to when you feel like really low:";
        int choice;
        cout<<"\n\t\t1. Weightless - Marconi Union";
        cout<<"\n\t\t2. Electra - Airstream";
        cout<<"\n\t\t3. Mellomaniac (Chillout Mix) - DJ Shah";
        cout<<"\n\t\t4. Watermark - Enya";
        cout<<"\n";
        cin>>choice;
        switch(choice)
        {
            case 1: {   
                        cout<<"\n\nWeightless - Marconi Union";
                        system("xdg-open https://www.youtube.com/watch?v=UfcAVejslrU ");
                        cout<<"\n";
                        break;
                    }
            case 2: {   
                        cout<<"\n\nElectra - Airstream";
                        system("xdg-open https://www.youtube.com/watch?v=YbHZ8VVhb94 ");
                        cout<<"\n";
                        break;
                    }
            case 3: {   
                        cout<<"\n\nMellomaniac (Chillout Mix) - DJ Shah";
                        system("xdg-open https://www.youtube.com/watch?v=EcRXlM6edrM ");
                        cout<<"\n";
                        break;
                    }
            case 4: {   
                        cout<<"\n\nWatermark - Enya";
                        system("xdg-open https://www.youtube.com/watch?v=NO5tb20qQnA ");
                        cout<<"\n";
                        break;
                    }
            default: {
                        break;
                     }

        }
        cout<<"\n\nAlso,here's a link for some Doctors you would want to visit in Gandhinagar.";
        cout<<"\n\nPsychatrists in Gandhinagar (Press Enter)";
        getchar();
        system("xdg-open https://www.practo.com/gandhinagar/psychiatrist ");
        cout<<"\n";
    }
    else if(sum>=54)
    {
        cout<<"\nHelpline Number: 022 2754 6669";
        cout<<"\nYou may have experienced delusions, feelings of stupor, halucinations or suicidal thoughts before.";
        cout<<"\nYou are in dire need of Medical Thrapy as soon as possible. Spend more time with friends and family and do lots of physical activity.";
        getchar();
        cout<<"\n\nHere's a link for online an online chat room and councelling.(Press Enter)";
        getchar();
        system("xdg-open https://www.7cups.com/ ");
        cout<<"\n";
        cout<<"\n\nHere's a link for some Doctors you would want to visit in Gandhinagar.";
        cout<<"\n\nPsychatrists in Gandhinagar(Press Enter)";
        getchar();
        system("xdg-open https://www.practo.com/gandhinagar/psychiatrist ");
        cout<<"\n";
    }    

    fin.close();

};