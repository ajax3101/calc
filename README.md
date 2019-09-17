# Калькулятор
Перевод арабских чисел в римские и наоборот. 
Иногда возникает потребность подсчета десятичных чисел в римские числа и наоборот. Именно для простого решения данной проблемы и создан онлайн калькулятор, который конвертирует десятичные числа в римские и обратно. В специальную ячейку, Вы сможете ввести значение десятичное числа и, нажав кнопку “перевести”, Вы получите римское число справа. 
Этот калькулятор может послужить очень хорошую службу, если вам вдруг понадобилось узнать, как обозначить, то или иное число римским символом, это Вы сможете сделать за считанные секунды. Лишь воспользуйтесь данным калькулятором.
## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/ajax3101/calc.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
