# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

#Variables
def Update_data_info():
    able_days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']
    able_time = ['08:30 09:50', '10:10 11:30', '12:00 13:20', '13:40 15:00', '15:20 16:40', '17:00 18:20']
    table_date_counter = 0
    end_number = 0
    week_number = 0
    week_file = open('date.txt', 'w')
    week_file.write(datetime.today().strftime("%Y-%m-%d"))



    #Requests
    url =  'https://online.karazin.ua:1443/cgi-bin/timetable.cgi?n=700&group=7598'
    datas = {"faculty" : "1014",
             "teacher" : "",
             "course" : "1",
             "group" : "%C0%CC%CF-15",
            "sdate" : "01.09.2023",
             "edate" : "31.12.2023",
             "n" : "700"}

    response = requests.get(url, data = datas)
    response.encoding = "CP1251"




    #Functions
    def Week_file():
        nonlocal table_date_counter
        nonlocal week_number
        nonlocal week_file

        table_date = list(lesson_date[0].split('.'))
        table_date = datetime.strptime(f'{table_date[2]}-{table_date[1]}-{table_date[0]}', "%Y-%m-%d")
        if week_number != table_date.isocalendar()[1] and table_date_counter == 0:
            week_number = table_date.isocalendar()[1]
            week_file.close()
            week_file = open(str(week_number) + '.txt', 'w')

    def Get_date_table():
        nonlocal table_date_counter
        nonlocal week_file
        Week_file()

        week_file.write(lesson_date[0] + ' ' + lesson_date[1] + '\n')

        Days = Table.findAll('tr')

        for Day in Days:
            Hour = Day.findAll('td')
            lesson_numb = Hour[0].text
            lesson_time = list(str(Hour[1]).split('<br/>'))
            lesson_time = lesson_time[0][4:] + " " + lesson_time[1][:5]
            lesson_name = list(str(Hour[2]).split('<br/>'))

            if len(lesson_name) > 2:
                if lesson_name[-3][0] == '1':
                    lesson_name = 'пів' + lesson_name[-2]
                else:
                    lesson_name = lesson_name[-2]
            elif str(Hour[2].text) == ' ':
                lesson_name = ' Відпочинок'
            else:
                lesson_name = ' ' + str(Hour[2].text)

            week_file.write(lesson_numb + '//' + lesson_time + '//' + lesson_name + '\n')
        table_date_counter += 1
        week_file.write('NEXT_DAY\n')

    def Empty_date_table():
        nonlocal table_date_counter

        Week_file()

        table_date = list(lesson_date[0].split('.'))
        table_date = datetime.strptime(f'{table_date[2]}-{table_date[1]}-{table_date[0]}', "%Y-%m-%d")
        if able_days.index(table_day) < able_days.index(lesson_date[1]):
            table_date -= timedelta(days=able_days.index(lesson_date[1]) - able_days.index(table_day))
        elif end_number > 0:
            table_date += timedelta(days= end_number)
        else:
            table_date -= timedelta(days=7 - able_days.index(table_day))
        table_date = table_date.strftime("%d.%m.%Y")

        week_file.write(table_date + ' ' + table_day + '\n')
        for table_time in able_time:
            table_index = able_time.index(table_time) + 1
            week_file.write(str(table_index) + '//' + table_time + '//' + ' Відпочинок' + '\n')
        week_file.write('NEXT_DAY\n')
        if table_day == 'Неділя':
            table_date_counter = 0
            if lesson_date[1] == 'Понеділок':
                Get_date_table()
        else:
            table_date_counter += 1


    #Parsing
    soup = BeautifulSoup(response.text, 'lxml')
    Tables = soup.find('div', class_='container').find('div', class_='container').findAll('div', class_='col-md-6')
    for Table in Tables:
        lesson_date = list(Table.find('h4').text.split(' '))
        for table_day in able_days[table_date_counter:]:

            if lesson_date[1] == table_day:
                Get_date_table()
                break
            else:
                Empty_date_table()

    if table_date_counter != 0:
        for table_day in able_days[table_date_counter:]:
            end_number += 1
            Empty_date_table()
    week_file.close()



