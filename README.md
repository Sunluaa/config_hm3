Вариант 2

Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.
Входной текст на учебном конфигурационном языке принимается из
стандартного ввода. Выходной текст на языке xml попадает в файл, путь к
которому задан ключом командной строки.
Однострочные комментарии:
:: Это однострочный комментарий
Многострочные комментарии:
{-
Это многострочный
комментарий
-}
Массивы:
list( значение, значение, значение, ... )
Словари:
table([
 имя = значение,
 имя = значение,
 имя = значение,
 ...
])
11
Имена:
[_a-zA-Z][_a-zA-Z0-9]*
Значения:
• Числа.
• Массивы.
• Словари.
Объявление константы на этапе трансляции:
set имя = значение;
Вычисление константы на этапе трансляции:
|имя|
Результатом вычисления константного выражения является значение.
Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3
примера описания конфигураций из разных предметных областей.


Стек технологий
Python 3: Используется как основной язык программирования для обработки конфигурационного языка и генерации XML-файла.
argparse: Для обработки аргументов командной строки (задание входного файла и выходного пути).
unittest: Для тестирования всех компонентов и функциональности инструмента.
xml.etree.ElementTree: Для создания XML-документов.
Описание функционала
Преобразование текста:

Трансляция текста из учебного конфигурационного языка в формат XML.
Поддержка всех конструкций конфигурационного языка, включая комментарии, массивы и словари.
Обработка вложенных конструкций:

Рекурсивная обработка вложенных массивов и словарей.
Выявление ошибок:

Проверка синтаксической корректности входного текста.
Сообщения об ошибках выводятся в стандартный поток ошибок.
Комментарии:

Поддержка однострочных комментариев (:: ...).
Поддержка многострочных комментариев ({- ... -}).
Константы:

Объявление констант на этапе трансляции с использованием синтаксиса set имя = значение;.
Вычисление значения констант с помощью конструкции |имя|.
Аргументы командной строки:

--output: Указание пути для сохранения выходного XML-файла.
Реализация
Парсинг конфигурационного языка:

Реализована функция parse_configuration, которая считывает входной текст, извлекает массивы, словари, значения и их имена.
Регулярные выражения используются для валидации имен и синтаксиса.
Генерация XML:

Преобразование данных в формат XML с помощью функции generate_xml, которая поддерживает вложенные массивы и словари.
Комментарии преобразуются в элементы XML (<comment>), а константы добавляются как атрибуты или элементы.
Обработка ошибок:

Включены проверки для:
Отсутствия обязательных конструкций.
Некорректных имен.
Неподдерживаемых значений.
Все ошибки сопровождаются информативными сообщениями.
Тестирование
Тестирование функционала проведено успешно:
![изображение](https://github.com/user-attachments/assets/f97c96f1-a725-4b61-9a47-f7cb988fc7ba)
![изображение](https://github.com/user-attachments/assets/803e1690-987e-4f4c-928f-285d0111d8b8)

Проведены три теста предметной области

Проверены сценарии с корректным и некорректным входным текстом.
Все конструкции конфигурационного языка покрыты тестами, включая:
Однострочные и многострочные комментарии.
Массивы и словари.
Константы и их вычисления.

задания:
1
![изображение](https://github.com/user-attachments/assets/f4599569-b0f7-4548-8e31-7a6c6333078c)
![изображение](https://github.com/user-attachments/assets/0f1a4b85-7d1f-4f34-b0f5-b32e7df0fdb1)

2
![изображение](https://github.com/user-attachments/assets/1187e4d8-9d92-4310-bf35-f921514d9572)
![изображение](https://github.com/user-attachments/assets/3b6376e0-a546-41e6-a0bf-3c75a56ab92b)

3
![изображение](https://github.com/user-attachments/assets/cd883077-71a5-447b-9b32-9d6f9c9e7c5d)
![изображение](https://github.com/user-attachments/assets/1b5d6e63-107b-48a8-a405-efc33c94abb4)

4
![Uploading изображение.png…]()





