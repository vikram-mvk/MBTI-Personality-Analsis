
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):                    #UI Done using PyQt.Twitter id's are stored in a list called me
                                                # A function called 'Operation' is then called which is defined below                
    def hi(self,):
        me = list()
        me.append(self.textEdit_x.toPlainText())
        me.append(self.textEdit_2.toPlainText())
        me.append(self.textEdit_3.toPlainText())
        me.append(self.textEdit_4.toPlainText())
        me.append(self.textEdit_5.toPlainText())
        me.append(self.textEdit_6.toPlainText())
        me.append(self.textEdit_7.toPlainText())
        me.append(self.textEdit_8.toPlainText())
        me.append(self.textEdit_9.toPlainText())
        me.append(self.textEdit_10.toPlainText())

        
        i=self.comboBox.currentIndex()
        operation(me,i)

       
   
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_x = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_x.setGeometry(QtCore.QRect(200, 20, 231, 31))
        self.textEdit_x.setObjectName("textEdit_x")
        self.textEdit_x.setText("PoseidonsPonder")

        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 70, 231, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText("james_r_eads")
        
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 120, 231, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText("jerrydunleavy")
        
        
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 170, 231, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setText("JordanSweeto")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(200, 220, 231, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setText("pageaujonathan")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(200, 270, 231, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setText("KimKardashian")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(200, 320, 231, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_7.setText("aamir_khan")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(200, 370, 231, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_8.setText("artistclairep")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(200, 420, 231, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_9.setText("suffolkpainter")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(200, 470, 231, 31))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_10.setText("gerwingM")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 78, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 280, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 330, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 380, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 430, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 480, 91, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 470, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.hi)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(640, 320, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(540, 320, 81, 31))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CANDIDATE 1"))
        self.label_2.setText(_translate("MainWindow", "CANDIDATE 2"))
        self.label_3.setText(_translate("MainWindow", "CANDIDATE 3"))
        self.label_4.setText(_translate("MainWindow", "CANDIDATE 4"))
        self.label_5.setText(_translate("MainWindow", "CANDIDATE 5"))
        self.label_6.setText(_translate("MainWindow", "CANDIDATE 6"))
        self.label_7.setText(_translate("MainWindow", "CANDIDATE 7"))
        self.label_8.setText(_translate("MainWindow", "CANDIDATE 8"))
        self.label_9.setText(_translate("MainWindow", "CANDIDATE 9"))
        self.label_10.setText(_translate("MainWindow", "CANDIDATE 10"))
        self.pushButton.setText(_translate("MainWindow", "GO"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MANAGER"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HUMAN RESOURCE"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ACCOUTING"))
        self.comboBox.setItemText(3, _translate("MainWindow", "MARKETING"))
        self.label_11.setText(_translate("MainWindow", "Select Role:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        
        
        
        


def operation(me,i):                                            
    a=list()
    
    for j in range(0,9):
        print(me[j])
        get_all_tweets(me[j])
        eg=type_return()
        po=  eg
        a.append(po)
        
    ko=0
    print("######################################")
    print(" THE ELIGIBLE CANDIDATES ARE :")
    
    for j in a:
   # variable i is the parameter that says what Post is selected in dropdown list. ex: i=0 is manager

        if i == 0:
            if j== 'INTJ' or j== 'ENTJ' or j== 'ESFP' or j== 'ENTP' :
                print(me[ko])
                test=1
            
            #if manager(i=0) is selected candidate should be INTJ or ENTJ or ESPF or ENTP
       
        if i == 1:
            if j== 'INFP' or j== 'ENFP' or j== 'ISTP'or j== 'ISFP' :
                print(me[ko])
                test=1
        if i == 2:
            if j== 'INTJ' or j== 'ISTJ' or j== 'ESFJ' or j== 'INFJ' :
                print(me[ko])
                test=1
                
        if i == 3:
            if j== 'ISTP' or j== 'ISFP' or j== 'ESTP' or j== 'INTP' :
                print(me[ko])
                test=1
        ko=ko+1
                
        
    if test==0:
        print("None of the candidates are eligible")
        
        
        

        
        












def type_return():              #Main Algorithm
    
   # import numpy as np
    import pandas as pd
   # from sklearn import *
    import sklearn
    from sklearn import ensemble ,feature_extraction,decomposition,pipeline

#have these files in ur E drive if you wanna test
    
    train = pd.read_csv('e:/mbti3.csv')       #traing dataset
    user_list = pd.read_csv('e:/User.csv')    #dummy file to perform join operation
    post_list = pd.read_csv('e:/book3.csv')   #extracted tweets 

    post_list = pd.merge(post_list, user_list, how='left', left_on='id', right_on='user')  #database style join operation
    sample_set = {}

    y=len(post_list)
    for i in range(len(post_list)):
        if post_list['id'][i] in sample_set:
            sample_set[str(post_list['id'][i])] += ' ' + str(post_list['text'][i])
            print(y)
            y=y-1
        else:
                sample_set[str(post_list['id'][i])] = str(post_list['text'][i])
      #  print("22")
        
        

    etc = ensemble.ExtraTreesClassifier(n_estimators = 20, max_depth=4, n_jobs = -1)
    #print(etc)
    tfidf = feature_extraction.text.TfidfVectorizer(ngram_range=(1, 1), stop_words='english')
    #print(tfidf)
    tsvd = decomposition.TruncatedSVD(n_components=10)
    #print(tsvd)
    model = pipeline.Pipeline([('tfidf1', tfidf), ('tsvd1', tsvd), ('etc', etc)])
    #print("pipelined")
    model.fit(train['posts'], train['type'])
    #print("Trained")

    pred = model.predict([sample_set['dummy']])[0]

    #print("@@@@@@@@@@@@")
    print(pred)
    #print("@@@@@@@@@@@@")

    return str(pred)




def get_all_tweets(screen_name):
	import tweepy
	import csv

#Twitter API credentials
	consumer_key = "v08vV2DTbiJw2o9jjsdWqroJf"
	consumer_secret = "ReFCuXOjwH8eMfbqNZs7Uu9vjo8BsiefkRSrWDinNPYr6ubfPe"
	access_key = "2164937185-WWLNcbItuk6hf0id7xsGrSsOYpICtdbRAMiYeux"
	access_secret = "qNkz5hmky1vOaG75XUsyvUTs2hwjrq9FaaisLhIwJgdxc"



	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	alltweets.clear()
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0 and len(alltweets) < 4000:
	#	print(oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		print("Tweets extracted")         
		print(len(alltweets))
        
		
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [['dummy', tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	f = open("e:/book3.csv", "w")
	f.truncate()

	with open('e:/book3.csv', 'w') as f:  #extraction of tweets
		writer = csv.writer(f)
		hello=["id","text"]
		writer.writerow(hello)
		writer.writerows(outtweets)
	
	pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())        
