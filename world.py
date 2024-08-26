import pygame as pg
from enemy_data import ENEMY_SPAWN_DATA
import constants as c
import random

class World():
    def __init__(self, data, map_image) -> None:
        self.level = 1
        self.game_speed = 1
        self.health = c.HEALTH
        self.money = c.MONEY
        self.waypoints = []
        self.tile_map = []
        self.level_data = data
        self.image = map_image
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def process_data(self):
        for layer in self.level_data["layers"]:
            if layer["name"] == "tilemap":
                self.tile_map = layer["data"]
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoints_data = obj["polyline"]
                    self.process_waypoints(waypoints_data)

    def process_waypoints(self, data):
        for point in data:
            self.waypoints.append((point.get("x"), point.get("y")))

    def process_enemies(self):
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)

    def check_level_complete(self):
        if self.killed_enemies + self.missed_enemies == len(self.enemy_list):
            return True

    def reset_level(self):
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def draw(self, surface):
        surface.blit(self.image, (0, 0))