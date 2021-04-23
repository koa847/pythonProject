tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Егор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tu_kl_tuple = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(0, len(tutors)))


for tu_kl in tu_kl_tuple:
    print(tu_kl)
