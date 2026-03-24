import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class DrokApp(App):
    def build(self):
        # Запрашиваем доступ к памяти в самом начале
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

        layout = BoxLayout(orientation='vertical', padding=20)
        self.lbl = Label(text="ПРИЛОЖЕНИЕ ГОТОВО", font_size='20sp')
        layout.add_widget(self.lbl)

        btn = Button(text="ОТКРЫТЬ ГАЛЕРЕЮ", size_hint_y=None, height='100dp')
        btn.bind(on_press=self.open_gal)
        layout.add_widget(btn)
        return layout

    def open_gal(self, instance):
        try:
            from plyer import filechooser
            filechooser.open_file(on_selection=self.on_sel)
        except Exception as e:
            self.lbl.text = f"Ошибка: {str(e)}"

    def on_sel(self, selection):
        if selection:
            self.lbl.text = f"Выбран: {os.path.basename(selection[0])}"

if __name__ == '__main__':
    DrokApp().run()
