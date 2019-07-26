import random
import string
def short(size=3, char=(string.ascii_letters + string.digits)):
	x = input('Enter a website URL to be shortened: ')
	x = ''.join([random.choice(char) for n in range(size)]) + '.abc'
	return x
url = short()
print(url)

j = 0
countries = ['Italy', 'Italy', 'Italy', 'USA', 'Australia', 'Italy', 'Japan', 'Mexico', 'Canada', 'Italy']
for i in countries:
	if i == 'Italy':
		j += 1
print(f'There are {j} instances of Italy in this list.')
comp_list = [random.randint(1,99) for k in range(20)]
print(comp_list)