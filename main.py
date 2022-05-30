import random
list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

list3 = ['1','2','3','4','5','6','7','8','9','0']

list4 = ['0','9','8','7','6','5','4','3','2','1']

list5 = ['/','*','@','$','!','^','&','(',')','#']
K = '#'
D = '#'
for _ in range(10):
    K+=list1[random.randint(0,25)]
    K+=list3[random.randint(0,9)]
    K+=list5[random.randint(0,9)]
    K+=list4[random.randint(0,9)]
    K+=list2[random.randint(0,25)]
    D+=list1[random.randint(0,25)]
    D+=list3[random.randint(0,9)]
    D+=list5[random.randint(0,9)]
    D+=list4[random.randint(0,9)]
    D+=list2[random.randint(0,25)]
code =''''''
print(K)
print(code)
print(D)
