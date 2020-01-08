import os.path
import requests
import json
from bs4 import BeautifulSoup
from sys import argv


class Exam:
    def __init__(self, course, instructor, date, time, room):
        self.course = course
        self.course = course
        self.instructor = instructor
        self.date = date
        self.time = time
        self.room = room


def extract_schedule():
    # go to exam schedule page
    url = 'https://www.tru.ca/current/enrolment-services/exam-schedule/exam.html'
    response = requests.get(url)
    # create soup object of web page
    soup = BeautifulSoup(response.content, "html.parser")
    # find tables on page
    table = soup.find("table", attrs={'class':"small-12"})
    headings = [th.get_text() for th in table.find('thead').find_all("th")]

    data = []
    for row in table.find("tbody").find_all("tr"):
        dataset = dict(zip(headings,(td.get_text() for td in row.find_all("td"))))
        data.append(dataset)
    return data


def save_to_file(table, filename):
    out = open(filename, 'w')
    # for formatting of courses in text file
    j = json.dumps(table)
    print(j,file=out)


if __name__ == "__main__":
    courselist = extract_schedule()
    filename = argv[1]
    if filename is not None:
        save_to_file(courselist, filename)
    else:
        print("Please add filename argument")
