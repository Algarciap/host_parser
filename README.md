# Host Parser
This host parser tool is build to find which hosts are connected to a specific host during a given time.

## Setup
Follow these instructions to set up Host Parser locally.

### Clone the repo
```bash
git clone https://github.com/Algarciap/host_parser.git
```

In order to make Host Parser work, be sure you have Python installed as well as the Pandas library.

## How does it work?
You will need to:
- Have your `.log` file in the root directory.
    - There is currently an `examples.log` file in the root directory referenced also at `host_parser.py`. Be sure you change that for your desired file.
- Launch the program via terminal to `python main.py`.
- Fill the inputs with the requested information.

And then... it will show you the results!

## Project under development -- Next iterations
1. Add validations for the date format.
2. Add tests.
3. Add inputs, host and file name in the script call.
4. Create a container in Docker for continuous execution in order to parse previously written logs and terminate or collect input from a new log file.