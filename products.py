products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name,price]
	products.append(p)
print(products)
print(products[0][0])	
print(products[0][1])
print(products[1][0])
print(products[1][1])

for p in products:
	print(p[0] , '的價格為' , p[1])


with open('product.txt','w') as f:
	for p in products:
		print(p)
		#f.write(p) #type Error not list 
		f.write(p[0] +"," +p[1]+"\n")