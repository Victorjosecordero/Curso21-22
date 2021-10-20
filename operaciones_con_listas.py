a = [8,2,1,4,9,6,9,9]
b = ['a','b','c']

total = min(a)
print('Total:', total)

a.append(9)
a.append(8)
print(a)

a.pop()
print(a)

#sort
a.sort(reverse=True)
print(a)


# extend
a.extend(b)
print(a)

#count


print(a.count(9))



#index

print('indice de c',a.index('c'))


#insert

a.insert(11,'nuevo')
print(a)


#remove

# a.remove(1)
# print(a)






#clear

a.clear()
print(a)
