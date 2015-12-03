import json
s=["@","*","*","*","*","*","*","*","*","*","*","*"]
dict=json.load(open("dict.json"))
num="""         1          
   2           5
      3     4
         6      
      8     9
   7           10
         11"""
dict["def"]=dict["def"]+[raw_input("translation> ")]
while 1:
	print("          "+s[1]+"           ")
	print("    "+s[2]+"          "+s[5]+"      ")
	print("       "+s[3]+"     "+s[4]+"        ")
	print("          "+s[6]+"           ")
	print("       "+s[8]+"     "+s[9]+"        ")
	print("    "+s[7]+"           "+s[10]+"     ")
	print("          "+s[11]+"           ")
	print("Type `?' for numbering help.\nType `exit' to exit.")
	id=raw_input("choice> ")
	if id=="exit":break
	try:
		if int(id)<1 or int(id)>11:raise ValueError
		if s[int(id)]=="*": s[int(id)]="X"
	        else:s[int(id)]="*"
	except:print("Only the following inputs are accepted:\n"+num)
iter=0
toleds=[]
for i in s:
	if i=="X":toleds.append(iter)
	iter=iter+1
dict["leds"].append(toleds)
print("Output will look like this:\n"+json.dumps(dict))
if raw_input("Do you want to write-out it?> ").upper()=="Y":json.dump(dict,open("dict.json","w"))
