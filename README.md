# spectra-client

## Introduction
Spectra client - use to get video from server and display it.

## Requirements
This project requires Python 3.x. Dependencies are listed in the `requirements.txt` file.

## Installation
1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Navigate to the project directory:
   ```
   cd [project directory]
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration
Configure the application settings in the `config.py` file. Available settings:

- `PROTOCOL`: The protocol that server uses (default is http).
- `IP_ADDRESS`: Local IP address of the server (192.168... check it on server device with command `ifconfig`)
- `PORT`: The port on which the server will run (default is 5000).
- `NAMESPACE`: Socket path (default is "/video").

Example `config.py`:
```python
PROTOCOL = "http"
IP_ADDRESS = "192.168.0.10"
PORT = 5000
NAMESPACE = "/video"
```

## Running the Project
To run the project, execute:
```
python main.py
```