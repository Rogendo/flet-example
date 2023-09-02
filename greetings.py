import flet as ft
from flet import *

def main(page:ft.Page):
  page.title="greet app"
  page.theme_ = "dark"
  
  first_name=ft.TextField(label="First name", autofocus=True)
  last_name=ft.TextFIeld(label="last name", autofocus= True)
  greetings = ft.Column()

      def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

ft.app(target=main)
