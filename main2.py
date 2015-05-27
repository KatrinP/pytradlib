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

def read_candle_file():
		for line in open("ES 03-14.Last-test.txt"):
			yield line

# f = read_candle_file()
# f.next()
