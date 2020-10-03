def hundreds(number_str, count):
	Units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	Tens = ["","Teens","Twenty","Thirty","Fourty","Fithty","Sixty","Seventy","Eighty","Ninety"]
	Teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fithteen","Sixteen","Seventeen","Eighteen","Nineteen"]
	big = ["Thousand,", "Million,", "Billion,", "Trillion,", "Quadrillion,", "Quintillion,", "Sextillion,", "Septillion,", "Octillion,", "Nonillion,", "Decillion,"]
	
	output_string = ""

	u= Units[int(number_str[len(number_str)-1])]
	u_ind = int(number_str[len(number_str)-1])
	number_str = number_str[:len(number_str)-1]
	
	output_string = u
	
	if(number_str==""):
		return output_string

	t = Tens[int(number_str[len(number_str)-1])]
	number_str = number_str[:len(number_str)-1]
	
	if(t!=""):
		if(u!="Zero"):
			output_string = t + " " + output_string
		else:
			output_string = t
	if(t=="Teens"):
		output_string = Teens[u_ind]
	
	if(number_str==""):
		return output_string
	
	h = Units[int(number_str[len(number_str)-1])]
	number_str = number_str[:len(number_str)-1]
	
	if(h!=""):
		if(output_string!=""):
			output_string = " and " + output_string
		output_string = h + " Hundred" + output_string
	
	if(number_str!=""):
		#There is more!
		thousands = hundreds(number_str, count + 1)
		
		if(output_string.find("and") == -1 and output_string!="" and count == 0):
			output_string = "and " + output_string
			
		if(thousands[len(thousands)-5:] == "ion, "):
			output_string = thousands  + output_string
		else:
			output_string = thousands + " " + big[count]+ " " + output_string
		
	#Remove trailing spaces
	if (count == 0):
		if (output_string[len(output_string)-1] == " "):
			output_string = output_string[:len(output_string)-1]
	
	#Remove trailing commas
	if (count == 0):
		if (output_string[len(output_string)-1] == ","):
			output_string = output_string[:len(output_string)-1]
	
	return output_string

def negative_str(neg):
	if(neg):
		return "Negative "
	else:
		return ""
		
def decimal(fraction):
	if(fraction == ""):
		return ""
	else:
		Units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
		out_str = ""
		for char in fraction:
			out_str += " " + Units[int(char)] 
		return " point" + out_str
	
def numb_to_text(number, mode=''):
	#Is Number Negative?
	neg = False
	if number < 0:
		neg = True

	number_str = str(number)

	#Trim '-' from number
	if neg:
		number_str = number_str[1:]
				
	#Is Number a Fraction?
	dec_point = number_str.find(".")
	fraction = ""
	if dec_point > -1:
		fraction = number_str[dec_point+1:]
		number_str = number_str[:dec_point]
	
	#Build up output string
	output_string = negative_str(neg) + hundreds(number_str, 0) + decimal(fraction)
	
	#Display mode
	if mode=="plain":
		return output_string
	elif mode=="pounds":
		output_string = hundreds(number_str, 0)
		if output_string == "One":
			output_string += " Pound"
		else:
			output_string += " Pounds"
		
		output_string = negative_str(neg) + output_string
		
		if fraction != "":
			if len(fraction) == 1:
				fraction += "0"
			output_string += " " + hundreds(fraction, 0) + " Pence"
		return output_string
	else:
		return str(number) + " = " + output_string

def index_of_list(list, search):
	matched_index = -1
	i = 0
	length = len(list)

	while i < length:
		if search == list[i]:
			matched_index = i
		i += 1
	
	return matched_index

def Classify_Units(word):
	Units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "naught"]
	index_units = index_of_list(Units,word) %10
	return index_units

def classify(word, current):
	Units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","eleven","twelve","thirteen","fourteen","fithteen","sixteen","seventeen","eighteen","nineteen"]
	Tens = ["twenty","thirty","fourty","fithty","sixty","seventy","eighty","ninety"]
	Other = ["and","hundred","negative","minus","point"]

	point = False
	output = 0

	index_units = index_of_list(Units,word)
	index_tens = index_of_list(Tens,word)
	index_other = index_of_list(Other,word)

	if index_units > -1:
		output = current + index_units
	elif index_tens > -1:
		index_tens = (index_tens+2)*10
		output = current + index_tens
	else:
		if index_other == 0 or index_other == 2 or index_other == 3:
			output = current
		elif index_other == 1:
			output = 100 * current
		elif index_other == 4:
			#point
			output = current
			point = True
		else:
			output = current
	
	return output, point


def text_to_numb(number_str, mode=''):

	number_str = number_str.lower()

	words = number_str.split(" ")

	sum = 0
	point = False
	neg = 1

	decimal_place = 0.1

	if (index_of_list(words,"negative") > -1):
		neg = -1
	if (index_of_list(words,"minus") > -1):
		neg = -1

	for w in words:
		if point == False:
			sum,point = classify(w, sum)
		else:
			sum += Classify_Units(w) * decimal_place
			decimal_place *= 0.1
	
	if sum == -1:
		return "Error: the number '" + number_str + "' was not converted to a valid number"
	elif mode=="plain":
		return sum * neg
	else:
		return number_str + " = " + str(sum * neg)

def main():
	print(numb_to_text(0))
	print(numb_to_text(10))
	print(numb_to_text(-110))
	print(numb_to_text(0.2))
	print(numb_to_text(-99999.02))


	print(text_to_numb("One"))
	print(text_to_numb("twO"))
	print(text_to_numb("Three"))
	print(text_to_numb("thirteen"))
	print(text_to_numb("FAILNUMBER"))
	print(text_to_numb("twenty"))
	print(text_to_numb("thirty three"))
	print(text_to_numb("fourty two"))
	print(text_to_numb("two hundred and fourty two"))
	print(text_to_numb("minus two hundred and fourty two"))
	print(text_to_numb("minus two hundred and fourty two point eight"))

	print(numb_to_text(3.012345, 'pounds'))

	print(hundreds("3", 0))
if __name__== "__main__":
	main()


