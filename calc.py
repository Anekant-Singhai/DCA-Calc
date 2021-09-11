print("what do you want me calculate senpai ;) ")


x = input()

if x == "%":
	print("selling price ,daddy: ")
	sp = float(input())
	print("cost price (not mine;): ")
	cp = float(input())
	print("and leverage senpai? ")
	n = float(input())
	print("profit is: ")
	pf = ((sp-cp)*100)/cp
	print(pf)
	print("leveraged profit is: ")
	print(pf*n)
	print("happy trading senpai...ara ara")

elif x == "avg":
	a = []
	b = []
	c = []
	sum = 0
	sum2 = 0
	print("ara ara ..what are the number of currencies you want me to calculate senpai")
	n1 = int(input())
	print("senpai ..now please put the no. of currrencies and price respectively like 25 currencies ay 20 dollar each then again")
	for _ in range(n1):
		a1 = float(input())
		a2 = float(input())
		a.append(a1)
		b.append(a2)
	for i in range(len(a)):
		c.append(a[i]*b[i])
		sum2 = sum2 + a[i]
	print(c)
	for p in range(len(c)):
		sum = sum+c[p]
		average = sum/len(c)
	avg_price = sum/sum2  #this is the avg price
	print("total invested amount is:/n" , sum)
	print("senpai the avg price is :",avg_price)
	print("happy trading senpai...and i'll be waiting at home ;)")


elif x == "dca":
	print("number of periods senpai:  ")
	t1 = int(input())
	e = []
	sum1 = 0
	print("senpai now i need the closing prices...and the D ofcourse but later;)")
	for _ in range(t1):
		d = float(input())
		e.append(d)
	for o in range(len(e)):
		e[o] = 1/e[o]
		sum1 = sum1 + e[o]
	print("the DCA senpai: " ,t1/sum1)
	print("happy trading onichan ...step onichan...")
	
