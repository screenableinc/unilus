import os
import bs4
import urllib.request as request
path = "C:\\Users\Wise\Documents\\unilus\schools\\"
schools_path =path+ "schools.html"
program_path = path+"program_ex.html"

keys = []
courses={}
def remove_spaces(string):

    while str(string).startswith(" "):
        string=string[1:]

    while str(string).endswith(" "):
        string = string[:-1]

    return string




# with open(program_path,"r",encoding="utf-8") as file:

#                 print(course_name,code)

def traverse_program(link):
    soup = bs4.BeautifulSoup(request.urlopen(link).read(), "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        if str(table).lower().__contains__("first semester"):
            for li in table.find_all("li"):
                text = str(li.get_text())
                code = text.split(" ",-1)[0]
                course_name ="         "+ text.replace(code,"")
                course_name = remove_spaces(course_name)
                code=remove_spaces(code)

                if not keys.__contains__(code):
                    keys.append(code)
                courses[code]=course_name


def traverse_school(link):
    soup =bs4.BeautifulSoup(request.urlopen(link).read(),"html.parser")
    a_tags = soup.find_all("a")
    for tag in a_tags:
        if str(tag).lower().__contains__("bachelor of"):
            href = tag.get("href")
            traverse_program("http://www.unilus.ac.zm/"+href)


def begin():
    with open(schools_path,"r") as file:
        file = bs4.BeautifulSoup(file,"html.parser")
        anchors = file.find_all("a")
        for anchor in anchors:
            if str(anchor).lower().__contains__("school of"):
                link = anchor.get("href")
                traverse_school(link)

    return {"courses":courses,"keys":keys}



