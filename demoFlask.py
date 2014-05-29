from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)


class Output(db.Model):
	__tablename__ = 'output'

	ID = db.Column(db.Integer, primary_key=True)
	LINE_NUMBER = db.Column(db.Integer)
	ZONE_NUMBER = db.Column(db.Integer)
	TIME_RANGE = db.Column(db.String(20))
	DIRECTION = db.Column(db.String(8))
	SCHEDULED_RUN_TIME = db.Column(db.Integer)
	TOTAL_OPERATING_COST = db.Column(db.Float)
	FARE_COLLECTED = db.Column(db.Float)
	FAREBOX_RECOVERY = db.Column(db.Float)
	DATE_STORED = db.Column(db.String(20))
	PCNAME = db.Column(db.String(10))
	SIGN_ON_DATE = db.Column(db.String(20))
	OPERATING_COST_PER_HOUR = db.Column(db.Float)
	RECOVERY_PROCESSING_ID = db.Column(db.Integer)
	AGGREGATE_ID = db.Column(db.Integer)
	COUNTY = db.Column(db.String(20))
	TYPE = db.Column(db.String(10))

	def __init__(self, ID, LINE_NUMBER, ZONE_NUMBER, \
		TIME_RANGE, DIRECTION, SCHEDULED_RUN_TIME, TOTAL_OPERATING_COST, \
		FARE_COLLECTED, FAREBOX_RECOVERY, DATE_STORED, PCNAME, SIGN_ON_DATE, \
		OPERATING_COST_PER_HOUR, RECOVERY_PROCESSING_ID, AGGREGATE_ID, COUNTY, TYPE):
		self.ID = ID
		self.LINE_NUMBER = LINE_NUMBER
		self.ZONE_NUMBER = ZONE_NUMBER
		self.TIME_RANGE = TIME_RANGE
		self.DIRECTION = DIRECTION
		self.SCHEDULED_RUN_TIME = SCHEDULED_RUN_TIME
		self.TOTAL_OPERATING_COST = TOTAL_OPERATING_COST
		self.FARE_COLLECTED = FARE_COLLECTED
		self.FAREBOX_RECOVERY = FAREBOX_RECOVERY
		self.DATE_STORED = DATE_STORED
		self.PCNAME = PCNAME
		self.SIGN_ON_DATE = SIGN_ON_DATE
		self.OPERATING_COST_PER_HOUR = OPERATING_COST_PER_HOUR
		self.RECOVERY_PROCESSING_ID = RECOVERY_PROCESSING_ID
		self.AGGREGATE_ID = AGGREGATE_ID
		self.COUNTY = COUNTY
		self.TYPE = TYPE

	def __repr__(self):
		return '<Output %r>' % self.ID