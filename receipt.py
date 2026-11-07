item1_name = 'Notebook'
item1_price= '4.99'
item1_qty = '2'

item2_name = 'Pen Pack'
item2_price = '7.50'
item2_qty = '1'

item3_name = 'Backpack'
item3_price = '34.99'
item3_qty = '1'

tax_rate = '0.075'            #7.5% sales tax

item1_price = float(item1_price)
item1_qty = int(item1_qty)

item2_price = float(item2_price)
item2_qty = int(item2_qty)

item3_price = float(item3_price)
item3_qty = int(item3_qty)

tax_rate = float(tax_rate)

subtotal1 = item1_price * item1_qty
subtotal2 = item2_price * item2_qty
subtotal3 = item3_price * item3_qty
subtotal = subtotal1 + subtotal2 + subtotal3
tax = subtotal * tax_rate
total = subtotal + tax

print('='*40)
print('\tSTORE RECEIPT')
print('='*40)
print(f'Notebook\t${item1_price}*{item1_qty} \t${subtotal1}')
print(f'Pen Pack\t${item2_price}*{item2_qty}  \t${subtotal2}')
print(f'Backpack\t${item3_price}*{item3_qty} \t${subtotal3}')
print('-'*40)
print(f'Subtotal:\t \t \t${subtotal}')
print(f'Tax (7.5%):\t \t \t${tax:.2f}')
print('='*40)
print(f'TOTAL:\t \t \t \t${total:.2f}')
print('='*40)
