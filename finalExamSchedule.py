from bs4 import BeautifulSoup
import requests


def extract_schedule():
    # go to exam schedule page
    url = 'https://www.tru.ca/campus/current/exam-schedule/exam.html'
    response = requests.get(url)
    # create soup object of web page
    soup = BeautifulSoup(response.content, "html.parser")
    table_rows = soup.find_all('td')
    courselist = []
    # strip html tags from text
    for i in table_rows:
        courselist.append(str(i).replace('<td>', '').replace('</td>', ''))
    save_to_txt(courselist)


def save_to_txt(table):
    linecount = 0
    output_file = "table.txt"
    out = open(output_file, 'w')
    # for formatting of courses in text file
    for lines in table:
        out.write(str(lines))
        out.write('\n')
        linecount += 1
        # determined every 5th line is the end of a course
        if linecount == 5:
            out.write("\n")
            linecount = 0


if __name__ == "__main__":
    extract_schedule()
