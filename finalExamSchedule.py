import os.path
import requests
from bs4 import BeautifulSoup
from sys import argv

class Exam:
    def __init__(self,course,instructor,date,time,room):
        self.course=course
        self.course=course
        self.instructor=instructor
        self.date=date
        self.time=time
        self.room=room

def extract_schedule():
    # go to exam schedule page
    url = 'https://www.tru.ca/campus/current/exam-schedule/exam.html'
    response = requests.get(url)
    # create soup object of web page
    soup = BeautifulSoup(response.content, "html.parser")
    # find tables on page
    table_rows = soup.find_all('td')
    courselist = []
    courselist.insert(0,"Exams Winter 2018")
    for i in table_rows:
        # strip html tags from text
        courselist.append(str(i).replace('<td>', '').replace('</td>', '').replace('\t', " "))
    return courselist

#def toJson(Examlist,filename):

def save_to_txt(table,filename):
    out = open(filename, 'w')
    # for formatting of courses in text file
    for idx, lines in enumerate(table):
        out.write(str(lines))
        out.write('\n')
        # ignore 0 as it can be used as a term id
        # idx mod 5 is used to seperate each exam with a space
        if idx % 5 == 0 and idx is not 0:
            out.write("\n")


if __name__ == "__main__":
    courselist = extract_schedule()
    filename=argv[1]
    if filename is not None:
        save_to_txt(courselist,argv[1])
    else:
        print("Please add filename argument")