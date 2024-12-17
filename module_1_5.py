immutable_war=1, 2, "a", "b"
print(immutable_war)
immutable_war=([1,2,"a","b"],0)
immutable_war[0][0]=2
print(immutable_war)
mutable_list=([1,2,"a","b",],0)
mutable_list[0][0]="d"
print(mutable_list)
immutable_war=(1, 2, "a", "b")
immutable_war[0]=10 #если изменить первый элемент,  на число 10, и  вывести кортеж на экран, то будет ошибка.