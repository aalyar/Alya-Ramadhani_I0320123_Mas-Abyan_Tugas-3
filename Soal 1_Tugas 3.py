list = ['Diva','Yuki', 'Rara', 'Salma','Ica','Aji', 'Rahmat', 'Zafira', 'Tsania', 'Rana']
print("teman di list ke-4 adalah : ", list[4])
print("teman di list ke-6 adalah : ", list[6])
print("teman di list ke-7 adalah : ", list[7])

list[3] = 'Wanda'
list[5] = 'Utsman'
list[9] = 'Rifqi'
print(list)

list.extend(['Maurich', 'Sekar'])
print(list)

for isi in list:
    print(isi)

print(len(list))
