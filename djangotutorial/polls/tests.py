import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class PruebasModeloPregunta(TestCase):
    def test_publicada_recientemente_con_pregunta_futura(self):
        tiempo = timezone.now() + datetime.timedelta(days=30)
        pregunta_futura = Question(pub_date=tiempo)
        self.assertIs(pregunta_futura.was_published_recently(), False)

    def test_publicada_recientemente_con_pregunta_antigua(self):
        tiempo = timezone.now() - datetime.timedelta(days=1, seconds=1)
        pregunta_antigua = Question(pub_date=tiempo)
        self.assertIs(pregunta_antigua.was_published_recently(), False)

    def test_publicada_recientemente_con_pregunta_reciente(self):
        tiempo = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        pregunta_reciente = Question(pub_date=tiempo)
        self.assertIs(pregunta_reciente.was_published_recently(), True)


def crear_pregunta(texto_pregunta, dias):
    tiempo = timezone.now() + datetime.timedelta(days=dias)
    return Question.objects.create(
        question_text=texto_pregunta,
        pub_date=tiempo
    )


class PruebasVistaIndice(TestCase):
    def test_sin_preguntas(self):
        respuesta = self.client.get(reverse("polls:index"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "No hay encuestas disponibles.")
        self.assertQuerySetEqual(
            respuesta.context["latest_question_list"],
            []
        )

    def test_pregunta_pasada(self):
        pregunta = crear_pregunta("Pregunta pasada.", -30)
        respuesta = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            respuesta.context["latest_question_list"],
            [pregunta]
        )

    def test_pregunta_futura(self):
        crear_pregunta("Pregunta futura.", 30)
        respuesta = self.client.get(reverse("polls:index"))
        self.assertContains(respuesta, "No hay encuestas disponibles.")
        self.assertQuerySetEqual(
            respuesta.context["latest_question_list"],
            []
        )

    def test_pregunta_futura_y_pregunta_pasada(self):
        pregunta = crear_pregunta("Pregunta pasada.", -30)
        crear_pregunta("Pregunta futura.", 30)
        respuesta = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            respuesta.context["latest_question_list"],
            [pregunta]
        )

    def test_dos_preguntas_pasadas(self):
        pregunta1 = crear_pregunta("Pregunta pasada 1.", -30)
        pregunta2 = crear_pregunta("Pregunta pasada 2.", -5)
        respuesta = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            respuesta.context["latest_question_list"],
            [pregunta2, pregunta1]
        )


class PruebasVistaDetalle(TestCase):
    def test_pregunta_futura(self):
        pregunta_futura = crear_pregunta("Pregunta futura.", 5)
        url = reverse("polls:detail", args=(pregunta_futura.id,))
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 404)

    def test_pregunta_pasada(self):
        pregunta_pasada = crear_pregunta("Pregunta pasada.", -5)
        url = reverse("polls:detail", args=(pregunta_pasada.id,))
        respuesta = self.client.get(url)
        self.assertContains(respuesta, pregunta_pasada.question_text)