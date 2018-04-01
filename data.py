from connectiondeMysql import DBConnection
import MySQLdb

class data:
	dbConn = DBConnection()	
	db = dbConn.getDBConnection()
	cur = db.cursor()

	def __init__(self, color=None, slot=None):
		self.color = color
		self.slot = slot

	def carsByColor(self):
		print "Displaying cars of the color: " + self.color
		query = "select * from Slots where car_color = '" + str(self.color) + "'"
		try:
			self.cur.execute(query)
			rows = self.cur.rowcount
			if(rows == 0):
				print "No cars of this color"
			else:
				for row in self.cur:
					print row
		
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print e

	def carBySlot(self):
		print "Displaying car in the slot: " + str(self.slot)
		query = "select * from Slots where id = " + str(self.slot)
		try:
			self.cur.execute(query)
			rows = self.cur.rowcount
			if(rows == 0):
				print "No cars in this slot"
			else:
				for row in self.cur:
					print row
		
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print e

print ("Enter 1 for Color, 2 for slot or 3 for both: \n")
choice = input()
if(choice == 1):
	color = raw_input("Please enter the color: ")
	dataObject = data(color)
	dataObject.carsByColor()
elif(choice == 2):
	slot = raw_input("Please enter the slot: ")
	dataObject = data(slot)
	dataObject.carBySlot()
elif(choice == 3):
	color = raw_input("Please enter the color: ")
	slot = raw_input("Please enter the slot: ")
	dataObject = data(color, slot)
	dataObject.carsByColor()
	dataObject.carBySlot()
else:
	print "Wrong choice mate!"