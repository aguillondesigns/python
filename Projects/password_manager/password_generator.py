import random, os
clear = lambda: os.system('cls')
clear()
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_characters = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','?']
desired_lower_characters = input('How many lowercase letters?: ')
desired_upper_characters = input('How many uppercase letters?: ')
desired_numbers = input('How many numbers?: ')
desired_special_characters = input('How many special letters? [!, @ , #, etc...]: ')
clear()
random_lower = random.choices(lower_letters, k=int(desired_lower_characters))
random_upper = random.choices(upper_letters, k=int(desired_upper_characters))
random_numbers = random.choices(numbers, k=int(desired_numbers))
random_special = random.choices(special_characters, k=int(desired_special_characters))
split_password = random_special + random_numbers + random_upper + random_lower
mixed_password = random.sample(split_password, len(split_password))
merge_password = ''.join(map(str,mixed_password))
print(merge_password,'\n\nyour password is' ,len(merge_password), 'characters long.')