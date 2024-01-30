from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys
import proxy

window=None
web=None
listbox=None
searchengine=["https://google.com","https://duckduckgo.com","https://bing.com","https://yandex.com"]
socket=None  


def select(): 
    global listbox
    global web
    global window
    url=searchengine[listbox.currentIndex()]
    web.setUrl(QUrl(url))
    window.setCentralWidget(web)
    window.show()

def conn():
    global socket
    try:
        socket=proxy.connect()
    except TimeoutError:
        return
def disc():
    global socket
    try:
        proxy.disconnect(socket)
    except AttributeError:
        return

def display():
    global listbox
    global web
    global window
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setWindowTitle("BROWSER")
    window.setGeometry(100,100,1000,900)
    
    toolbar=QToolBar()
    window.addToolBar(toolbar)
     
    web=QWebEngineView()
    
    back=QPushButton("BACK",window)
    back.clicked.connect(web.back)
    toolbar.addWidget(back)

    forward=QPushButton("FORWARD",window)
    forward.clicked.connect(web.forward)
    toolbar.addWidget(forward)

    rel=QPushButton("RELOAD",window)
    rel.clicked.connect(web.reload)
    toolbar.addWidget(rel)


    
    listbox=QComboBox()
    listbox.addItem("GOOGLE")
    listbox.addItem("DUCK DUCK GO")
    listbox.addItem("BING")
    listbox.addItem("YANDEX")
    toolbar.addWidget(listbox)

    sel=QPushButton("SELECT",window)
    sel.clicked.connect(select)
    toolbar.addWidget(sel) 

    connect=QPushButton("CONNECT TO PROXY",window)
    connect.clicked.connect(conn)
    toolbar.addWidget(connect)

    discon=QPushButton("DISCONNECT",window)
    discon.clicked.connect(disc)
    toolbar.addWidget(discon)

   
    window.show()

    sys.exit(app.exec())
    


display()