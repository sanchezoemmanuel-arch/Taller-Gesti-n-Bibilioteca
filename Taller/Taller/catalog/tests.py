from django.test import TestCase
from .models import Book, Author

class BibliotecaTests(TestCase):

    def test_01_creacion_autor(self):
        autor = Author.objects.create(first_name="Joe", last_name="Dispenza")
        self.assertEqual(autor.first_name, "Joe")

    def test_02_apellido_autor(self):
        autor = Author.objects.create(first_name="Emmanuel", last_name="Sánchez")
        self.assertEqual(autor.last_name, "Sánchez")

    def test_03_autor_vacio(self):
        autor = Author.objects.create(first_name="", last_name="")
        self.assertEqual(autor.first_name, "")

    def test_04_conteo_autores(self):
        Author.objects.create(first_name="A", last_name="B")
        Author.objects.create(first_name="C", last_name="D")
        self.assertEqual(Author.objects.count(), 2)

    def test_05_orden_autores(self):
        Author.objects.create(first_name="Z", last_name="Zapata")
        Author.objects.create(first_name="A", last_name="Alvarez")
        self.assertEqual(Author.objects.all().first().last_name, "Alvarez")

    def test_06_id_autor(self):
        autor = Author.objects.create(first_name="Test", last_name="Test")
        self.assertIsNotNone(autor.id)

   
    def test_07_str_libro(self):
        libro = Book.objects.create(title="Deja de ser tu", author="Joe Dispenza")
        self.assertEqual(str(libro), "Deja de ser tu (Joe Dispenza)")

    def test_08_disponibilidad_por_defecto(self):
        libro = Book.objects.create(title="Libro", isbn="123")
        self.assertTrue(libro.is_available)

    def test_09_resumen_largo(self):
        libro = Book.objects.create(title="R", summary="A"*500)
        self.assertEqual(len(libro.summary), 500)

    def test_10_isbn_guardado(self):
        libro = Book.objects.create(title="ISBN Test", isbn="9781234567890")
        self.assertEqual(libro.isbn, "9781234567890")

    def test_11_borrado_libro(self):
        libro = Book.objects.create(title="Borrar", isbn="000")
        libro.delete()
        self.assertEqual(Book.objects.count(), 0)

    def test_12_cambio_disponibilidad(self):
        libro = Book.objects.create(title="Libro", is_available=True)
        libro.is_available = False
        libro.save()
        self.assertFalse(libro.is_available)
