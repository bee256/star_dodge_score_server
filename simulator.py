import sys
import time
import random

import requests
import socket
import platform

# import uuid

# API_URL = 'http://192.168.178.71:8123'
API_URL = 'http://127.0.0.1:8123'


def submit_score(name, score, screen_width: int = 0, screen_height: int = 0, nickname=None, email=None):
    computer_name = socket.gethostname()
    os_info = platform.system() + " " + platform.release()
    data = {
        'name': name,
        'nickname': nickname,
        'email': email,
        'score': score,
        'computer_name': computer_name,
        'os': os_info,
        'screen_width': screen_width,
        'screen_height': screen_height
    }
    try:
        response = requests.post(f'{API_URL}/submit_score', json=data)
        response.raise_for_status()
    except Exception as err:
        print(f"An error occurred: {err}")
    else:
        print(response.json())


def get_scores(num_recs: int = 20):
    response = requests.get(f'{API_URL}/get_scores?n={num_recs}')
    scores = response.json()
    for score in scores:
        print(score)


if __name__ == '__main__':
    # response = requests.get(f'{API_URL}/ping')
    # get_scores(num_recs=10)

    # # Example usage
    # name = 'Hans'
    # # nickname = 'Johnny'
    # email = 'hans@acme.org'
    # score = 112.56
    # screen_width = 1200
    # screen_height = 800
    #
    # submit_score(name, score, screen_width, screen_height, email=email)
    # get_scores()

    names = [
        'Liam Wang',
        'Ethan Patel',
        'Lucas Santos',
        'Noah Kim',
        'Mason Chen',
        'Alexander Ivanov',
        'Daniel Müller',
        'James Takahashi',
        'William Garcia',
        'Michael López',
        'Emma Nguyen',
        'Olivia Sharma',
        'Ava Smith',
        'Sophia Dubois',
        'Isabella Fernandez',
        'Mia Rossi',
        'Charlotte Li',
        'Amelia Johnson',
        'Harper Brown',
        'Evelyn Jones'
    ]

    for name_ in names:
        score_ = random.uniform(20, 160)
        submit_score(name_, score_)
        time.sleep(2)
