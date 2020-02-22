
prod_list = []

while True:
	name = input("請輸入商品名稱")

	if name == "q":
		break

	price = input("請輸入商品價格")

	each_P = [name,price]

	#each_P.append(name)
	#each_P.append(price)

	prod_list.append(each_P)

print(prod_list)

#print(prod_list[0][0])