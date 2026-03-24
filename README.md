import json, urllib.request, base64, threading, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

class DrokApp(App):
    def build(self):
        # Запрос прав сразу при запуске
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.lbl = Label(text="ВЫБЕРИ ФОТО ИЗ ГАЛЕРЕИ", font_size='20sp')
        self.layout.add_widget(self.lbl)

        self.btn_gallery = Button(text="ОТКРЫТЬ ГАЛЕРЕЮ", size_hint_y=None, height=150)
        self.btn_gallery.bind(on_press=self.open_gal)
        self.layout.add_widget(self.btn_gallery)
        
        return self.layout

    def open_gal(self, instance):
        try:
            from plyer import filechooser
            filechooser.open_file(on_selection=self.on_sel)
        except:
            self.lbl.text = "Ошибка: Plyer не найден"

    def on_sel(self, selection):
        if selection:
            self.lbl.text = f"Файл выбран: {os.path.basename(selection[0])}"
            # Тут пойдет твоя логика отправки на GitHub
