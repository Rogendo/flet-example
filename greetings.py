import flet as ft
from flet import *

def main(page:ft.Page):
  page.title="greet app"
  page.theme_ = "dark"
  
  first_name=ft.TextField(place_holder="First name", autofocus=True)
  last_name=ft.TextFIeld(place_holder="las name", autofocus= True)
  greet_message="hello {}.value {}.value !"
  
  def click_btn(e):
    

    
  greet_button=ft.ElevatedButton(text="Greet", onClick=click_btn)
  
