import flet as ft

def main(page):
    page.title = "Card Example"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Grocery Delivery, Mombasa"),
                            subtitle=ft.Text(
                                "pickup groceries at Naivas Supermarket..."
                            ),
                            subtitle=ft.Text("Deadline at November 10, 2023 10:00 am"),
                        ),
                        ft.Row(
                            [ft.TextButton("View"), ft.TextButton("Confirm")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

ft.app(target=main)
  
