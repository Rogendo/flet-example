import flet as ft
from flet import *

def main(page :ft.Page):
  page.title="counter app"
  page.vertical_allignment= "center"
  page.theme_mode = "system"

  text_input=ft.TextField(value="0", text_align="center")

  def minus_clicked(e):
    text_input.value=int(text_input.value) -1
    page update

  def plus_clicked(e):
    text_input.value=int(text_input.value)+1
    page.update
    
  page.add(
    ft.Row(
      controls[
        ft.IconButton(ft.icons.REMOVE, on_click=minus_clicked),
        text_input,
        ft.IconButton(ft.icons.PLUS, on_click=plus_clicked),
        
      ],
      alignment="center"
    )
  )

ft.app(target=main)
