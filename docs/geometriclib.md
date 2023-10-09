# geometric_lib

## Описание

С помощью фукций данной библиотеки по введённым параметрам пользователь может получить значения площади и периметра прямоугольника/треугольника/квадрата/круга/треугольника.

## Функции

### ▭ Прямоугольник - rectangle.ру

area(side length **a**, side length **b**) = **ab**
perimeter(side length **a**, side length **b**) = **2**(**a + b**)

~~~python
S = area(2, 3) #S = 6
P = perimeter(2, 3) #P = 10
~~~

### △ Треугольник - triangle.ру

area(side length **a**, height length **h~a~**) = **0.5**(**ah~a~**)
perimeter(side length **a**, side length **b**, side length **c**) = **a** + **b** + **c**

~~~python
S = area(4, 3) #S = 6
P = perimeter(4, 3, 5) #P = 12
~~~

### ❒ Квадрат - square.ру

area(side length **a**) = **a^2^**
perimeter(side length A) = **4a**

~~~python
S = area(5) #S = 25
P = perimeter(5) #P = 20
~~~

### ◯ Круг - circle.ру

area(radius R) = **πR^2^**
perimeter(radius R) = **2πR**

~~~python
S = area(10) #S = 314.1592653589793
P = perimeter(10) #P = 62.83185307179586
~~~

## История изменений

|Commit |Author |Date |Message |
|:------|:------|:----|:-------|
|64357d|409416 <prohinmihail@mail.ru>|Sat Oct 7 13:40:35 2023 +0300|added descriptions with examples|
|8a2ce9|409416 <prohinmihail@mail.ru>|Sat Sep 23 12:25:49 2023 +0300|added triangle.py and fixed rectangle.py|
|f65a8a|409416 <prohinmihail@mail.ru>|Sat Sep 23 12:24:04 2023 +0300|added rectangle.py|
|d078c8|smartiqa <info@smartiqa.ru>|Thu Mar 4 14:55:29 2021 +0300|L-03: Docs added|
|8ba9ae|smartiqa <info@smartiqa.ru>|Thu Mar 4 14:54:08 2021 +0300|L-03: Circle and square added
