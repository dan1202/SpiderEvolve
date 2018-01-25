# import random
# import math
# import numpy as np
#
# import pygame
# from pygame.color import THECOLORS
#
# import pymunk
# from pymunk.vec2d import Vec2d
# from pymunk import pygame_util
#
# fps = 60.0
# pygame.init()
# screen = pygame.display.set_mode((690, 300))
# clock = pygame.time.Clock()
# 
# clock.tick(1 / 5.)
#
# ### Physics stuff
# space = pymunk.Space()
# space.gravity = 0, 900
# space.sleep_time_threshold = 0.3
#
# draw_options = pygame_util.DrawOptions(screen)
# pygame_util.positive_y_is_up = False
#
# ### Physics stuff
# space = pymunk.Space()
# space.gravity = 0, 900
# space.sleep_time_threshold = 0.3
#
# draw_options = pygame_util.DrawOptions(screen)
# pygame_util.positive_y_is_up = False
#
# floor = pymunk.Segment(space.static_body, (-100, 210), (1000, 210), 5)
# floor.friction = 1.0
# space.add(floor)
#
#
# # class Spider:
# #     """Class Spyder. Physics Engine and Simulation"""
# #
# #     def __init__(self, position_XY):
# #         self.position_XY = position_XY
# #
# #         # Physics stuff.
# #         self.space = pymunk.Space()
# #         self.space.gravity = pymunk.Vec2d(0., 0.)
#
#
# def spider_create(space):
#     pos = Vec2d(100, 200)
#
#     first_arm_color = 0, 0, 0
#     second_arm_color = 50, 50, 50
#
#     wheel_color = 52, 219, 119
#     mass = 100
#     radius = 10
#     moment = pymunk.moment_for_circle(mass, 20, radius)
#     wheel1_b = pymunk.Body(mass, moment)
#     wheel1_s = pymunk.Circle(wheel1_b, radius)
#     wheel1_s.friction = 1.5
#     wheel1_s.color = wheel_color
#     space.add(wheel1_b, wheel1_s)
#
#     mass = 100
#     radius = 10
#     moment = pymunk.moment_for_circle(mass, 20, radius)
#     wheel2_b = pymunk.Body(mass, moment)
#     wheel2_s = pymunk.Circle(wheel2_b, radius)
#     wheel2_s.friction = 1.5
#     wheel2_s.color = wheel_color
#     space.add(wheel2_b, wheel2_s)
#
#     mass = 100
#     size = (50, 30)
#     moment = pymunk.moment_for_box(mass, size)
#     chassi_b = pymunk.Body(mass, moment)
#     chassi_s = pymunk.Poly.create_box(chassi_b, size)
#     space.add(chassi_b, chassi_s)
#
#     wheel1_b.position = pos - (55, 0)
#     wheel2_b.position = pos + (55, 0)
#     chassi_b.position = pos + (0, -25)
#
#     space.add(
#         pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), (-25, -15)),
#         pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), (-25, 15)),
#         pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), (25, -15)),
#         pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), (25, 15))
#     )
#
#     first_arm = pymunk.Segment(chassi_b, (25, -15), (30, -40), 2)
#     space.add(first_arm)
#     space.add(pymunk.PinJoint(first_arm, chassi_b, (0, 0), (25, -15)))
#
#     speed = 4
#     space.add(
#         pymunk.SimpleMotor(wheel1_b, chassi_b, speed),
#         pymunk.SimpleMotor(wheel2_b, chassi_b, speed)
#     )
#
# events = []
# events.append((0.1, spider_create))
# # while True:
# t = events[0]
# # f = events[1]
#
# spider_create(space)
# space.step(1. / fps)
#
# while True:
#     screen.fill(pygame.color.THECOLORS["white"])
#     space.debug_draw(draw_options)
#     pygame.display.flip()
#     dt = clock.tick(fps)
