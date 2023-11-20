print(''' 
Menu:
1 - kurslarni ko'rish
2 - kurs qushish
3 - kursni o'zgartirish
4 - kursni uchirish
5 - chiqish
''')

kurslar = {
    "Python":['15:30','300000']
}

check_action = input("kamanda kiriting: ")


def add_course(kurs_nomi,kurs_vaqti,kurs_narxi):
    if kurs_nomi not in kurslar:
        kurs_value = [kurs_vaqti, kurs_narxi]
        kurslar[kurs_nomi.capitalize()] = kurs_value
        print('Kurs qoshildi')
    else:
        print('Unaqa kurs bor!')


def update_course(kurs_nomi,kurs_vaqti,kurs_narxi):
    if kurs_nomi not in kurslar:
        kurs_value = [kurs_vaqti, kurs_narxi]
        kurslar[kurs_nomi.capitalize()] = kurs_value
    else:
        print('Bunday kurs mavjud emas!!!')

def remove_course(kurs_nomi):
    if kurs_nomi.capitalize() in kurslar:
        kurslar.pop(kurs_nomi.capitalize())
    else:
        print('Bunday kurs mavjud emas!!!')


while True: # kod ishlashi uchun False ni True ga o'zgartiring 

    if check_action == '1':
        print(kurslar)
    elif check_action == '2':

        kurs_nomi = input('Kurs nomini kiriting: ')
        kurs_vaqti = input('Kurs vatini kiriting: ')
        kurs_narxi = input('Kurs narxini kiriting: ')

        add_course(kurs_nomi,kurs_vaqti,kurs_narxi)
    elif check_action == '3':

        kurs_nomi = input('Kurs nomini kiriting: ')
        kurs_vaqti = input('Kurs vatini kiriting: ')
        kurs_narxi = input('Kurs narxini kiriting: ')

        update_course(kurs_nomi,kurs_vaqti,kurs_narxi)
    elif check_action=='4':

        kurs_nomi = input('Kurs nomini kiriting: ')
        
       

        remove_course(kurs_nomi)
    elif check_action =='5':
        print('Tizimdan chiqdingiz!!')
        break

    else:
        print('unaqa kamanda yoq')

    check_action = input("kamanda kiriting: ")