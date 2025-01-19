import random
import time

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
        "John Doe",
        "Jane Smith",
        "Bartholomew Attenborough Jenkins",
        "Michael Johnson",
        "Emily Davis",
        "Christopher Anderson",
        "Maximilian Leopold von Hohenberg",
        "Olivia Brown",
        "William Martinez",
        "Theodora Alexandria Montgomery",
        "Sophia Garcia",
        "James Wilson",
        "Isabella Moore",
        "Benjamin Clark",
        "Seraphina Anastasia von Winterfeldt",
        "Charlotte Harris",
        "Alexander Thomas",
        "Gabrielle Marie Rosenthal-Klein"
        "Amelia Robinson",
        "Sebastian Lewis",
        "Lily Walker",
        "Sofia Kim",
    ]

    names2 = [
        "Liam Smith", "Emma Johnson", "Noah Brown", "Olivia Jones", "William Garcia",
        "Ava Martinez", "James Rodriguez", "Isabella Hernandez", "Benjamin Lopez", "Sophia Gonzalez",
        "Lucas Wilson", "Mia Anderson", "Henry Thomas", "Amelia Taylor", "Alexander Moore",
        "Charlotte Jackson", "Sebastian Lee", "Evelyn Perez", "Michael Thompson", "Abigail White",
        "Elijah Harris", "Emily Lewis", "Daniel Walker", "Harper Hall", "Matthew Allen",
        "Ella Young", "Joseph King", "Aria Wright", "David Scott", "Avery Green",
        "Samuel Adams", "Lily Nelson", "Gabriel Baker", "Chloe Carter", "Anthony Rivera",
        "Layla Mitchell", "Jack Campbell", "Zoe Roberts", "Christopher Carter", "Riley Diaz",
        "Andrew Edwards", "Nora Murphy", "Joshua Rivera", "Scarlett Torres", "Nathan Wood",
        "Hannah Ramirez", "Ryan Hughes", "Sofia Kim", "Jacob Flores", "Madison Morris"
    ]
    # Creating an array of 50 long names, each with 64 characters

    long_names_64 = [
        'Alexandria Josephine Marguerite Fitzwilliam-Hargrave von Eisenberg',
        'Bartholomew Percival Thaddeus Reginald Augustus Sinclair von Wood',
        'Cassandra Ophelia Evangeline Seraphina Isabella Montgomery-Wentworth',
        'Dimitri Maximilian Zacharias Constantine Alexander von Stuyvesant',
        'Eleanora Celestine Arabella Theodosia Christiana Brackenridge',
        'Fitzwilliam Archibald Sebastian Ignatius Rupert Alistair Montgomery',
        'Gabriella Isolde Melisande Vivienne Isabella Francesca de la Vega',
        'Harrison Leopold Augustus Theophilus Edmund Reginald von Smythe',
        'Isabella Seraphina Celestine Rosalind Arabella Anastasia Fairfax',
        'Jonathan Archibald Percival Fitzherbert Augustus Thaddeus Montague',
        'Katarina Evangeline Ophelia Seraphina Christiana von Brackenridge',
        'Lysander Thaddeus Constantine Leopold Zacharias Alexander Fitzwilliam',
        'Madeleine Ophelia Seraphina Anastasia Vivienne de la Vega Huntington',
        'Nathaniel Augustus Thaddeus Archibald Reginald Fitzwilliam von Wood',
        'Ophelia Celestine Arabella Isolde Persephone Christiana Fairfax',
        'Percival Archibald Thaddeus Rupert Ignatius Zacharias von Stuyvesant',
        'Quentin Maximilian Leopold Alexander Augustus Fitzherbert von Cavendish',
        'Rosalind Seraphina Evangeline Theodosia Christiana de la Cruz von Eisenberg',
        'Sebastian Ignatius Fitzwilliam Alexander Rupert Constantine von Trevelyan',
        'Theodosia Celestine Arabella Persephone Isolde Anastasia von Huntington',
        'Ulysses Alexander Zacharias Thaddeus Maximilian Archibald Montague',
        'Vivienne Seraphina Gabriella Ophelia Christiana Isolde de la Vega von Eisenberg',
        'William Augustus Archibald Reginald Leopold Theophilus von Trevelyan',
        'Xander Thaddeus Constantine Fitzwilliam Zacharias Ignatius von Fairfax',
        'Yvette Ophelia Melisande Seraphina Celestine Persephone von Wentworth',
        'Zacharias Fitzwilliam Alexander Ignatius Thaddeus Maximilian von Stuyvesant',
        'Aurelia Isolde Evangeline Arabella Christiana von Fotheringham',
        'Benedict Leopold Archibald Augustus Fitzherbert Theophilus von Ludendorff',
        'Catherine Seraphina Vivienne Ophelia Isolde Persephone von Trevelyan',
        'Dominic Thaddeus Constantine Maximilian Alexander Fitzwilliam von Fairfax',
        'Evangeline Theodosia Celestine Arabella Christiana von Eisenberg',
        'Fitzherbert Archibald Augustus Reginald Thaddeus Leopold von Wood',
        'Gabriel Alexander Zacharias Thaddeus Constantine von Ludendorff',
        'Helena Seraphina Arabella Isolde Evangeline Christiana von Fairfax',
        'Ignatius Thaddeus Maximilian Archibald Augustus von Fotheringham',
        'Juliana Celestine Ophelia Seraphina Persephone von Eisenberg',
        'Konstantin Alexander Fitzwilliam Leopold Augustus Thaddeus von Huntington',
        'Lydia Arabella Vivienne Theodosia Christiana Isolde de la Cruz von Ludendorff',
        'Maximilian Thaddeus Archibald Constantine Augustus von Stuyvesant',
        'Natalia Seraphina Celestine Isolde Persephone von Fairfax',
        'Octavius Alexander Zacharias Fitzwilliam Thaddeus von Cavendish',
        'Penelope Theodosia Evangeline Arabella Christiana von Eisenberg',
        'Quincy Maximilian Thaddeus Archibald Augustus von Stuyvesant',
        'Rosamund Seraphina Celestine Ophelia Vivienne Christiana von Ludendorff',
        'Sebastiana Thaddeus Constantine Fitzwilliam Alexander Ignatius von Trevelyan',
        'Theodore Archibald Augustus Reginald Leopold Theophilus von Cavendish',
        'Ursula Arabella Seraphina Isolde Persephone von Eisenberg',
        'Valentin Alexander Zacharias Fitzwilliam Thaddeus von Wood',
        'Wilhelmina Celestine Ophelia Evangeline Christiana von Fairfax',
        'Xavier Thaddeus Maximilian Augustus Fitzherbert von Ludendorff'
    ]

    names_increasing_length = [
        "Abcdefghij",  # 10 characters
        "Abcdefghijk",  # 11 characters
        "Abcdefghijkl",  # 12 characters
        "Abcdefghijklm",  # 13 characters
        "Abcdefghijklmn",  # 14 characters
        "Abcdefghijklmno",  # 15 characters
        "Abcdefghijklmnop",  # 16 characters
        "Abcdefghijklmnopq",  # 17 characters
        "Abcdefghijklmnopqr",  # 18 characters
        "Abcdefghijklmnopqrs",  # 19 characters
        "Abcdefghijklmnopqrst",  # 20 characters
        "Abcdefghijklmnopqrstu",  # 21 characters
        "Abcdefghijklmnopqrstuv",  # 22 characters
        "Abcdefghijklmnopqrstuvw",  # 23 characters
        "Abcdefghijklmnopqrstuvwx",  # 24 characters
        "Abcdefghijklmnopqrstuvwxy",  # 25 characters
        "Abcdefghijklmnopqrstuvwxyz",  # 26 characters
        "Abcdefghijklmnopqrstuvwxyza",  # 27 characters
        "Abcdefghijklmnopqrstuvwxyzab",  # 28 characters
        "Abcdefghijklmnopqrstuvwxyzabc"  # 29 characters
    ]

    # Randomly select 20 names from the list
    # selected_names = random.sample(names, 20)
    # selected_names = random.sample(long_names_64, 20)
    selected_names = names

    for num, name_ in enumerate(reversed(selected_names)):
        score_ = num + 100 + random.random()
        submit_score(name_, score_)
        time.sleep(5)

    # for name_ in selected_names:
    #     score_ = random.uniform(20, 160)
    #     submit_score(name_, score_)
    #     time.sleep(2)
