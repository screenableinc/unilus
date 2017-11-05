import bs4
import os
import urllib.request as request
import urllib
import json
import get_details
import repair_html
import get_list_of_all_programs
# create needed directories
# if not os.path.exists(dir())

project_path = os.getcwd()+"\\"
htmls = project_path+"htmls\\"
undergrad_fulltime_program_sched_htmls = htmls+"undergrad\\fulltime\\"
undergrad_parttime_program_sched_htmls = htmls+"undergrad\\parttime\\"
undergrad_parttime_rm_htmls = htmls+"undergrad_pt_rm\\"
undergrad_fulltime_rm_htmls = htmls+"undergrad_ft_rm\\"
postgrad_program_sched_htmls = htmls+"postgrad\\"
postgrad_rm_htmls = htmls+"postgrad_rm\\"

folders_to_create = [undergrad_fulltime_program_sched_htmls,undergrad_parttime_program_sched_htmls,postgrad_rm_htmls,undergrad_fulltime_rm_htmls,undergrad_parttime_rm_htmls]
main_json = {"free_classes":{},"programs":{}}
for i in folders_to_create:
    if not os.path.exists(i):
        os.makedirs(i)

# my_soup = bs4.BeautifulSoup(urllib.request.urlopen("http://google.com").read(), "html.parser")

# list of lecturers
import urllib.request


# urllib.request.urlretrieve("http://www.unilus.ac.zm/UndergradFullTimeTable/x3001bba121382.htm","C:\\Users\AC\Documents\CPY_SAVES\\moron.html")
# print("done")
all_programs = get_list_of_all_programs.begin()
keys = all_programs["keys"]
all_courses=all_programs["courses"]
rooms={"Sunday":{},"Monday":{},"Tuesday":{},"Wednesday":{},"Thursday":{},"Friday":{},"Saturday":{}}
with open(project_path+"undergrad_all.html", "r") as html:
    g_soup = bs4.BeautifulSoup(html,"html.parser")
    g_soup=g_soup.find_all("a")

def download_markup(link, program, category):
    if not str(link).__contains__("www."):
        link = str(link).replace("://","://www.")
    import repair_html
    if category =="ug_ft_pg":
        urllib.request.urlretrieve(link, undergrad_fulltime_program_sched_htmls+program+".html")
        repair_html.repair(undergrad_fulltime_program_sched_htmls+program+".html")

    elif category =="ug_pt_pg":
        urllib.request.urlretrieve(link,undergrad_parttime_program_sched_htmls + program + ".html")
        repair_html.repair(undergrad_parttime_program_sched_htmls + program + ".html")
    elif category=="pg_pg":

        program=program.split(":",-1)[1]
        urllib.request.urlretrieve(link, postgrad_program_sched_htmls + program + ".html")
        repair_html.repair(postgrad_program_sched_htmls + program + ".html")

def download_rooms_markup(link, room, category):
    if not str(link).__contains__("www."):
        link = str(link).replace("://","://www.")
    if category == "ug_ft_rm":
        # with open(, "w")as file:
        urllib.request.urlretrieve(link,undergrad_fulltime_rm_htmls + room + ".html")
        repair_html.repair(undergrad_fulltime_rm_htmls + room + ".html")

    elif category == "ug_pt_rm":

        urllib.request.urlretrieve(link, undergrad_parttime_rm_htmls + room + ".html")
        repair_html.repair(undergrad_parttime_rm_htmls + room + ".html")
    elif category == "pg_rm":
        with open(postgrad_rm_htmls+room+".html","w")as file:
            urllib.request.urlretrieve(link, postgrad_rm_htmls + room + ".html")
            repair_html.repair(postgrad_rm_htmls + room + ".html")


# prog time tables
# undergrad fulltime

