#flet hello world app
import flet as ft
from flet import Text, TextField
from flet import *

def main(page :ft.Page):
  page.title = "hello world app"
  page.theme_mode= "dark"

  message = ft.Text(value= "hello guys, this us my first flutter app")
  page.add(message)

flet.app(terget=main)
