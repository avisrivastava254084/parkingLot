import MySQLdb

class DBConnection:
	db = MySQLdb.connect(host="localhost", user="root", passwd="indicadls02", db="parking_lot")

	def getDBConnection(self):
		print "yo"
		return self.db
