from connectiondeMysql import DBConnection
import MySQLdb

class chargeSlot:
	
	dbConn = DBConnection()	
	db = dbConn.getDBConnection()
	cur = db.cursor()

	def __init__(self, slot):
		self.slot = slot

	def vacateSlot(self):
		print "Vacating the slot#: " + str(slot)
		query = "update Slots set car_number = null, car_color = null where id = "+ str(slot)
		print query
		try:
			self.cur.execute(query)
			self.db.commit()
			print "Slot #: " + str(slot) + " is vacated"
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print e
		
slot = raw_input("Please enter the slot number to be freed \n " )
chargeSlotObject = chargeSlot(slot)
chargeSlotObject.vacateSlot()