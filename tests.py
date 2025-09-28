import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #проверяем добавление книг с валидной длиной названия
    @pytest.mark.parametrize('name',['А','Моана','Бббббббббббббббббббббббббббббббббббббббб']) 
    def test_add_new_book_valid_lenght(name):
        collector = BooksCollector()
        if 0 < len(name) < 41:
            collector.add_new_book(name)
            assert name in collector.books_genre

    #проверяем, что книги не добавляются с невалидной длиной названия
    @pytest.mark.parametrize('name',[' ','длинноеназваниекотороепревышаетсорокодинс']) 
    def test_add_new_book_invalid_lenght(name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre
        
    # проверяем, что книге устанавливается жанр
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'
