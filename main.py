"""Фоторедактор"""

import tkinter as tk
import numpy as np
from photo import Photo


class Application:
    """Класс приложения"""
    def __init__(self):
        # Экран
        self.screen = tk.Tk()

        # Отображаемое изображение для tkinter
        self.img = Photo.open('img.png')

        # Холст
        self.can = tk.Canvas(self.screen, width=self.img.img.width(), height=self.img.img.height())
        self.can.create_image(0, 0, anchor='nw', image=self.img.img)
        self.can.bind('<Button-1>', self.set_black)

        # Отрисовка
        self.can.pack()

        # Бесконечный цикл
        self.screen.mainloop()

    def set_black(self, event: tk.Event):
        """Обработчик нажатия на холст"""
        self.img.img_arr[event.y][event.x] = np.array([0, 0, 0, 255])
        # Отрисовка
        self.img.convert()
        self.can.create_image(0, 0, anchor='nw', image=self.img.img)
        self.can.pack()


if __name__ == '__main__':
    app = Application()
