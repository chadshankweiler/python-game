from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, _, img_file in walk(path):
        for img in img_file:
            full_path = path + "/" + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list
