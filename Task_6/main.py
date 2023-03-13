"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. 
билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no"""

tiket_number = int(input('Введите номер билета: '))
if tiket_number<100000 or tiket_number>999999:
    print('Введен некорректный номер')
else:
    first_part = tiket_number//1000
    second_part = tiket_number%1000
    if {first_part%10 + int(first_part/10%10) + first_part//100} == {second_part%10 + int(second_part/10%10) + second_part//100}:
        print('Билет счастливый')
    else:
        print('Билет несчастливый')