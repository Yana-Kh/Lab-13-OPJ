# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_anime(**kwargs):
    """
    Названия аниме по именам героям
    """
    print("На ошибках учатся, после ошибок лечатся")
    if kwargs:
        for name, anime in kwargs.items():
            print(f"{anime}: {name}")
    else:
        return None


if __name__ == "__main__":
    print_anime(
        Kakashi="Naruto", Sakura="Naruto",
        Narumi="Otaku ni Koi wa Muzukashii",
        Violet="Violet Evergarden",
        Ban="Nanatsu no Taizai: The Seven Deadly Sins",
        Akutagava="Bungo sutorei doggusu"
    )
