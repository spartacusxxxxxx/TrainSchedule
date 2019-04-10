import sqlite3

conn = sqlite3.connect("TrainSchedule.db")
cursor = conn.cursor()

# Create table cities
cursor.execute("DROP TABLE IF EXISTS cities")
cursor.execute("""CREATE TABLE IF NOT EXISTS 
	cities (city_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ON CONFLICT REPLACE, 
			city_name TEXT NOT NULL UNIQUE);""")
conn.commit()

cities   = [(1, 'Torzhok'),
			(2, 'Likhoslavl'),
			(3, 'Tver'),
			(4, 'Vyshny Volochek'),
			(5, 'Spirovo'),
			(6, 'Bologoye'),
			(7, 'Firovo'),
			(8, 'Ostashkov'),
			(9, 'Peno'),
			(10, 'Selijarovo'),
			(11, 'Kuvshinovo'),
			(12, 'Staritsa'),
			(13, 'Rzhev'),
			(14, 'Olenino'),
			(15, 'Nelidovo'),
			(16, 'Zap Dvina'),
			(17, 'Zharkovsky'),
			(18, 'Andreapol'),
			(19, 'Toropets'),
			(20, 'Udomlya'),
			(21, 'Maksatiha'),
			(22, 'Bezhetsk'),
			(23, 'Sonkovo'),
			(24, 'Kashin'),
			(25, 'Kalyazin'),
			(26, 'Savyolovo'),
			(27, 'Sandovo'),
			(28, 'Krasnyy Kholm'),
			(29, 'Vesegonsk')]

cursor.executemany("INSERT INTO cities VALUES(?, ?)", cities)
conn.commit()