import random
cFactorValue = 10 # from 100
with open('input.txt', 'r') as file:
	string = file.read()
string=string.lower() # We and we have no diffrence.
hashmap={}
arr = string.split(" ")
for i in range(len(arr)):
    if arr[i][-1] == '\n':
        arr[i] = arr[i][:-1]
for i in range(len(arr)-1):
	if(arr[i] not in hashmap):
		hashmap[arr[i]] =  {}
	if(arr[i+1]  not in hashmap[arr[i]]):
		hashmap[arr[i]][arr[i+1]] = 1
	else:
	    hashmap[arr[i]][arr[i+1]] += 1	

newstr = random.choices(arr)[0] # start with a random choice
words = 1
while (words<200): # could be upto 400
	curr = newstr.split(" ")[-1]
	creativeFactor = random.randint(1,100)
	if creativeFactor > (100-cFactorValue):
	    newstr += " " + random.choices(arr)[0]
	    words += 1
	    continue
	sum = 0
	for key in hashmap[curr]:
		sum += hashmap[curr][key]
	probDict = {} # dictionary of probability 
	for key in hashmap[curr]:
		probDict[key] = hashmap[curr][key] / sum
	keys = []
	values = []
	for key in hashmap[curr]: 
		keys.append(key)
		values.append(hashmap[curr][key])	
	choice = random.choices(keys, values, k=1)[0] # choice based on weight
	newstr+=" "+choice
	words+=1
print(newstr)

