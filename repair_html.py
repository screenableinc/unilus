
def repair(file):


    with open(file,"r")as file2rep:
        file2rep = file2rep.read()
        ml = file2rep.split("<td",-1)
        saveforlater = ml[0]
        ml.remove(ml[0])
        html = saveforlater
        for i in ml:
            # print("___________________",i.__len__())
            if not i.lower().__contains__("semester") or not i.lower().__contains__("mimosa"):
                if i.__len__()>200 or i.__contains__(":00") or i.__contains__(":30"):
                    if not i.__contains__("</td>") and not i.__contains__("<tr"):
                        i = i+"</td>"
            i="<td"+i

            html = html+i
        with open(file, "w")as wr:
            wr.write(html)



# repair("C:\\Users\AC\Documents\PycharmProjects\\unilus\htmls\\undergrad\\fulltime\Bachelor of Arts Economics 1st Yr 2nd Semester.html")
