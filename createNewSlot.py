from connectiondeMysql import DBConnection
import MySQLdb

class createNewSlot:
	dbConn = DBConnection()	
	db = dbConn.getDBConnection()
	cur = db.cursor()

	def __init__(self):
		print "Hi, Welcome to the daashboard, please tell how many slots you want to enter:"
		slots = input()
		if(slots>0):
			for i in range (0, slots):
				print "Entering the "+ str(i+1) + " new slot:"
				query = "insert into Slots values(default, null)"
				try:
					self.cur.execute(query)
					if self.cur.lastrowid:
						print('last insert id', self.cur.lastrowid)
					else:
						print('last insert id not found')
					self.db.commit()
				except (MySQLdb.Error, MySQLdb.Warning) as e:
					print (e)

		else:
			print "Sorry, that is not an acceptable value for inserting the number of rows"

ob = createNewSlot()