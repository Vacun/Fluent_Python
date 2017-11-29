l = [10, 20, 30, 40, 50, 60]

l[:2]

s = 'bicycle'

s[::3]

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

SKU = slice(0, 6)
Description = slice(6, 40)
unit_price = slice(40, 52)
quantity = slice(52, 55)
total_price = slice(55, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print('***   ',item[Description], item[total_price])


# Assigning to slices

l = list(range(10))