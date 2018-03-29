from connectiondeMysql import DBConnection

class tickets:
	dbConn = DBConnection()	
	db = dbConn.getDBConnection()
	cur = db.cursor()

	def __init__(self, maximumSlots, carNumber, carColor):
		self.maximumSlots = maximumSlots
		self.carNumber = carNumber
		self.carColor = carColor
		print "hi avi"
		print "maximum slots are: " + str(self.maximumSlots)
		print "the car number is: " + str(self.carNumber)
		print "the car color is: " + str(self.carColor)

	def generateTicket(self):
		if(checkSlot):
			slot = self.nearestSlot()
			return slot
		else:
			return ("Sorry, no slots left")

	def checkSlot(self):
		print "Checking slots"
		query = "select max(id) from Slots where car_number is null"
		self.cur.execute(query)
		rows = self.cur.fetchone()
		if(rows[0] != null):
			print "the first slot to be entered is: " + str(rows[0])
		#if(rows > self.maximumSlots):
		#	return false
		#else:
		#	query = "update Slots set carNumber = "+self.carNumber+" where id = "+rows


a = tickets(4, "UP31F3393", "White")
a.checkSlot()