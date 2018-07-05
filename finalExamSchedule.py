import os.path
import sqlite3
import requests
from bs4 import BeautifulSoup


def create_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS exams(id INTEGER PRIMARY KEY ,course TEXT,
             instructor TEXT, datetime TEXT,location TEXT)
 ''')
    conn.commit()
    conn.close()


def add_exam_entry(course, instructor, time, location):
    db = sqlite3.connect("test.db")
    curs = db.cursor()
    # insert data into exams table
    curs.execute('''  INSERT INTO exams(course ,instructor, datetime ,location ) VALUES (?,?,?,?)'''
                 , (course, instructor, time, location))
    db.commit()
    db.close()


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
    save_to_txt(courselist)



def save_to_txt(table):
    output_file = "table1.txt"
    out = open(output_file, 'w')
    # for formatting of courses in text file
    for idx, lines in enumerate(table):
        out.write(str(lines))
        out.write('\n')
        # ignore 0 as it can be used as a term id
        if idx % 5 == 0 and idx is not 0:
            out.write("\n")


if __name__ == "__main__":
    # prevent having to scrape if done one already
    if not os.path.isfile("table.txt"):
        extract_schedule()
    if not os.path.isfile("test.db"):
        create_db()
