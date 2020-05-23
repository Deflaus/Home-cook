
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from view import Ui_Form, WindowRecipe
from dbaccess import DataBaseAccess
import operator

call = {"Курица": 1.9, "Свинина": 2.6, "Говядина": 1.85,"Баранина": 2.1,
        "Картофель": 0.75, "Капуста": 0.15, "Помидор": 0.2, "Огурец": 0.15, "Морковь": 0.32, "Лук": 0.4,
        "Семга": 1.9, "Мидии": 0.6, "Тунец": 1.3, "Креветки": 1,
        "Вермиешль": 3.45, "Спагетти": 3.45, "Рожки": 3.45, "Фунчоза": 3.2,
        "Шампиньоны": 0.5, "Белые грибы": 0.4, "Опята": 0.2, "Лисички": 0.2,
        "Банан": 0.95, "Яблоко": 0.5, "Апельсин": 0.35, "Дыня": 0.33, "Киви": 0.48,
        "Яйцо": 1.57, "Сыр": 3.6, "Маргарин": 7, "Укроп": 0.4}
id_ingr = DataBaseAccess.parse_ingridients()
comform = DataBaseAccess.parse_conform()
titles = DataBaseAccess.parse_titles()
textrecipes = DataBaseAccess.parse_recipes()


def main_button():
    Window.FindRec.show()
    Window.Ingridients.show()
    Window.Callories_3.hide()
    Window.TopRec_3.hide()
    Window.Instructions.hide()


def toprec_button():
    Window.Callories_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.Instructions.hide()
    Window.TopRec_3.show()
    rate = DataBaseAccess.parse_rate()
    sorted_rate = sorted(rate.items(), key=operator.itemgetter(1), reverse=True)

    Window.listWidget_1.clear()
    Window.listWidget_2.clear()
    Window.listWidget_3.clear()

    Window.TopRec2.show()
    Window.TopRec3.show()
    Window.TopRec1.show()

    Window.updateimg1(str(sorted_rate[0][0]) + "5")
    title = titles[sorted_rate[0][0]]
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_1.addItem(item)
    title = "Оценка рецепта: " + str(sorted_rate[0][1])
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_1.addItem(item)

    Window.updateimg2(str(sorted_rate[1][0]) + "5")
    title = titles[sorted_rate[1][0]]
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_2.addItem(item)
    title = "Оценка рецепта: " + str(sorted_rate[1][1])
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_2.addItem(item)

    Window.updateimg3(str(sorted_rate[2][0]) + "5")
    title = titles[sorted_rate[2][0]]
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_3.addItem(item)
    title = "Оценка рецепта: " + str(sorted_rate[2][1])
    item = QtWidgets.QListWidgetItem(title)
    Window.listWidget_3.addItem(item)


def instr_button():
    Window.Instructions.show()
    Window.Callories_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.TopRec_3.hide()


def callories_button():
    Window.Callories_3.show()
    Window.TopRec_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.Instructions.hide()


def callories():
    try:
        int(Window.Weight.text())
        Window.label_callories.setText("Количество калорий: " + str(int(Window.Weight.text())*call[Window.Title.text()]))
    except:
        Window.label_callories.setText("Введите целое число(!)")


def findrecbutclicked():
    try:
        recipes = []
        arr = Window.text.split(". ")
        for i in range(0, len(arr) - 1):
            arr[i] = id_ingr[arr[i]]
        for j in comform:
            count = 0
            for i in range(0, len(arr) - 1):
                instr = str(comform[j]).find(str(arr[i]))
                if instr % 2 == 0 and instr != -1:
                    count += 1
            if count == len(arr) - 1:
                recipes.append(j)
        Window.FindRec.hide()
        Window.Ingridients.hide()
        Window.TopRec_3.show()

        Window.TopRec3.setVisible(False)
        Window.TopRec2.setVisible(False)
        Window.TopRec1.setVisible(False)

        Window.label_error.setText("")
        Window.listWidget_1.clear()
        Window.listWidget_2.clear()
        Window.listWidget_3.clear()
        if len(recipes) > 0:
            Window.updateimg1(str(recipes[0]) + "5")
            Window.TopRec2.setVisible(True)
            title = titles[recipes[0]]
            item = QtWidgets.QListWidgetItem(title)
            Window.listWidget_1.addItem(item)
            if len(recipes) > 1:
                Window.updateimg2(str(recipes[1]) + "5")
                title = titles[recipes[1]]
                item = QtWidgets.QListWidgetItem(title)
                Window.listWidget_2.addItem(item)
                Window.TopRec3.setVisible(True)
                if len(recipes) > 2:
                    Window.updateimg3(str(recipes[2]) + "5")
                    title = titles[recipes[2]]
                    item = QtWidgets.QListWidgetItem(title)
                    Window.listWidget_3.addItem(item)
                    Window.TopRec1.setVisible(True)
        else:
            Window.label_error.setText("Рецептов с такими ингредиентами нет(")
    except:
        pass


