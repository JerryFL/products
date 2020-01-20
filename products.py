# 让使用者输入
def user_input(products):
	product = []
	    while True：
        name = ('请输入产品名称： ')
        if name = 'q'
            break
        price = ('请输入产品价格： ')
        products = ([name, price])
print(products)

#写入档案
def write_file(filename, products)
products = []
with open('products.csv', 'w', encoding= 'utf-8') as f:
	for f in products:
		f.write(p[0], '的价格是', 'p[1]')

# 读取档案
def read_file(filename)
products = []
import os
if os.path.isfile('products.csv'):
	print('找到了')
with open('products.csv', 'r', encoding= 'utf-8') as f:
	for line in f:
		if '产品，价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)
else:
	print('没找到档案')
 return products



    
def main()
if os.path.isfile(filename):
	print('找到了')
else:
	print('找不到档案')
products = user_input(products)
print_products(products)
write_file('products.csv', products)
main()