#AUTOMATED CLASSROOM ATTENDANCE

IDEA: This project automates attendance of students automatically based on facial recognition
	
##Theme : Automation
##Product Name: 
 
##Hardware Requirements

- Webcam
- Raspberripi
- Wifi conectivity

##How it works

- Each door in the classroom has an attached camera which registers faces everytime someone enters and exits.

<p align="center">
 <img ss="./front.jpeg" alt="FrontFace" style="width: 400px;"/></div>
</p>

- Upon facial recognition, a timestamp is stored along with every successful facial recognition be it entering the room or leaving.
- Based on the timestamps registered at entry and exit point(s), the total amount of time spent inside the classroom is calculated.
- Students spending more than 60% of the time in the classroom are marked present.
- Students having only one timestamp i.e only at the time of entry or exit would be marked absent unless explicitly verified by humans.
- Extreme case of recognising twins can be tackled by imlementing two step verifcation process like verification by roll numbers or biometrics.

##Technicalities

- The image is captured using camera with raspberrypi 1b+.
- Implementation of OpenCV for facial recogniton algorithm.
- Timestamps are stored in a file using ID as primary key and time spent inside the classroom is calculated as per the timestamps using python programing language.