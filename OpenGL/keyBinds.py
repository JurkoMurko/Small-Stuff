import pygame

key_flag = {
        pygame.KEYDOWN: True,
        pygame.KEYUP: False
    }

speed = 0.1

keys = {
    'up': {
        "code": pygame.K_LSHIFT,
        "flag": False,
        "xDir": 0,
        'yDir': -speed,
        'zDir': 0
    },
    'down': {
        'code': pygame.K_LCTRL,
        "flag": False,
        "xDir": 0,
        'yDir': speed,
        'zDir': 0
    },
    'left': {
        'code': pygame.K_a,
        "flag": False,
        "xDir": speed,
        'yDir': 0,
        'zDir': 0
    },
    'right': {
        'code': pygame.K_d,
        "flag": False,
        "xDir": -speed,
        'yDir': 0,
        'zDir': 0
    },
    'forward': {
        'code': pygame.K_w,
        "flag": False,
        "xDir": 0,
        'yDir': 0,
        'zDir': speed
    },
    'backward': {
        'code': pygame.K_s,
        "flag": False,
        "xDir": 0,
        'yDir': 0,
        'zDir': -speed
    }
}