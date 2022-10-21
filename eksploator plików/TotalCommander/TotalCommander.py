import kivy                         # import koniecznych modułów
from kivy.app import App
from kivy.uix.label import Label  # moduł odpowiadający za GUI
from kivy.uix.gridlayout import GridLayout   # moduł odpowiadający za GUI
from kivy.uix.textinput import TextInput    # moduł odpowiadający za GUI
from kivy.uix.button import Button          # IMPORTUJE PRZYCISK



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        #super(MyGrid, self).__init__(**kwargs) # We use **kwargs because we don't know how many arguments we may receive. 
        #self.cols = 2 # We define the amount of columns to be 2

        #self.add_widget(Label(text="Name: "))  # Add a label widget 
        #self.name = TextInput(multiline = False)  # Create a Text input box stored in the name variable
        #self.add_widget(self.name)  # Add the text input widget to the GUI

        #self.add_widget(Label(text="Last Name: "))
        #self.lastName = TextInput(multiline=False)
        #self.add_widget(self.lastName)

        #self.add_widget(Label(text="Email: "))
        #self.email = TextInput(multiline=False)
        #self.add_widget(self.email)

        #self.submit = Button(text="Submit", font_size=40)  
        #self.add_widget(self.submit) # Adding this inside the __init__ of the class will create a button for us


        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1 # Set columns for main layout

        self.inside = GridLayout() # Create a new grid layout
        self.inside.cols = 2 # set columns for the new grid layout

        # ALL OF THESE ARE APART OF THE (INTERIOR)NEW LAYOUT
        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: ", font_size=22))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        #-------------------------------------------------

        self.add_widget(self.inside) # Add the interior layout to the main

        self.submit = Button(text="Submit", font_size=48)
       
        self.add_widget(self.submit) # Add the button to the main layout 
        self.submit.bind(on_press=self.pressed)
        # pressed is the name of the method we want to run
        # submit is clearly the name of our button


     # This goes inside our class MyGrid
    def pressed(self, instance):
        # Get the value of all of the tex inputs
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        # print the values to the screen
        print("Name:", name, "Last Name:", last, "Email:", email)

        # Reset text to blank in each text input
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""





class MyApp(App):  # klasa reprezentująca okno aplikacji
    def build(self):  # metoda build() mówi Kivy co umieścić na ekranie
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

