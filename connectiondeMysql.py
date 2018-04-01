import MySQLdb

class DBConnection:
	db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="parking_lot")

	def getDBConnection(self):
		print "Attempting to connect to DB"
		return self.db
