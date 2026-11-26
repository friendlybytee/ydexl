# Библиотека Кэр-Параваля

| Характеристика | Значение |
| --- | --- |
| **Категория** | Дополнительные задачи |
| **Макс. балл** | 33 |
| **Ограничение времени** | 1.2 секунды |
| **Ограничение памяти** | 64 Мб |
| **Ввод** | books.csv |
| **Вывод** | library.docx |
| **ID задачи** | `94981` |

---

## Условие

В библиотеке замка ведут каталог книг в файле **books.csv**.  
Формат:  
`ID;Название;Автор;Год;Количество_копий`  
`id;Title;Author;Year;Copies

Напишите программу, которая:

* Читает CSV-файл и построчно обрабатывает данные.
* Для каждой книги, у которой количество копий > 1, создает карточку книги в формате Word по шаблону **book\_card.docx** (поля: `ID, Title, Author, Year, Copies`).
* Сохраняет все карточки, каждую на новой странице, в файл **library.docx**.

Если подходящих книг не найдено, итоговый файл создаётся, но пустой.

Файл шаблона можно скачать по [ссылке](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..MINpLlgm1rZS-bzb.C1SOdputUDmRKvc6Ub2jjdL653uCLgraApBEjsU_NXMbOnjBUqX1R85PLCObM1oXBFjjXnx81aoAWkNjo8IbDzfgqdhllsAbG83o-k8.6erWBhEi2y_KWLWmutiCyA).

### Пример входного CSV-файла:

```
ID;Title;Author;Year;Copies
1;The Lion, the Witch and the Wardrobe;C.S. Lewis;1950;5
2;Prince Caspian: The Return to Narnia;C.S. Lewis;1951;3
3;The Voyage of the Dawn Treader;C.S. Lewis;1952;2
4;The Silver Chair;C.S. Lewis;1953;1
5;The Horse and His Boy;C.S. Lewis;1954;4
6;The Magician's Nephew;C.S. Lewis;1955;1
7;The Last Battle;C.S. Lewis;1956;1
```

Пример результата на файле из примера [library.docx](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..EveIPn2c_E9bUUwJ.HMpzw3D_ApaRnNnAn7he7dpZ-BGdBfGiqipAIE3lRpzHU54CglUHOutNSq32kWti5JYbgHzutMnGNK9kEko2LV-A8sLQei4YHDoA.IKv0jMLmSTaAXKPE6W8WDg).
