#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-


'''
Generate my supersecret key
v.2
ACAB
poo poo won't get my secrets
'''

import hashlib

def append_to_keyarr(val, arrname):
	arrname.append(val+len(arrname))


def get_sub_key(foofile):
	sumarr = 0
	for i in range(1, len(foofile)):
		sumarr += foofile[i]
	foofile.append(sumarr)
	hasher = hashlib.md5(str(foofile).encode('utf-8'))
	hashvalue = hasher.hexdigest()
	#print(hashvalue)
	del foofile[-1]
	return hashvalue

def get_main_key(foofile, hashval):
	hasher = hashlib.md5(str(foofile).encode('utf-8'))
	hashervalue = hasher.hexdigest()
	foofile.append(hashervalue)
	sechasher = hashlib.md5(str(foofile).encode('utf-8'))
	sechasherval = sechasher.hexdigest()

	if sechasherval == hashval:
		the_secret_key = []
		for i in keyarr1:
			the_secret_key.append(i)
		for i in keyarr2:
			the_secret_key.append(i)
		for i in keyarr3:
			the_secret_key.append(i)
		for i in keyarr4:
			the_secret_key.append(i)
		print('Congratulations, you have found my key:', ''.join(map(chr, the_secret_key)))
	else:
		print('This is not my secret key')

#This is bad, takes for ever!!
def bruteforcer():
	arr = [110,100,110,98,105,88,107,103,102,96,101,100,88,116,98,93,94,94,106]
	outputarr = {}

	brutesum = 0
	#brutehash
	for i in range(1, len(arr)):
		brutesum += keyarr[i]
	for o in range(0, 19):
		ordF = str(o)
		outputarr[ordF] = []
	for i in arr:
		#outputarr.append(i)
		for s in range(0,19):
			#outputarr[o] = []
			#print(s)
			#outputarr[str(s)].append(chr(i+s)) #str(i)+'+'+str(s)+':'+
			isascii = i+s
			if isascii < 128:
				#print('valid ascii: ', isascii)
				outputarr[str(s)].append(isascii)
			#else:
			#	print('not valid: ', isascii)

	with open('./tmpout.txt', 'a') as bruteout:
		print(outputarr)
		for n in range(0, 19):
			#bla = 0
			nval = outputarr[str(n)][n]
			for n0 in range(0, len(outputarr[str(n+1)])): #outputarr[str(n)]:
				print(nval)
				print(n0)

				#n0val = outputarr[str(n)][n], outputarr[str(n + 1)][n0], outputarr[str(n + 2)][n1],outputarr[str(n + 2)][n2],outputarr[str(n + 2)][n3],outputarr[str(n + 2)][n4]  #, outputarr[str(n + 2)][o]

				for n1 in range(0, len(outputarr[str(n+2)])): #outputarr[str(n+1)]:
					#print(n0val)
					for n2 in range(0, len(outputarr[str(n+3)])): #outputarr[str(n+2)]:
						for n3 in range(0, len(outputarr[str(n+4)])): #outputarr[str(n+3)]:
							for n4 in range(0, len(outputarr[str(n+5)])): #outputarr[str(n+4)]:
								for n5 in range(0, len(outputarr[str(n+6)])):
									for n6 in range(0, len(outputarr[str(n+7)])):
										for n7 in range(0, len(outputarr[str(n+8)])):
											for n8 in range(0, len(outputarr[str(n+9)])):
												for n9 in range(0, len(outputarr[str(n+10)])):
													for n10 in range(0, len(outputarr[str(n+11)])):
														for n11 in range(0, len(outputarr[str(n+12)])):
															for n12 in range(0, len(outputarr[str(n+13)])):
																for n13 in range(0, len(outputarr[str(n+14)])):
																	for n14 in range(0, len(outputarr[str(n+15)])):
																		for n15 in range(0, len(outputarr[str(n+16)])):
																			for n16 in range(0, len(outputarr[str(n+17)])):
																				for n17 in range(0, len(outputarr[str(n+18)])):
																					pass
																					#print(len(outputarr[str(n+17)]))

																					brutearr = [outputarr[str(n)][n], \
																							outputarr[str(n + 1)][n0], \
																							outputarr[str(n + 2)][n1], \
																							outputarr[str(n + 3)][n2], \
																							outputarr[str(n + 4)][n3], \
																							outputarr[str(n + 5)][n4], \
																							outputarr[str(n + 6)][n5], \
																							outputarr[str(n + 7)][n6], \
																							outputarr[str(n + 8)][n7], \
																							outputarr[str(n + 9)][n8], \
																							outputarr[str(n + 10)][n9], \
																							outputarr[str(n + 11)][n10], \
																							outputarr[str(n + 12)][n11], \
																							outputarr[str(n + 13)][n12], \
																							outputarr[str(n + 14)][n13], \
																							outputarr[str(n + 15)][n14], \
																							outputarr[str(n + 16)][n15], \
																							outputarr[str(n + 17)][n16], \
																							outputarr[str(n + 18)][n17], brutesum]
																					#brutearr = []
																					#brutearr.append(n0val)
																					#print(brutearr)
																					hasher = hashlib.md5(
																						str(brutearr).encode('utf-8'))
																					if hasher.hexdigest() == '733dadb42ba64831e0aad8fd6d51188c':
																						del brutearr[-1]
																						print('You have found my key:',
																						  ''.join(map(chr, brutearr)))
																					else:
																						del brutearr[-1]
																						#print(''.join(map(chr, brutearr)),
																						#	  ' Oh no, this is not my key!')

																					#print(n0val)





								#pass
								#print('done')

			#for m in outputarr:
				#print(n,m,bla)
				#bruteout.write(outputarr[str(n)][bla])
			#	bla += 1

				#bruteout.write(outputarr[str(m)][bla])

			#bruteout.write('\n')
				#print('Value: ',n , m, outputarr[str(n)][bla])


keyarr1 = []
keyarr2 = []
keyarr3 = []
keyarr4 = []
keyarr5 = []

secrethash = 'd050d6ef5c5685336d467af6d6406fee'

# Oh no, i need to sort these in correct order...

append_to_keyarr(110, keyarr1)
append_to_keyarr(110, keyarr1)
append_to_keyarr(100, keyarr1)
append_to_keyarr(116, keyarr1)
append_to_keyarr(98, keyarr1)


append_to_keyarr(103, keyarr2)
append_to_keyarr(93, keyarr2)
append_to_keyarr(110, keyarr2)
append_to_keyarr(108, keyarr2)
append_to_keyarr(107, keyarr2)


append_to_keyarr(103,keyarr3)
append_to_keyarr(117,keyarr3)
append_to_keyarr(104,keyarr3)
append_to_keyarr(116,keyarr3)
append_to_keyarr(98,keyarr3)


append_to_keyarr(111,keyarr4)
append_to_keyarr(29,keyarr4)
append_to_keyarr(116,keyarr4)
append_to_keyarr(115,keyarr4)
append_to_keyarr(109,keyarr4)


key1 = get_sub_key(keyarr1)
key2 = get_sub_key(keyarr2)
key3 = get_sub_key(keyarr3)
key4 = get_sub_key(keyarr4)

keyarr6 = [key1, key2, key3, key4]


get_main_key(keyarr6, secrethash)
