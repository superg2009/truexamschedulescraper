import os.path
import requests
import json
from bs4 import BeautifulSoup
from sys import argv


def extract_schedule():
    # go to exam schedule page
    url = 'https://www.tru.ca/current/enrolment-services/exam-schedule/exam.html'
    response = requests.get(url)
    # create soup object of web page
    soup = BeautifulSoup(response.content, "html.parser")
    # find tables on page
    # table = soup.find("table", attrs={'class':"small-12"})
    table = soup.select('div section div table')
    # print(table.prettify())
    data = []
    for sect in table:
        headings = [th.get_text() for th in sect.find('thead').find_all("th")]
        # create dict of headings (Key) and value
        for row in sect.find("tbody").find_all("tr"):
            dataset = dict(zip(headings, (td.get_text().strip('\t')
                                          for td in row.find_all("td"))))
            data.append(dataset)
    return data


def save_to_file(table, filename):
    out = open(filename+".json", 'w')
    # for formatting of courses in Json, fairly standard 4 indent
    json_file = json.dumps(table, indent=4)
    print(json_file, file=out)
    out.close()


if __name__ == "__main__":
    courselist = extract_schedule()  # get dict
    try:
        filename = argv[1]  # pull filename from CLI
        save_to_file(courselist, filename)  # publish dict as a json
    except Exception as e:
        print('likely you forgot the filename argument eg "winter2020" the extension .json is appended')
        print('stack trace: ')
        print(e)
        
