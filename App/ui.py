from PyQt5 import QtCore, QtGui, QtWidgets
from API_setup.Answer_processing import Model
import numpy as np
from gradio_client import Client


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        generalcontest= """
        bob tom and lucy are friends. they are completely normal people. bob and lucy are happily married. bob and lucy are loyal and really 
        love each other, their love is true. bob loves lucy. lucy loves bob. bob tom and lucy are middle aged. bob is blind. 
        bob is not religious. the story is set in the early 900's. the story is completely plausible and does not involve anything 
        not realistic.
        """.replace("\n","")

        piercontest="""
        A kind sailor saved Bob and Tom from an island and brought them to a pier. Now, they are sad and shocked. Bob does not know lucy  
        is dead, Tom knows Lucy is dead. They go to a restaurant. Bob orders seagull meat. The waiter brings bob the seagull meat. 
        Everything is ordinary. The seagull meat is perfectly fine and edible. After Bob takes a bite, he understands tom betrayed him. 
        Bob kills himself. Tom knew bob would suicide, so he is not surpirse. Other people at the restaurant were surprised. 
        Bob and tom were exhausted. bob and tom had discussions.  
        Bob wanted to go to the restaurant in order to eat seagull, bob had this plan when he was on the island and nothing 
        that happened changed bob's mind.
        """.replace("\n","")

        boatcontest="""
        bob tom and lucy are having fun. they did not have any argument. what happened was not upon them. 
        there is a storm and the boat is wrecked. bob, tom, lucy cast away on an island. 
        """.replace("\n","")

        general_islandcontest="""
        lucy dies in the shipwreck. bob and tom manage to survive. they are alone on the island. there is no one else on the island. there are 
        not dangerous animals. bob and tom do not have to fight to survive. there is no one else on the island. there is not much food.
        they resort to unconvential food sources. they did not have to fight. tom finds lucy's corpse. they manage to survive.
        tom is compelled to eat lucy. tom does not want to eat lucy. tom eats lucy. bob also eats lucy. because bob is blind, bob does not 
        know he is eating lucy. tom knows he is eating lucy. tom revolts while eating lucy. bob does not revolt while eating lucy. 
        tom tells bob he is eating seagull. bob thinks he is eating seagull. bob is suspicious. there is a sailor passing by. 
        the sailor saves bob and tom and brings them to a pier. the sailor is a good man. the sailor does not have ill intentions. 
        bob and tom are grateful to the sailor.bob does not know lucy is dead. tom knows lucy is dead.
        """.replace("\n","")

        boat_discover="""
        bob and tom went on a boat trip
        """.replace("\n","")

        island_discover="""
        bob and tom cast away on an island
        """.replace("\n","")

        final_discover="""
        bob realized he ate lucy
        """.replace("\n","")

        self.model=Model("API_setup/Model/")
        self.api =Client("https://manuu01-seagullstory.hf.space/")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-150, -180, 1000, 1000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/manu/mnt/DData/misc/Projects/Python/SeagullStory/App/Images/sad.jpg"))
        self.label.setObjectName("label")
        self.answer = QtWidgets.QLabel(self.tab)
        self.answer.setWordWrap(True)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)  # Set alignment to center

        self.answer.setGeometry(QtCore.QRect(100, 460, 300, 400))
        self.answer.setText("")
        self.answer.setObjectName("answer_4")
        self.answer.setStyleSheet("color: white;")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(100, 490, 301, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(180, 570, 140, 40))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.answer.setGeometry(QtCore.QRect(100, 460, 300, 400))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/manu/mnt/DData/misc/Projects/Python/SeagullStory/App/Images/sad.jpg"))
        self.label_2.setObjectName("label_2")
        self.answer_2 = QtWidgets.QLabel(self.tab_3)
        self.answer_2.setWordWrap(True)
        self.answer_2.setAlignment(QtCore.Qt.AlignCenter)  # Set alignment to center
        self.answer_2.setGeometry(QtCore.QRect(100, 460, 300, 400))
        self.answer_2.setText("")
        self.answer_2.setObjectName("answer_4")
        self.answer_2.setStyleSheet("color: white;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 490, 301, 71))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 570, 140, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(-150, -180, 1000, 1000))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/manu/mnt/DData/misc/Projects/Python/SeagullStory/App/Images/sad.jpg"))
        self.label_3.setObjectName("label_3")
        self.answer_3 = QtWidgets.QLabel(self.tab_2)
        self.answer_3.setGeometry(QtCore.QRect(100, 460, 300, 400))

        self.answer_3.setWordWrap(True)
        self.answer_3.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_3.setText("")
        self.answer_3.setObjectName("answer_4")
        self.answer_3.setStyleSheet("color: white;")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 490, 301, 71))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 570, 140, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(-150, -180, 1000, 1000))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/manu/mnt/DData/misc/Projects/Python/SeagullStory/App/Images/sad.jpg"))
        self.label_4.setObjectName("label_4")
        self.answer_4 = QtWidgets.QLabel(self.tab_4)
        self.answer_4.setGeometry(QtCore.QRect(100, 460, 300, 400))
        self.answer_4.setWordWrap(True)
        self.answer_4.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_4.setText("")
        self.answer_4.setObjectName("answer_4")
        self.answer_4.setStyleSheet("color: white;")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 490, 301, 71))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 570, 140, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.pushButton_4.clicked.connect(lambda x : self.on_button_click(self.answer_4,self.lineEdit_4.text(),"Island"))
        self.pushButton_3.clicked.connect(lambda x : self.on_button_click(self.answer_3,self.lineEdit_3.text(),"Boat"))
        self.pushButton_2.clicked.connect(lambda x : self.on_button_click(self.answer_2,self.lineEdit_2.text(),"Pier"))
        self.pushButton.clicked.connect(lambda x : self.on_button_click(self.answer,self.lineEdit.text(),"General"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_button_click(self,label,question,passage):
        result=self.model.get_predict(question,"bob has a girlfriend")
        if(np.argmax(result)==0):
            label.setText("That's right! Bob has a girlfriend. From now on, you can refer to her as Lucy")
            return
        result=self.model.get_predict(question, "bob is blind")
        if(np.argmax(result)==0):
            label.setText("That's right! Bob is blind")
            return
         
        result = self.api.predict(
                        passage,	# str (Option from: ['General', 'Pier', 'Boat', 'Island'])
                        question,	# str in 'enter your question' Textbox component
                        api_name="/predict"
        )
        label.setText(result)
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter question"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter question"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pier"))
        self.pushButton_3.setText(_translate("MainWindow", "Enter question"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Boat"))
        self.pushButton_4.setText(_translate("MainWindow", "Enter question"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Island"))
