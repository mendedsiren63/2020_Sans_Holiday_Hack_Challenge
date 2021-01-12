#!/usr/bin/python3
import os
main_nonce="nonce"
obj_file_new_nonce="obj_new_nonce_624"
cmd_cut='cat nonce | tail -312 > obj_nonce_312'
nonce_combined_list=[]

def split_nonce():

	os.system(cmd_cut)	#This block will cut 312 nonce from main file and put in last nonce_312 
	file_nonce="obj_nonce_312"

	with open(file_nonce, "r") as file:		# Calculate hi and lo 32 bit of 64 bit nonce.
		for line in file.readlines():
			line=int(line)
			highint = line >> 32       #hi 			
			lowint = line & 0xffffffff #lo
			
			with open (obj_file_new_nonce, 'a') as file: 	#Add nonces to a new file making it 624 values. 
				file.write(str(lowint)+'\n')
			
			with open(obj_file_new_nonce, 'a') as file:
				file.write(str(highint)+'\n')


def predict():
	try:
		os.system('cat obj_new_nonce_624 | mt19937predict | head -20 > obj_pred_10.txt') # Using Kmyk's Mersenne twister Predictor
	except Exception as e:									# This will through a broken pipe exception but it will successfully predict 10 next nonces
		pass

	with open('obj_pred_10.txt', 'r') as file:
		nonce_array = file.readlines()
		for i,j in zip(range(0,len(nonce_array),2), range(129997,130007)):
#				if i <len(nonce_array)-1:
				nonce_lo=int(nonce_array[i])				# Converting back to 64 bit.
				nonce_hi=int(nonce_array[i+1])
				nonce_combined=(nonce_hi <<32) + nonce_lo
				hex_nonce=hex(nonce_combined)
				print("Predicted nonce at",j,"is:", nonce_combined, " [ Hex value:",hex_nonce,"]")  #Printing the nones and their hex value

split_nonce()
predict()






