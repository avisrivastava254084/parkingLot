from connectiondeMysql import DBConnection
import MySQLdb

class tickets:
	dbConn = DBConnection()	
	db = dbConn.getDBConnection()
	cur = db.cursor()

	def __init__(self, carNumber, carColor):
		self.carNumber = carNumber
		self.carColor = carColor
		print "hi avi"
		print "the car number is: " + str(self.carNumber)
		print "the car color is: " + str(self.carColor)

	def generateTicket(self):
		if(self.checkSlot() == True):
			slot = self.nearestSlot()
			ticket = str(slot) + "~" + self.carNumber +  "~" + self.carColor 
			print ticket
		else:
			print ("Sorry, no slots left")

	def checkSlot(self):
		print "Checking slots"
		query = "select * from Slots where car_number is null"
		try:
			self.cur.execute(query)
			rows = self.cur.rowcount
			if(rows > 0):
				print "Slots available"
				return True
			else:
				print "No Slot left"
				return False
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print e
		
	def nearestSlot(self):
		print "Checking the nearest slot to the entry"
		query = "select * from Slots where car_number is null order by id limit 1"
		try:
			self.cur.execute(query)
			row = self.cur.fetchone()
			row = row[0]
			print "The id to be used is: " + str(row)
			query = "update Slots set car_number = "+ "\""+ self.carNumber + "\"" + " where id = "+str(row)
			print query
			try:
				self.cur.execute(query)
				self.db.commit()
				return row
			except (MySQLdb.Error, MySQLdb.Warning) as e:
				print e
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print e

a = tickets("AVI2", "White")
a.generateTicket()