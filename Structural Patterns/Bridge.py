# You are building a web application where users can select different themes (Light Mode, Dark Mode) and different UI Components (Buttons, Textboxes, Checkboxes).

# Instead of creating every possible combination like:

#     LightButton, DarkButton
#     LightTextBox, DarkTextBox

# We separate the Theme (Abstraction) from the UI Component (Implementation).


class Theme:
    def get_color(self):
        pass

class LightTheme(Theme):
    def get_color(self):
        return "White background with black text"
    
class DarkTheme(Theme):
    def get_color(self):
        return "Black background and white text"
    
class UIComponent:
    def __init__(self, theme : Theme):
        self.theme = theme    #this is the bridge between theme and UI component
    def render(self):
        pass

class Button(UIComponent):
    def render(self):
        print(f"Render button {self.theme.get_color()}")

class TextBox(UIComponent):
    def render(self):
        print(f"Render Text box {self.theme.get_color()}")



if __name__ == "__main__":
    light_theme = LightTheme()
    darktheme = DarkTheme()

    light_button = Button(light_theme)
    dark_text = TextBox(darktheme)

    light_button.render()
    dark_text.render()


    


        