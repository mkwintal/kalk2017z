def dodawanie (a, b):
	wynik = a + b 
	return wynik
def get_info() :
		print('to jest prosty kalkulator')

get_info()
print ('Wprowadz pierwsza liczbe')
z1 = int(input())
print ('Wprowadz druga liczbe')
z2 = int(input())
print(dodawanie(z1, z2))