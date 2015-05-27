# 20140102 110100; 1837.75;  1838;  1834.25;  1834.75; 9890
# date      time   open      high    low      close    volume    

def compare(candle_close_0, candle_close_1):
	if candle_close_1:
		# print(float(candle_close_0[4]), float(candle_close_1[4]))
		if float(candle_close_0[4]) > float(candle_close_1[4]):
			print("I am buying at {}".format(candle_close_0[4]))
		elif float(candle_close_0[4]) == float(candle_close_1[4]):
			print("====Waiting===")
		else:
			print("I am selling at {}".format(candle_close_1[4]))

def read_candle_file(filename):
	with open(filename) as f:
		candle_close_0 = f.readline()[:-1].split(';')
		# compare(candle_close_0, candle_close_1)
		while True:
			candle_close_1 = candle_close_0
			candle_close_0 = f.readline()[:-1].split(';')
			if not candle_close_0[0]:
				break
			print(candle_close_0)
			compare(candle_close_0, candle_close_1)

		# for line in f:
		# 	candle_close_0 = line[:-1].split(';')[4]
		# 	compare(candle_close_0, candle_close_1)
		# 	candle_close_1 = candle_close_0

read_candle_file('ES 03-14.Last-test.txt')