def get_program_tables():

    with open(project_path+"undergrad_all.html","r")as html:
        soup = bs4.BeautifulSoup(html,"html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()


            if str(title).__contains__("Semester") or str(title).__contains__("ACCA"):
                if  str(title).__contains__("/"):
                    title = str(title).replace("/","-")
                print(i.get("href"))
                download_markup(i.get("href"),title,"ug_ft_pg")
    # undergrad partime
    with open(project_path + "undergrad_all_part_time.html", "r")as html:
        soup = bs4.BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()

            if str(title).__contains__("Semester") or str(title).__contains__("ACCA"):
                if  str(title).__contains__("/"):
                    title = str(title).replace("/","-")
                download_markup(i.get("href"),title ,"ug_pt_pg")
            # post_grad
    with open(project_path + "postgrad_programs.html", "r")as html:
        soup = bs4.BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()

            if str(title).__contains__("PG") or str(title).__contains__("Stage"):
                if  str(title).__contains__("/"):
                    title = str(title).replace("/","-")
                download_markup(i.get("href"), title ,"pg_pg")


def get_rooms():
    # postgrad_rooms
    with open(project_path+"postgrad_rooms.html","r")as html:
        soup = bs4.BeautifulSoup(html,"html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()

            if str(title).__contains__("Pioneer") or str(title).__contains__("pioneer"):
                title = i.get_text()
                download_rooms_markup(i.get("href"), title, "pg_rm")

    # undergrad_full_time_rooms
    with open(project_path+"undergrad_all.html","r")as html:
        soup = bs4.BeautifulSoup(html,"html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()

            if str(title).lower().__contains__("lecture"):
                title = i.get_text()
                download_rooms_markup(i.get("href"), title, "ug_ft_rm")
    # under_grad_part_time rooms
    with open(project_path+"undergrad_all_part_time.html","r")as html:
        soup = bs4.BeautifulSoup(html,"html.parser")
        links = soup.find_all("a")
        for i in links:
            title = i.get_text()
            title = str(title).replace("/","-")


            if str(title).lower().__contains__("lecture"):
                print(title,";")
                download_rooms_markup(i.get("href"), str(title), "ug_pt_rm")

times = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:30"
         ,"18:30","19:30","20:30"]
# create this on the fly in update
programs_json = {"undergraduate":{"fulltime":{},"parttime":{}},"postgraduate":{}}

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# undergrad programs

def get_undergrad_programs_ft():
    for file in os.listdir(undergrad_fulltime_program_sched_htmls):
        column_span = [0,0,0,0,0,0,0]


        with open(undergrad_fulltime_program_sched_htmls+file,"r") as program:
            # soup = bs4.BeautifulSoup(program,"html.parser").prettify()
            soup = bs4.BeautifulSoup(program,"html.parser")
            title = str(soup.find("table").find("td").find("a").get("title")).split(":",-1)[0]
            programs_json["undergraduate"]["fulltime"][title] = {"Sunday":[],"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[]}
            # get all table rows
            table = soup.find_all("table")[0]
            rows = table.find_all("tr")
            # remove the first one whic contians the course name
            rows.remove(rows[0])
            # remove time slot rows
            rows.remove(rows[0])
            row_count = 0
            iteration_count = 7
            # the first tabel tag


            for i in rows:


                columns = i.find_all("td")


                # remove the first column...ths has time slot
                columns.remove(columns[0])
                column_idx=0


                for j in range(iteration_count):







                    if column_span[column_idx]>0:

                        columns.insert(column_idx,bs4.BeautifulSoup("<td></td>","html.parser"))


                    rowspan =columns[j].get("rowspan")



                    text=str(columns[j].get_text())
                    day = days[column_idx]
                    day_programs = programs_json["undergraduate"]["fulltime"][title][day]

                    if text.__len__()>50:
                        start = int(times[row_count].split(":")[0])
                        minute = times[row_count].split(":")[1]
                        if rowspan==None:
                            rowspan="2"

                        ed_hr = start+int(rowspan)
                        time = str(start)+":"+minute+"-"+str(ed_hr)+":"+minute
                        link_text = columns[j].find("a")

                        if link_text==None:
                            break
                        else:
                            link_text=link_text.get_text()
                        json_of_details = get_details.details(str(columns[j].get_text()).replace("\n","").lower(),link_text,g_soup,keys,all_courses)

                        json_of_details["time"]=time.replace("8:00-","08:00-")
                        room = json_of_details["room"]
                        # get start and end time
                        split_time = str(json_of_details["time"]).split(":",-1)
                        start_time = split_time[0]
                        end_time = split_time[1].split("-",-1)[1]
                        for t in range (int(end_time)-int(start_time)):
                            curr_time = int(start_time)+t
                            min2appen = ":00"
                            if curr_time>=17:
                                min2appen=":30"
                            if curr_time<10:
                                curr_time="0"+str(curr_time)

                            curr_time = str(curr_time)+min2appen

                            if rooms[day][curr_time].__contains__(room):
                                # rooms[day][curr_time].remove(room)
                                print("removed", room,day,time)
                        print(int(start_time)-int(end_time))
                        day_programs.append(json_of_details)
                        column_span[column_idx]=int(rowspan)
                    column_idx = column_idx + 1
                for l in range(iteration_count):
                    column_span[l]=column_span[l]-1

                    # print(column_span)
                row_count = row_count+1







def get_postgrad_programs():
    for file in os.listdir(postgrad_program_sched_htmls):
        column_span = [0,0,0,0,0,0,0]

        with open(postgrad_program_sched_htmls+file,"r") as program:
            soup = bs4.BeautifulSoup(program,"html.parser")
            title = str(soup.find("table").find("td").find("a").get("title")).split(":",-1)[0]
            programs_json["postgraduate"][title] = {"Sunday":[],"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[]}
            # get all table rows
            table = soup.find_all("table")[0]
            rows = table.find_all("tr")
            # remove the first one whic contians the course name
            rows.remove(rows[0])
            # remove time slot rows
            rows.remove(rows[0])
            row_count = 0
            iteration_count = 7
            # the first tabel tag

            for i in rows:

                columns = i.find_all("td")


                # save time slot.....ostgrad doest use row span like full time
                # remove the first column...ths has time slot
                tim_column = columns[0]
                columns.remove(columns[0])
                column_idx=0
                for j in range(7):


                    if column_span[column_idx]>0:

                        columns.insert(column_idx,bs4.BeautifulSoup("<td></td>","html.parser"))




                    text = columns[j].get_text()

                    day = days[column_idx]
                    day_programs = programs_json["postgraduate"][title][day]
                    if str(text).__len__()>50:


                        time = str(tim_column.get_text()).replace("\n","").replace(" ","")
                        link_text = columns[j].find("a")

                        json_of_details = get_details.details(str(columns[j].get_text()).replace("\n", "").lower(),
                                                              link_text, g_soup,keys,all_courses)

                        json_of_details["time"] = str(time).replace("\xa0","").replace("8:00-","08:00-")


                        day_programs.append(json_of_details)

                    column_idx = column_idx + 1



                    # print(column_span)
                row_count = row_count+1

def get_undergrad_programs_pt():
    for file in os.listdir(undergrad_parttime_program_sched_htmls):
        column_span = [0, 0, 0, 0, 0, 0, 0]

        with open(undergrad_parttime_program_sched_htmls + file, "r") as program:
            soup = bs4.BeautifulSoup(program, "html.parser")
            title = str(soup.find("table").find("td").find("a").get("title")).split(':',-1)[0]
            programs_json["undergraduate"]["parttime"][title] = {"Sunday":[],"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[]}
            # get all table rows
            table = soup.find_all("table")[0]
            rows = table.find_all("tr")
            # remove the first one whic contians the course name
            rows.remove(rows[0])
            # remove time slot rows
            rows.remove(rows[0])
            row_count = 0
            iteration_count = 7
            # the first tabel tag

            for i in rows:

                columns = i.find_all("td")

                # save time slot.....ostgrad doest use row span like full time
                # remove the first column...ths has time slot
                tim_column = columns[0]
                columns.remove(columns[0])
                column_idx = 0
                for j in range(7):

                    if column_span[column_idx] > 0:
                        columns.insert(column_idx, bs4.BeautifulSoup("<td></td>", "html.parser"))

                    text = columns[j].get_text()
                    day = days[column_idx]
                    day_programs = programs_json["undergraduate"]["parttime"][title][day]
                    if str(text).__len__() > 50:

                        time = str(tim_column.get_text()).replace("\n", "").replace(" ", "")
                        link_text = columns[j].find("a")

                        json_of_details = get_details.details(
                            str(columns[j].get_text()).replace("\n", "").lower(),
                            link_text, g_soup,keys,all_courses)
                        json_of_details["time"] = str(time).replace("\xa0","").replace("8:00-","08:00-")



                        day_programs.append(json_of_details)

                    column_idx = column_idx + 1



                        # print(column_span)
                    row_count = row_count + 1
# __________________________________________rooms________________________________________

# create keys
for i in days:
    for j in times:
        rooms[i][j]=[]
def get_fulltime_rooms():
    for file in os.listdir(undergrad_fulltime_rm_htmls):
        column_span = [0,0,0,0,0,0,0]

        with open(undergrad_fulltime_rm_htmls+file,"r") as program:
            soup = bs4.BeautifulSoup(program,"html.parser")
            title = str(soup.find("table").find("td").find("a").get("title")).split(":",-1)[0].split("RM",-1)[1].split("#",-1)[0]



            # get all table rows
            table = soup.find_all("table")[0]
            rows = table.find_all("tr")
            # remove the first one whic contians the course name
            rows.remove(rows[0])
            # remove time slot rows
            rows.remove(rows[0])
            row_count = 0
            iteration_count = 7
            # the first tabel tag

            for i in rows:

                columns = i.find_all("td")


                # save time slot.....ostgrad doest use row span like full time
                # remove the first column...ths has time slot
                tim_column = columns[0]
                columns.remove(columns[0])
                column_idx=0
                for j in range(7):


                    if column_span[column_idx]>0:

                        columns.insert(column_idx,bs4.BeautifulSoup("<td></td>","html.parser"))


                    if not str(columns[j])=="<td></td>":


                        text = columns[j].get_text()
                        rowspan = columns[j].get("rowspan")
                        day = days[column_idx]

                        if str(text).__len__()>50 or str(text).lower().__contains__("reserved"):


                            time = str(tim_column.get_text()).replace("\n","").replace(" ","")
                            link_text = columns[j].find("a")

                            if rowspan==None:
                                rowspan=1


                            column_span[column_idx] = int(rowspan)

                        elif str(text).__len__()<50:

                            rooms[days[column_idx]][times[row_count]].append(title)
                            print(title,days[column_idx],times[row_count])

                    column_idx = column_idx + 1



                    # print(column_span)
                for j in range(column_span.__len__()):
                    column_span[j]=column_span[j]-1
                row_count = row_count+1

def get_fulltime_rooms():
    for file in os.listdir(undergrad_fulltime_rm_htmls):
        column_span = [0,0,0,0,0,0,0]

        with open(undergrad_fulltime_rm_htmls+file,"r") as program:
            soup = bs4.BeautifulSoup(program,"html.parser")
            title = str(soup.find("table").find("td").find("a").get("title")).split(":",-1)[0].split("RM",-1)[1].split("#",-1)[0]



            # get all table rows
            table = soup.find_all("table")[0]
            rows = table.find_all("tr")
            # remove the first one whic contians the course name
            rows.remove(rows[0])
            # remove time slot rows
            rows.remove(rows[0])
            row_count = 0
            iteration_count = 7
            # the first tabel tag

            for i in rows:

                columns = i.find_all("td")


                # save time slot.....ostgrad doest use row span like full time
                # remove the first column...ths has time slot
                tim_column = columns[0]
                columns.remove(columns[0])
                column_idx=0
                for j in range(7):


                    if column_span[column_idx]>0:

                        columns.insert(column_idx,bs4.BeautifulSoup("<td></td>","html.parser"))


                    if not str(columns[j])=="<td></td>":


                        text = columns[j].get_text()
                        rowspan = columns[j].get("rowspan")
                        day = days[column_idx]

                        if str(text).__len__()>50 or str(text).lower().__contains__("reserved"):


                            time = str(tim_column.get_text()).replace("\n","").replace(" ","")
                            link_text = columns[j].find("a")

                            if rowspan==None:
                                rowspan=1


                            column_span[column_idx] = int(rowspan)

                        elif str(text).__len__()<50:

                            rooms[days[column_idx]][times[row_count]].append(title)
                            print(title,days[column_idx],times[row_count])

                    column_idx = column_idx + 1



                    # print(column_span)
                for j in range(column_span.__len__()):
                    column_span[j]=column_span[j]-1
                row_count = row_count+1


def start_getting_programs():
    get_fulltime_rooms()
    get_undergrad_programs_ft()
    get_undergrad_programs_pt()
    # get_postgrad_programs()

    with open(project_path+"programs_scheds.json","w")as file:
        json.dump(programs_json,file)
    with open(project_path+"free_classes.json","w")as file:
        json.dump(rooms,file)

start_getting_programs()
# get_program_tables()
# get course code
# for i in os.listdir(undergrad_fulltime_program_sched_htmls):
#     with open(undergrad_fulltime_program_sched_htmls+i,"r") as k:
#         soup = bs4.BeautifulSoup(k.read(),"html.parser")
#         title = soup.find("table").find("td").find("a").get("title")
#         print(title)


