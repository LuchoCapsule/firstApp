import flet as ft

def main(page: ft.Page):
    page.title = "Flet HTML Example"
    
    # Create a header
    header = ft.Text("Welcome to Flet!", style="headlineMedium")
    
    # Create a text field
    text_field = ft.TextField(label="Enter your name")
    
    # Define a function to handle button clicks
    def on_click(e):
        name = text_field.value
        page.snack_bar = ft.SnackBar(ft.Text(f"Hello, {name}!"), open=True)
        page.update()
    
    # Create a button
    button = ft.ElevatedButton("Submit", on_click=on_click)
    
    # Add the components to the page
    page.add(header, text_field, button)

# Run the app
ft.app(target=main)