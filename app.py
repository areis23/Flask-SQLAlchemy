from flask import Flask, render_template, request
from demoFlask import db
db.create_all()
from demoFlask import Output
import csv
from sqlalchemy.sql import func

with open('Temp2.db', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	for row in fb_reader:
		db.session.add(Output(row['ID'], row['LINE_NUMBER'], row['ZONE_NUMBER'], \
			row['TIME_RANGE'], row['DIRECTION'], row['SCHEDULED_RUN_TIME'], \
			row['TOTAL_OPERATING_COST'], row['FARE_COLLECTED'], \
			row['FAREBOX_RECOVERY'], row['DATE_STORED'], row['PCNAME'], \
			row['SIGN_ON_DATE'], row['OPERATING_COST_PER_HOUR'], \
			row['RECOVERY_PROCESSING_ID'], row['AGGREGATE_ID'], row['COUNTY'], \
			row['TYPE']))
db.session.commit()

my_query = db.session.query(func.sum(Output.FARE_COLLECTED)).filter_by(LINE_NUMBER = 1)
for result in my_query:
	line_sum = result[0]

app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/chart', methods=['POST'])
def chart():
	line = int(request.form['line'])
	#line_sum = db.session.query(func.sum(Output.FARE_COLLECTED)).filter_by(LINE_NUMBER = line)
	return render_template('chart.html', line= line, line_sum = line_sum)


"""
if __name__ == '__main__': # if called from command line  
  main()                   # run main()
"""