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


elif x == "sip":
	
