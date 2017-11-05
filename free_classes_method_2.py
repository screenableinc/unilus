import os;
# from bs4 import BeautifulSoup
import bs4
# open and read all html class files
path = "C:\\Users\Wise\Documents\\unilus\htmls\\undergrad\\fulltime\\"
class_time_tables = os.listdir(path);
for file in class_time_tables:
    class_time_table = path+file
    column_span = [0, 0, 0, 0, 0, 0, 0]

    with open(class_time_table, "r") as program:
        # soup = bs4.BeautifulSoup(program,"html.parser").prettify()
        soup = bs4.BeautifulSoup(program, "html.parser")
        title = str(soup.find("table").find("td").find("a").get("title")).split(":", -1)[0]

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
            column_idx = 0

            for j in range(iteration_count):

                if column_span[column_idx] > 0:
                    columns.insert(column_idx, bs4.BeautifulSoup("<td></td>", "html.parser"))

                rowspan = columns[j].get("rowspan")

                text = str(columns[j].get_text())
                day = days[column_idx]
                day_programs = programs_json["undergraduate"]["fulltime"][title][day]

                if text.__len__() > 50:
                    start = int(times[row_count].split(":")[0])
                    minute = times[row_count].split(":")[1]
                    if rowspan == None:
                        rowspan = "2"

                    ed_hr = start + int(rowspan)
                    time = str(start) + ":" + minute + "-" + str(ed_hr) + ":" + minute

                    link_text = columns[j].find("a")

                    if link_text == None:
                        break
                    else:
                        link_text = link_text.get_text()

                    # print("_______________________", file, day, time)

                    json_of_details = get_details.details(str(columns[j].get_text()).replace("\n", "").lower(),
                                                          link_text, g_soup)
                    json_of_details["time"] = time.replace("8:00-", "08:00-")

                    day_programs.append(json_of_details)
                    column_span[column_idx] = int(rowspan)

                column_idx = column_idx + 1

            for l in range(iteration_count):
                column_span[l] = column_span[l] - 1

                # print(column_span)
            row_count = row_count + 1


            # parse and get times at each slot
# pit against other algorithm