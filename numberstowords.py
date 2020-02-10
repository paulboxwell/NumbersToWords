def hundreds(number_str, count):
	Units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	Tens = ["","Teens","Twenty","Thirty","Fourty","Fithty","Sixty","Seventy","Eighty","Ninety"]
	Teens = ["Ten","Eleven","Twelve","Therteen","Fourteen","Fithteen","Sixteen","Seventeen","Eighteen","Nineteen"]
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
		if(u!=""):
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
        neg = False
        if number < 0:
                neg = True

        number_str = str(number)

        if neg:
                number_str = number_str[1:]
        dec_point = number_str.find(".")
        fraction = ""
        if dec_point > -1:
                fraction = number_str[dec_point+1:]
                number_str = number_str[:dec_point]
                

        if mode=="plain":
                return negative_str(neg) + hundreds(number_str, 0) + decimal(fraction)
        else:
                return str(number) + " = " + negative_str(neg) + hundreds(number_str, 0) + decimal(fraction)


print(numb_to_text(0))
print(numb_to_text(10))
print(numb_to_text(-110))
print(numb_to_text(0.2))
print(numb_to_text(-99999.02))
