import pandas as pd

log_path = './logs/'

def log(message):
	print(f"[{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}] "+ message)
	date = pd.Timestamp.now().strftime('%Y-%m-%d')
	with open(log_path+date+'_log.txt', 'a') as f:
		f.write(f"[{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}] "+ message + '\n')