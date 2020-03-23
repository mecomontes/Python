import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


class IngresarTasa (GridLayout):
    def __init__(self, **kwargs):
        super ( IngresarTasa, self ).__init__ ( **kwargs )
        self.cols = 1
        self.add_widget(Label(text="Ingrese la tasa sin % :"))


class MyGrid ( GridLayout ):
    def __init__(self, **kwargs):
        super ( MyGrid, self ).__init__ ( **kwargs )
        self.cols = 1

        self.inside = GridLayout ()
        self.inside.cols = 4

        self.inside.add_widget ( Label ( text="Ingrese los parametros de la tasa dada: " ) )

        self.parnomi = Spinner (

            text='NOMINAL',
            values=('Ninguno', 'Anual', 'Semestral', 'Trimestral', 'Bimestral', "Mensual", "Quincenal", "Diario"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parnomi )

        self.parperi = Spinner (

            text='PERIODO',
            values=('Anual', 'Semestral', 'Trimestral', 'Bimestral', "Mensual", "Quincenal", "Diario"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parperi )

        self.parvoai = Spinner (

            text='Vencida',
            values=("Vencida", "Anticipada"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parvoai )

        self.inside.add_widget ( Label ( text="Ingrese los parametros de la tasa deseada: " ) )
        self.parnomf = Spinner (

            text='NOMINAL',
            values=('Ninguno', 'Anual', 'Semestral', 'Trimestral', 'Bimestral', "Mensual", "Quincenal", "Diario"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parnomf )

        self.parperf = Spinner (

            text='PERIODO',
            values=('Anual', 'Semestral', 'Trimestral', 'Bimestral', "Mensual", "Quincenal", "Diario"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parperf )

        self.parvoaf = Spinner (

            text='Vencida',
            values=("Vencida", "Anticipada"),
            size_hint=(None, 1),
            size=(100, 44),
            pos_hint={'center_x': 1, 'center_y': .5} )

        self.inside.add_widget ( self.parvoaf )

        self.add_widget ( self.inside )

        self.calcular = Button ( text="CALCULAR", font_size=40, size_hint=(1, 1),

                                 size=(100, 44),
                                 pos_hint={'center_x': 1, 'center_y': .5} )
        self.calcular.bind ( on_press=self.pressed )
        self.add_widget ( self.calcular )

    def pressed(self, instance):
        tasa = self.tasa.text
        parametrosi = self.parametrosi.text
        parametrosf = self.parametrosf.text
        print ( "Tasa ingresada: ", tasa, "Parametros dados: ", parametrosi, " Parametros buscados: ", parametrosf )


class MyApp ( App ):
    def build(self):
        return MyGrid ()


if __name__ == "__main__":
    MyApp ().run ()


	
	
	
