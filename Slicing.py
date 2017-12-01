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
    print('***   ', item[Description], item[total_price])


# Assigning to slices

l = list(range(10))

# for mutiable sequances we can graft,excise or otherwise modify slices in place

l[2:5] = [20, 30]  # here we graft: replacing 3 elements of the list by 2 new ones

# deleteing in place can be done as follows

del l[5:7]

# OR del(l[5:7])
l[3::2] = [11, 22]  # needs to be the same element count

# when the target of assignment is a slice, then right-hand side must be an iterable

l[2:5] = [100]  # even if it is just one item. here we excise.


# Using + and * with sequences
