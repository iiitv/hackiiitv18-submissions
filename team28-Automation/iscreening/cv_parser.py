import re
import mechanize
from bs4 import BeautifulSoup
import csv

browser = mechanize.Browser(factory=mechanize.RobustFactory()) 
browser.set_handle_robots(False)
browser.open("http://recruitplushrxmlapidemo.onlineresumeparser.com/Default.aspx")
browser.select_form(nr=0)
browser.form.set_all_readonly(False)
filename = '/home/heet/My-Work/MyProjects/hackiiitv18-submissions/team28-Automation/iscreening/Sample resumes/CV4.pdf'
browser.form.add_file(open(filename), 'text/plain', filename)
response = browser.submit()
soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
extracted_cv = soup.find(id="txtResume")
text = extracted_cv.get_text().encode('utf-8')
ext_file = open("./cv_parsed.txt", "w")
ext_file.write(text)
ext_file.close()
