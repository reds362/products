import os

#讀取檔案
def read_file(filename):
	products = []
	
	with open(filename,'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)
	return products


	

#使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name,price])
	print(products)


#購買清單
def print_data(products):
	for p in products:
		print(p[0] , '的價格為' , p[1])


#寫入檔案
def write_file(filename , products):
	with open(filename,'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] +"," +p[1]+'\n')



def main():
	filename = 'product.csv'
	if os.path.isfile(filename):#檢查檔案是否在不在
		print('找到了檔案!!')

		products = read_file(filename)
		print_data(products)
		user_input(products)
		
		write_file(filename , products)

	else:
		print('找不到檔案!!')

main()
