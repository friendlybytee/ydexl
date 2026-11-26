# Совет у Элронда

| Характеристика | Значение |
| --- | --- |
| **Категория** | Классная работа |
| **Макс. балл** | 15 |
| **Ограничение времени** | 1 секунда |
| **Ограничение памяти** | 64 Мб |
| **Ввод** | members.csv |
| **Вывод** | council.jsonlines |
| **ID задачи** | `95002` |

---

## Условие

На Совете собрались представители разных рас. В файле **members.csv** записана информация обо всех, присутствующих на Совете, с заголовками (разделители — запятые):  
`номер по порядку, имя, раса, возраст`  
`no, name, race, age`

Сгруппируйте участников Совета по расам и запишите в файл **council.jsonlines** в виде `json`-словарей (каждая строка — отдельный словарь) с ключами:  
`race` — раса, `members` — список представителей этой расы, отсортированный сначала по убыванию длины имени, затем по алфавиту.

Порядок строк в файле — по расе по алфавиту.

## Примеры

### Пример 1

**Ввод:**
```
no,name,race,age
1,Elrond,HalfElven,6500
2,Gandald,Maiar,2000
3,Galadriel,Elf,7000
4,Celeborn,Elf,6500
5,Glorfindel,Elf,6000
6,Aragorn,Man,87
7,Boromir,Man,41
8,Frodo,Hobbit,50
9,Samwise,Hobbit,38
10,Meriadoc,Hobbit,36
11,Peregrin,Hobbit,28
12,Bilbo,Hobbit,128
13,Gimli,Dwarf,139
14,Legolas,Elf,2931
15,Elrohir,HalfElven,2700
16,Elladan,HalfElven,2700
17,Arwen,HalfElven,2778
18,Erestor,Elf,5000
19,Gildor,Elf,5500
20,Haldir,Elf,3500
```

**Вывод:**
```
{"race": "Dwarf", "members": ["Gimli"]}
{"race": "Elf", "members": ["Glorfindel", "Galadriel", "Celeborn", "Erestor", "Legolas", "Gildor", "Haldir"]}
{"race": "HalfElven", "members": ["Elladan", "Elrohir", "Elrond", "Arwen"]}
{"race": "Hobbit", "members": ["Meriadoc", "Peregrin", "Samwise", "Bilbo", "Frodo"]}
{"race": "Maiar", "members": ["Gandald"]}
{"race": "Man", "members": ["Aragorn", "Boromir"]}
```
