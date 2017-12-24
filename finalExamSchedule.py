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
    for i in table_rows:
        courselist.append(str(i).strip('<td>').strip('</td>'))
    save_to_txt(courselist)


def save_to_txt(tableout):
    linecount = 0
    output_file = "table.txt"
    out = open(output_file, 'w')
    for lines in tableout:
        out.write(str(lines))
        out.write('\n')
        linecount += 1
        if linecount == 5:
            out.write("\n")
            linecount = 0


if __name__ == "__main__":
    extract_schedule()