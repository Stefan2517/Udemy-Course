'''
user_prompt = "Introdu activitatile:"
text = input(user_prompt) # ce e scris in user_prompt se salveaza in variabila text
print(text) # afisam variabila text
'''

################

'''
user_prompt = "Introdu activitatile:"
activitate1 = input(user_prompt)
activitate2 = input(user_prompt)
activitate3 = input(user_prompt)

activitati = [activitate1, activitate2, activitate3, "Hello"]
print(activitati)

print(type(activitate1))
'''

################

'''
user_prompt = "Introdu activitatile:"
while 2>1: # 2>1 este intotdeauna valabil, deci poate fi inlocuita conditia cu True,
    # daca pun False nu executa comenzile
    activitate = input(user_prompt)
    print(activitate)
    print("Urmatoarea...")
'''

################

'''
user_prompt = "Introdu activitatile:"

activitati = []

while True:
    activitate = input(user_prompt)
    #activitate.append()  o sa dea eroare deoarece activitate e string nu lista
    print(activitate.capitalize()) # capitalize returneaza stringul ca avand majuscula prima litera
    activitati.append(activitate)
    print(activitati)
    print(activitate.title()) # title returneaza stringul ca fiecare cuvant sa fie cu majuscula

'''

################  BONUS

'''
parola = input("Introdu parola:")

while parola != "pass123":
    parola = input("Introdu parola:")

print("Parola e corecta!")
'''

################  BONUS

'''
x = 1

while x <= 6:
    print(x)
    x = x + 1
'''

# pentru a afla metodele in consola scriu de exemplu pt STRING: dir('str'), sau dir('oricelitere'), dir(int)
# tot in consola ca sa aflu cum functioneaza metodele: help(list.append), sau help([]) sau help(list),
# sau a = [1, 2, 3]
# dir(a)
# cand cauti append sau capitalize, ultimul nu are argument, primul are. Asa stii unde se cere...  ??????
# adica: append(self, object, /),  ?????????
# sau pentru functii: import builtins
# help(builtins)