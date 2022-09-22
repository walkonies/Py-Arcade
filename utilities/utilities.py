import time
import pandas as pd

def readCSV(file):
	'''
	Read CSV file and return data frame
	'''
	df = pd.read_csv(file)
	return df

def saveDataFrame(path, df):
	data = df.to_csv()
	with open(path, 'w') as f:
		write(f, data)

def makeTxt(data, path=None):
	'''
	List -> .txt
	'''
	if path is None:
		path = f'{dir_path}/{getTime()}.txt'
	with open (path, 'w') as f:
		write(f,data)
	return path

def log(path, data):
	'''
	Append data to .txt given path
	'''
	with open(path, 'a')as f:
		write(f,data)

def write(f, data):
	'''
	Write data to open file
	'''
	if type(data) == str or type(data) == int:
		f.write(str(data))
		f.write('\n')
	else:
		for elem in data:
			f.write(str(elem))
			f.write('\n')

def getDate():
	return time.strftime("%m/%d/%Y")
def getTime():
	'''
	Current time year-month-day-hour-minute -> str
	'''
	return time.strftime("%Y_%m_%d_%H:%M", time.localtime())
