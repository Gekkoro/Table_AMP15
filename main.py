# -*- coding: cp1251 -*-
from datetime import datetime
from Update import Update_data_info

from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'resizable', False)
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

week_lesson_matrix = [[], [], [], [], [], [], []]
week_button_matrix = [[], [], [], [], [], [], []]
week_limit = [35, 49]
Short_name = {'Іноземна мова І Шастало Віра Олександрівна (Пр)': 'Граматика#',
              'Інформаційні технології та академічна доброчесність Недовєсова Наталія Михайлівна (Л)': 'ІТ та АД+',
              'Іноземна мова І  (Пр)': 'Граматика#',
              'Іноземна мова ІІ(італ) Путівцева Наталія Костянтинівна (Пр)': 'Італійска\nПракт.#',
              'Вступ до фаху (філологія) Шевченко Ірина Семенівна (Пр)': 'Вступ#',
              'Україна в контексті історії Європи Домановська Марина Євгенівна (Л)': 'Історія+',
              'Кураторська година': 'Кур. Год.+',
              'Відпочинок': 'Відпочинок',
              'Українська мова за професійним спрямуванням Курушина Марина Анатоліївна (Л)': 'УМПС+',
              'Вступ до фаху (філологія) Шевченко Ірина Семенівна (Л)': 'Вступ+',
              'Інформаційні технології та академічна доброчесність(КузнєцоваОВ) Кузнєцова Ольга Володимирівна (Л)': 'ІТ та АД+',
              'Інформаційні технології та академічна доброчесність Недовєсова Наталія Михайлівна (Пр)': 'ІТ та АД#',
              'Українська мова за професійним спрямуванням Курушина Марина Анатоліївна (Пр)': 'УМПС#',
              'пів Іноземна мова І Шастало Віра Олександрівна (Пр)': '%Граматика#',
              'Іноземна мова ІІ(італійська) Безрук Інна Володимирівна (Пр)': 'Італійська\nГрам.#',
              'Усна практика іноземної мови І Гакало Даріна Олександрівна (Пр)': 'Усна\nпрактика#',
              'пів Іноземна  мова І Медвідь Марина Миколаївна (Пр)': '%Аналітика#',
              'Іноземна мова  І Гакало Даріна Олександрівна (Пр)': 'Усна\nпрактика#',
              'Іноземна  мова І Медвідь Марина Миколаївна (Пр)': 'Аналітика#',
              'пів Іноземна мова ІІ(італ) Путівцева Наталія Костянтинівна (Пр)': '%Італійська\nПракт.#',
              'Україна в контексті історії Європи Домановська Марина Євгенівна (Пр)': 'Історія#',
              'Понеділок': 'Пн',
              'Вівторок': 'Вт',
              'Середа': 'Ср',
              'Четвер': 'Чт',
              'П\'ятниця': 'Пт',
              'Субота': 'Сб',
              'Неділя': 'Нд'}
start_x = 0
week_number = datetime.today().isocalendar()[1]

date_file = open('date.txt', 'r')
if date_file.readline().rstrip() != datetime.today().strftime("%Y-%m-%d"):
    Update_data_info()
    date_file.close()
    date_file = open('date.txt', 'w')
    date_file.write(datetime.today().strftime("%Y-%m-%d"))
date_file.close()