def rec1clicked():
    WindowRecipe.Step1.clear()
    WindowRecipe.Step2.clear()
    WindowRecipe.Step3.clear()
    WindowRecipe.Step4.clear()
    WindowRecipe.Step5.clear()

    title = Window.listWidget_1.item(0).text()
    WindowRecipe.label.setText(title)
    number = 0
    for i in titles:
        if titles[i] == title:
            number = i
    text = textrecipes[number].split('\\n')

    item = QtWidgets.QListWidgetItem(text[0])
    WindowRecipe.Step1.addItem(item)

    item = QtWidgets.QListWidgetItem(text[1])
    WindowRecipe.Step2.addItem(item)

    item = QtWidgets.QListWidgetItem(text[2])
    WindowRecipe.Step3.addItem(item)

    item = QtWidgets.QListWidgetItem(text[3])
    WindowRecipe.Step4.addItem(item)

    item = QtWidgets.QListWidgetItem(text[4])
    WindowRecipe.Step5.addItem(item)

    FormRecipe.showMaximized()
    WindowRecipe.update_imgs(number)


def rec2clicked():
    WindowRecipe.Step1.clear()
    WindowRecipe.Step2.clear()
    WindowRecipe.Step3.clear()
    WindowRecipe.Step4.clear()
    WindowRecipe.Step5.clear()

    title = Window.listWidget_2.item(0).text()
    WindowRecipe.label.setText(title)
    number = 0
    for i in titles:
        if titles[i] == title:
            number = i
    text = textrecipes[number].split('\\n')

    item = QtWidgets.QListWidgetItem(text[0])
    WindowRecipe.Step1.addItem(item)

    item = QtWidgets.QListWidgetItem(text[1])
    WindowRecipe.Step2.addItem(item)

    item = QtWidgets.QListWidgetItem(text[2])
    WindowRecipe.Step3.addItem(item)

    item = QtWidgets.QListWidgetItem(text[3])
    WindowRecipe.Step4.addItem(item)

    item = QtWidgets.QListWidgetItem(text[4])
    WindowRecipe.Step5.addItem(item)

    FormRecipe.showMaximized()
    WindowRecipe.update_imgs(number)


def rec3clicked():
    WindowRecipe.Step1.clear()
    WindowRecipe.Step2.clear()
    WindowRecipe.Step3.clear()
    WindowRecipe.Step4.clear()
    WindowRecipe.Step5.clear()

    title = Window.listWidget_3.item(0).text()
    WindowRecipe.label.setText(title)
    number = 0
    for i in titles:
        if titles[i] == title:
            number = i
    text = textrecipes[number].split('\\n')

    item = QtWidgets.QListWidgetItem(text[0])
    WindowRecipe.Step1.addItem(item)

    item = QtWidgets.QListWidgetItem(text[1])
    WindowRecipe.Step2.addItem(item)

    item = QtWidgets.QListWidgetItem(text[2])
    WindowRecipe.Step3.addItem(item)

    item = QtWidgets.QListWidgetItem(text[3])
    WindowRecipe.Step4.addItem(item)

    item = QtWidgets.QListWidgetItem(text[4])
    WindowRecipe.Step5.addItem(item)

    FormRecipe.showMaximized()
    WindowRecipe.update_imgs(number)


def buttonlikeclicked():
    title = WindowRecipe.label.text()
    rate = DataBaseAccess.parse_rate()
    number = 0
    for i in titles:
        if titles[i] == title:
            number = i
    DataBaseAccess.update_rate(number, rate[number] + 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    FormRecipe = QtWidgets.QWidget()

    Window = Ui_Form()
    WindowRecipe = WindowRecipe()

    Window.setupUi(Form)
    Window.Main.clicked.connect(main_button)
    Window.TopRec.clicked.connect(toprec_button)
    Window.Callories.clicked.connect(callories_button)
    Window.Instruction.clicked.connect(instr_button)
    Window.pushButton.clicked.connect(findrecbutclicked)
    Window.pushButton_5.clicked.connect(callories)
    Window.pushButton_3.clicked.connect(rec1clicked)
    Window.pushButton_4.clicked.connect(rec2clicked)
    Window.pushButton_2.clicked.connect(rec3clicked)

    WindowRecipe.setupUi(FormRecipe)
    WindowRecipe.Like.clicked.connect(buttonlikeclicked)

    Form.showMaximized()

    Window.Callories_3.hide()
    Window.TopRec_3.hide()
    Window.Instructions.hide()

    sys.exit(app.exec_())

