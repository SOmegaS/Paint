"""Модуль класса изображения"""

import numpy as np
from PIL import Image, ImageTk


class Photo:
    """Класс изображения"""
    def __init__(self, img_arr=None):
        """"""
        # Массив изображения
        self.img_arr = img_arr

        if self.img_arr is not None:
            # Выводимое изображение
            self.img = ImageTk.PhotoImage(Image.fromarray(self.img_arr))

    def convert(self):
        """Конвертирует массив в изображение"""
        self.img = ImageTk.PhotoImage(Image.fromarray(self.img_arr))

    @staticmethod
    def open(path: str):
        """
        Открывает изображение из файла
        :param path: путь к файлу
        :return: экземпляр класса
        """
        # Открытие фото
        img = Image.open(path)
        # Запись изображения в массив
        img_arr = np.array(img)
        # Создание и возврат экземпляра класса
        return Photo(img_arr)
