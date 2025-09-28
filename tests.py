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
    @pytest.mark.parametrize('name',['А', 'Моана', 'Бббббббббббббббббббббббббббббббббббббббб']) 
    def test_add_new_book_valid_lenght(name):
        collector = BooksCollector()
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
    
    #проверяем, что можем получить жанр по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Голый пистолет')
        collector.set_book_genre('Голый пистолет', 'Комедия')
        assert collector.get_book_genre('Голый пистолет') == 'Комедия'

    #проверяем, что можем вывести список с определенны жанром
    @pytest.mark.parametrize('genre,name',[('Комедия',['Голый пистолет']),('Ужасы',['Оно'])])
    def test_get_books_with_specific_genre(genre,name):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(genre) == name

    # проверяем, что можем получить словарь books_genre
    def test_get_books_genre():
        collector = BooksCollector()
        collector.add_new_book('Заклятие')
        collector.set_book_genre('Заклятие', 'Ужасы')
        collector.add_new_book('Голый пистолет')
        collector.set_book_genre('Голый пистолет', 'Комедия')
        books_genre = collector.get_books_genre()
        assert 'Заклятие' in books_genre
        assert books_genre['Заклятие'] == 'Ужасы'
        assert 'Голый пистолет' in books_genre
        assert books_genre['Голый пистолет'] == 'Комедия'
    
    #проверяем, что можем вернуть книги, подходящие детям
    @pytest.mark.parametrize('name,genre', [('Моана', 'Мультфильм'),('Заклятие','Ужасы')])
    def test_get_books_for_children(name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.genre_age_rating = {'Ужасы':'18+', 'Детективы': '16+'}
        books_for_children = collector.get_books_for_children()
        assert name in books_for_children if genre not in collector.genre_age_rating else name not in books_for_children

    #проверяем, что можем добавить книгу в избранное     
    def test_add_book_in_favorites():
        collector = BooksCollector()
        collector.add_new_book('Сказка')
        collector.set_book_genre('Сказка', 'Мультфильм')
        collector.add_book_in_favorites('Сказка')
        assert 'Сказка' in collector.get_list_of_favorites_books()

    #проверяем, что можем удалить книгу из избранного
    def test_delete_book_from_favorites():
        collector = BooksCollector()
        collector.favorites = ['Сказка', 'Оно']
        collector.delete_book_from_favorites('Сказка')
        assert 'Сказка' not in collector.get_list_of_favorites_books()
        assert 'Оно' in collector.get_list_of_favorites_books()

    #проверяем, что можем получить список избранных книг
    def test_get_list_of_favorites_books():
        collector = BooksCollector()
        collector.favorites = ['Моана', 'Оно', 'Заклятие']
        favorites_list = collector.get_list_of_favorites_books()
        assert favorites_list == ['Моана', 'Оно', 'Заклятие']





