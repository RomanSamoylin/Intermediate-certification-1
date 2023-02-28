from View.Display import Display
from DataBase.DataBase import Database
from FileManager.XMLfileManager import XMLfileManager

d1 = Display()
db = Database(d1)


fm = XMLfileManager()

db.notepad=fm.load()
db.list()