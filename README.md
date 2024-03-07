# algo_labs
## lab2
### Варіант 3
#### Рівень 2
Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.

Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.

Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.

Напишвть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н годин, поки повернеться охорона.

Приклад 1: piles = [3,6,7,11], H = 8
Результат: 4

Приклад 2: piles = [30,11,23,4,20], H = 5
Результат: 30

Приклад 3: piles = [30,11,23,4,20], H = 6
Результат: 23

Важливо: 1 <= piles.length <= 10^4 piles.length <= H <= 10^9 1 <= piles[i] <= 10^9