def Read_week():
    day_iter = 0
    lesson_iter = 0
    print(week_number)
    file = open(str(week_number) + '.txt', 'r')
    for line in file:
        fill_button = Button()
        if line.rstrip() == 'NEXT_DAY':
            day_iter += 1
            lesson_iter = 0
        elif lesson_iter == 0:
            fill_button = Button(disabled=True, background_disabled_normal='', disabled_color=(1, 1, 1, 1),
                                 background_color=(124 / 255, 124 / 255, 124 / 255, 1), halign='center',
                                 text=f'{Short_name[line.split()[1].rstrip()]} \n {line[:5]}')
            week_button_matrix[day_iter].append(fill_button)
            lesson_iter += 1
        else:

            lesson_line = list(line.strip().split('//'))
            lesson_kay = Short_name.get(lesson_line[2].strip(), lesson_line[2])
            if lesson_kay == lesson_line[2]:
                fill_button = Button(disabled=True, background_disabled_normal='', disabled_color=(1, 1, 1, 1),
                                     background_color=(1, 0.3, 0.3, 1), halign='center',
                                     text=lesson_line[2].replace(' ', '\n'))

            if lesson_kay == 'Відпочинок':
                fill_button = Button(disabled=True)

            elif '+' in lesson_kay:
                fill_button = Button(disabled=True, background_disabled_normal='', disabled_color=(1, 1, 1, 1),
                                     background_color=(237 / 255, 195 / 255, 112 / 255, 1), halign='center',
                                     text=f'{lesson_kay[:-1]} \n {lesson_line[1]}')

            elif '#' in lesson_kay:
                fill_button = Button(disabled=True, background_disabled_normal='', disabled_color=(1, 1, 1, 1),
                                     background_color=(1 / 255, 170 / 255, 189 / 255, 1), halign='center',
                                     text=f'{lesson_kay[:-1]} \n {lesson_line[1]}')

            if '%' in lesson_kay:
                fill_button.text = f'{lesson_kay[1:-1]}'
                fill_button.size_hint = (1, 0.5)
                half_box = BoxLayout(orientation='vertical')
                half_box.add_widget(fill_button)
                half_box.add_widget(Button(disabled=True, size_hint=(1, 0.5)))
                fill_button = half_box

            week_button_matrix[day_iter].append(fill_button)
            lesson_iter += 1
    file.close()


def Add_to_row(n, box, Scrin):
    if n < 7:
        for i in range(7):
            box.add_widget(week_button_matrix[i][n])
    else:
        for i in range(7):
            box.add_widget(Button(disabled=True))
    Scrin.add_widget(box)


def Drow_Table():
    Table = BoxLayout(orientation='vertical')  # , size_hint = (0.91, 1)
    Sizes = (0.09, 0.041, 0.11, 0.0273, 0.11, 0.041, 0.11, 0.0273, 0.11, 0.0273, 0.11, 0.0273, 0.11, 0.055)
    lesson_row = 0
    for s in Sizes:
        Row = BoxLayout(orientation='horizontal', size_hint=(0.91, s), spacing=1)
        if s > 0.08:
            Add_to_row(lesson_row, Row, Table)
            lesson_row += 1
        else:
            Add_to_row(7, Row, Table)
    return Table


def touch_down(instance, touch):
    global start_x
    start_x = touch.x


def touch_up(instance, touch, Scrin, Table):
    global week_button_matrix
    global week_limit
    global week_number
    global start_x

    swipe_distanse = touch.x - start_x
    swipe = False
    if swipe_distanse > 300 and week_number != week_limit[0]:
        week_number -= 1
        swipe = True
    elif swipe_distanse < -300 and week_number != week_limit[1]:
        week_number += 1
        swipe = True
    start_x = 0
    if swipe == True:
        week_button_matrix = [[], [], [], [], [], [], []]
        Read_week()
        Scrin.remove_widget(Scrin.children[0])
        Table = Drow_Table()
        Scrin.add_widget(Table)


class TimeTableApp(App):
    def build(self):
        # Window.size = (324, 720)
        Window.clearcolor = (28 / 255, 28 / 255, 28 / 255, 1)  # (245, 245, 220, 1)

        Read_week()
        Table = Drow_Table()

        Hours_line = BoxLayout(orientation='vertical', size_hint=(0.09, 1), spacing=1)
        Hours_line.add_widget(Button(size_hint=(1, 0.09), disabled=True, background_disabled_normal='',
                                     background_color=(124 / 255, 124 / 255, 124 / 255, 1),
                                     disabled_color=(1, 1, 1, 1)))

        for hour in range(8, 19):
            Hours_line.add_widget(Button(size_hint=(1, 0.0823), text=str(hour) + ':00', background_disabled_normal='',
                                         disabled=True, background_color=(124 / 255, 124 / 255, 124 / 255, 1),
                                         disabled_color=(1, 1, 1, 1)))

        Scrin = BoxLayout(orientation='horizontal', spacing=5)
        Scrin.add_widget(Hours_line)
        Scrin.add_widget(Table)
        Scrin.bind(on_touch_down=touch_down)
        Scrin.bind(on_touch_up=lambda instance, touch: touch_up(instance, touch, Scrin, Table))
        return Scrin


if __name__ == "__main__":
    TimeTableApp().run()




