# [22,27,16,2,18,6] -> Insertion Sort
a = [22,27,16,2,18,6]
a = sorted(a)
# Sıraladıktan sonra dizinimiz [2, 6, 16, 18, 22, 27] bu şekildedir.
# Worst Case durumu.

#[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.
b = [7,3,5,8,2,9,4,15,6]
# Adım 1 -> [2,3,5,8,7,9,4,15,6]
# Adım 2 -> [2,3,4,8,7,9,5,15,6]
# Adım 3 -> [2,3,4,5,7,9,8,15,6]
# Adım 4 -> [2,3,4,5,6,9,8,15,7]

b = sorted(b)
print(b)

# Selection Sorta göre bitmiş durum -> [2, 3, 4, 5, 6, 7, 8, 9, 15]
