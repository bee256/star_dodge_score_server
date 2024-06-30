import requests
import socket
import platform
# import uuid

API_URL = 'http://192.168.178.71:8123'


def submit_score(name, score, screen_width, screen_height, nickname = None, email = None):
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


def get_scores():
    response = requests.get(f'{API_URL}/get_scores')
    scores = response.json()
    for score in scores:
        print(score)


if __name__ == '__main__':
    response = requests.get(f'{API_URL}/ping')
    # Example usage
    name = 'Hans'
    # nickname = 'Johnny'
    email = 'hans@acme.org'
    score = 112.56
    screen_width = 1200
    screen_height = 800

    submit_score(name, score, screen_width, screen_height, email=email)
    # get_scores()
