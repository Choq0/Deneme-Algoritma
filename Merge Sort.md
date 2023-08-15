[16,21,11,8,12,22] -> Merge Sort 

[16,21,11] - [8,12,22]

[16,21] - [11] - [8,12] - [22]

[16] - [21] - [11] - [8] - [12] -[22] 

[16,21] - [8,11] - [12,22]

[8,11,16,21] - [12,22]

[8,11,12,16,21,22] 

Insertion sort'da, time complexity n2 olduğundan ötürü çalışma zamanımız artıyordu. Merge sort'da ise nlogn olduğu için açık ara performans olarak daha iyi diyebiliriz.

