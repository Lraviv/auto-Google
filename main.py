''''
automation which sign in to gmail account by email & password
which is saved in other file [creds.txt] and then opens classroom
'''
import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# ------------------------------UI-----------------------------------------------------------
def main_pyqt():
    '''main graphic design (ui)'''
    # initial the pyqt module
    global window
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Auto-Google")
    window.setWindowIcon(QIcon("icon.png"))
    window.setGeometry(50,50,1000,600)

    # welcome text
    welcome_label = QLabel(window)
    welcome_label.setText("welcome to Auto-Google")  # welcome text
    welcome_label.setFont(QFont('Aharoni', 40))  # set font and size of text
    welcome_label.adjustSize()
    welcome_label.move(10,30)

    # instructions text
    inst_label = QLabel(window)
    inst_text = "welcome to auto-google! set your gmail and password in" \
                "the creds.txt file and then click on the app \nwhich you want" \
                " to connect to!"
    inst_label.setText(inst_text)  # welcome text
    inst_label.setFont(QFont('Aharoni', 10))  # set font and size of text
    inst_label.adjustSize()
    inst_label.move(10, 100)

    # logged in text
    gmail = get_email()[0]
    user_label = QLabel(window)
    user_text = "you are logged in as: "+ gmail
    user_label.setText(user_text)  # welcome text
    user_label.setFont(QFont('Courier New', 10))  # set font and size of text
    user_label.adjustSize()
    user_label.move(250, 170)

    # inside window icon picture
    pic_label = QLabel(window)
    pic = QPixmap('icon.png')
    pic = pic.scaledToWidth(150)  # adjust image width
    pic = pic.scaledToHeight(150)  # adjust image height
    pic_label.setPixmap(pic)
    pic_label.move(800,0)

    # classroom button
    classroom_bt = QPushButton(window)
    classroom_bt.setText(" Classroom")   # button text
    classroom_bt.setFont(QFont('Aharoni', 15))  # button font and size
    classroom_bt.setStyleSheet("border: 2px solid ;"
                               "border-color :blue;"
                               "border-radius : 15px"
                               "QPushButton::hover"
                               "{"
                               "background-color : blue;"
                               "}"
                               )  # create a blue-round border and turn button blue when mouse on button
    classroom_bt.setIcon(QIcon('classroom.png'))  # button icon
    classroom_bt.setGeometry(0,0,400,50)    # button size
    classroom_bt.clicked.connect(classroom_button)  # if button is clicked
    classroom_bt.move(300, 200)

    # classos button
    classos_bt = QPushButton(window)
    classos_bt.setText(" Classoos")  # button text
    classos_bt.setFont(QFont('Aharoni', 15))  # button font and size
    classos_bt.setStyleSheet("border: 2px solid ;"
                               "border-color :blue;"
                               "border-radius : 15px"
                               "QPushButton::hover"
                               "{"
                               "background-color :blue;"
                               "}"
                               )   # create a blue-round border and turn button blue when mouse on button
    classos_bt.setIcon(QIcon('classos.png'))  # button icon
    classos_bt.setGeometry(0, 0, 400, 50)  # button size
    classos_bt.clicked.connect(classos_button)  # if button is clicked
    classos_bt.move(300, 280)

    # gmail button
    gmail_bt = QPushButton(window)
    gmail_bt.setText(" gmail")  # button text
    gmail_bt.setFont(QFont('Aharoni', 15))  # button font and size
    gmail_bt.setStyleSheet("border: 2px solid ;"
                               "border-color :blue;"
                               "border-radius : 15px"
                               "QPushButton::hover"
                               "{"
                               "background-color : blue;"
                               "}"
                               )    # create a blue-round border and turn button blue when mouse on button
    gmail_bt.setIcon(QIcon('gmail.png'))  # button icon
    gmail_bt.setGeometry(0, 0, 400, 50)  # button size
    gmail_bt.clicked.connect(gmail_button)  # if button is clicked
    gmail_bt.move(300, 360)

    # show window
    window.show()
    sys.exit(app.exec_())

# Buttons :


def classroom_button():
    # if the classroom button clicked, open classroom
    print("classroom button was clicked")
    open_classroom()


def classos_button():
    # if the classos button is clicked, open classos
    print("classoos button was clicked")
    open_classos()


def gmail_button():
    # if gmail button is clicked, open gmail
    print("gmail button was clicked")
    open_gmail()

# ------------------------------UX---------------------------------------------------------


def initial_browser():
    # initial browser

    # keep browser open at the end
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # initial browser
    s = Service(ChromeDriverManager().install())
    global browser
    browser = webdriver.Chrome(service=s)


def get_email():
    # get credentials (gmail and password) from file [creds.txt]
    with open('creds.txt', 'r') as f:
        lines = ''
        for line in f:
            lines += line
        (gmail, password) = lines.split('\n')
        f.close()
    return gmail, password


def sign_in_with_gmail():
    # open google with gmail account
    global browser
    browser.get('https://accounts.google.com/ServiceLogin')  # get to the gmail sign in page
    browser.implicitly_wait(15)

    # try to log in
    try:
        email_id = 'identifierId'
        password_path = '//*[@id="password"]/div[1]/div/div[1]/input'
        send_creds(email_id, password_path)
        # print if log in succeeded
        print("login succeeded")
        time.sleep(4)

    except Exception as E:
        # print if login failed
        print("login failed")
        print(E)


def open_classroom():
    # open the classroom of the gmail account that opened
    global browser
    initial_browser()
    sign_in_with_gmail()    # open google with gmail account
    try:
        browser.get('https://classroom.google.com/h')
        # print success message
        print("classroom opened successfully")

    except Exception as E:
        print("classroom opening failed")
        print("ERROR: ", E)


def open_classos():
    # open and login classos ( a website for study-books)
    global browser
    initial_browser()
    browser.get('https://my.classoos.com/il/login/main')  # go to classos url
    time.sleep(4)
    try:
        # go to mail log in
        connect_with_gmail = browser.find_element(By.XPATH, '//*[@id="login-boxes"]/div[3]/div[4]/a')
        connect_with_gmail.click()
        time.sleep(1)
        email_id = 'identifierId'
        password_path = '//*[@id="password"]/div[1]/div/div[1]/input'
        send_creds(email_id, password_path)
        print("classoos opened successfully")
    except Exception as E:
        print("failed to login to classos")
        print(E)


def open_gmail():
    # open your gmail account
    global browser
    initial_browser()
    sign_in_with_gmail()    # open google with gmail account
    try:
        # go to the gmail inbox url
        browser.get('https://mail.google.com/mail/u/0/#inbox')
        print("gmail opened successfully")  # success message
    except Exception as E:
        print(" couldn't open gmail")   # fail message
        print("ERROR: ", E)


def send_creds(email_id, password_path):
    # type in email and password in the paths that were given
    global browser
    (gmail,password) = get_email()
    # enter email
    email_box = browser.find_element(By.ID, email_id)
    email_box.click()
    email_box.send_keys(gmail)  # send the mail to email box
    email_box.send_keys(Keys.ENTER)
    time.sleep(2)
    # enter password
    password_box = browser.find_element(By.XPATH, password_path)
    password_box.click()
    password_box.send_keys(password)  # send the password to password box
    password_box.send_keys(Keys.ENTER)


if __name__ == '__main__':
    main_pyqt()






