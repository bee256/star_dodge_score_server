# Star Dodge Score Server

This repository contains the server-side application for managing high scores for the [**Star Dodge**](https://github.com/bee256/star_dodge) game.
It is designed to store, retrieve, and serve player scores, enabling seamless integration with the game.

## Features

- **RESTful API** for submitting and retrieving high scores.
- Storage of player scores in a SQLite db alongside other client data
- Integration-ready with the **Star Dodge** game.
- Simple and lightweight Python implementation for easy setup.
- Simulator to add scores for testing purposes.

The code of this project was mainly written by generative AI.

## Prerequisites

To run the score server, ensure you have the following installed:

- Python 3.12 or later
- Required Python packages (see `requirements.txt`)

## Setup

Follow these steps to set up and run the score server locally:

### Clone the Repository

```bash
git clone https://github.com/bee256/star_dodge_score_server.git
cd star_dodge_score_server
```

### Install Dependencies

Install the required dependencies with:
```bash
pip install -r requirements.txt
```

### Run the server

Start the server using the following command:

```bash
python app.py
```

The server will come up and create an empty database instance at `instance/scores.db`.
The console input indicates a development servers, however, the performance is enough for many gaming clients.

#### Console output
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8123
 * Running on http://192.168.178.111:8123
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 452-250-555
 ```
#### Simulator

Run the simulator to add some test data. If the [**Star Dodge**](https://github.com/bee256/star_dodge) game is
run in high score server mode, it will update the high scores every 5 seconds and play a sound if a player
made it to the top ten. 

```bash
python simulator.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
