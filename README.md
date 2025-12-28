# Glitch Console

A terminal application that allows connecting to SSH and console interfaces of target systems.

## Installation

1. Clone or download this repository to your local machine
2. Make sure you have Python 3.x installed on your system
3. Install required dependencies (if any):
   ```bash
   npm install  # if you want to use the Node.js server
   ```
4. The application can be run in two ways:
   - Web Interface (requires Node.js): `node server.js` or `npm start`
   - Terminal Interface (Python): `python loader.py`

## Features

- Animated loading screen with typing effect
- User agent randomization with display
- Target input for URL or IP address
- Configurable scan settings (aggressive vs normal)
- SSH port scanning functionality
- Dual connection modes:
  - SSH connection (when SSH port is accessible)
  - Console connection (when SSH is not accessible)
- Real-time console output with command history
- Support for both SSH commands (Linux) and console commands (JS-like)

## How to Use

1. Enter a target URL or IP address
2. Select a scan configuration (aggressive for fast scanning, normal for stealth)
3. The application will scan for SSH port (22, 2222, 2200, 2022)
4. If SSH is accessible, you'll see "ssh connect:" prompt
5. If SSH is not accessible, you'll connect to the console with "ssh-console:" prompt
6. Enter commands in the console input area

## Configuration Files

- `user_agents.json`: Contains list of user agents for random selection
- `aggressive_config.json`: High-thread configuration for fast scanning
- `normal_config.json`: Standard configuration for stealth scanning

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Backend: C++ for SSH connection logic (mock implementation provided)
- Launcher: Python script (loader.py) to run the application
- Configuration: JSON files for flexible settings
- Animation: CSS animations and JavaScript for loading effects

## Backend Implementation

The C++ backend (in `backend.cpp`) contains:
- SSH port scanning logic
- Connection attempt functionality
- Command execution simulation
- Configurable scan parameters

## How It Works

The Glitch Console application operates in two main modes:

1. **Web Interface Mode**: Serves the HTML/CSS/JS application through a local web server, providing a graphical terminal interface in your browser

2. **Terminal Interface Mode**: A Python-based command-line interface that simulates SSH and console connections

The application first scans for open SSH ports (22, 2222, 2200, 2022) on the target system. If an SSH port is accessible, it attempts to establish an SSH connection. If SSH is not accessible, it connects to the site's console interface.

## What It Does

- Scans target systems for open SSH ports
- Establishes SSH connections when possible
- Provides console access when SSH is not available
- Simulates Linux command execution in SSH mode
- Simulates web console commands in console mode
- Uses configurable scan settings (aggressive vs normal)
- Randomizes user agents for requests

## Running the Application

You can run the application in several ways:

1. Using the Python loader: `python loader.py`
2. Using Node.js server: `node server.js` then open http://localhost:3000
3. Using npm: `npm start` then open http://localhost:3000

## Usage Examples

### Terminal Interface Mode:

```
Choose mode:
1. Web Interface (opens in browser)
2. Terminal Interface (command line)
Enter choice (1 or 2): 2

     _____     ____         ____  _________________      _____    ____   ____ 
  ___|\    \   |    |       |    |/                 \ ___|\    \  |    | |    |
 /    /\    \  |    |       |    |\______     ______//    /\    \ |    | |    |
|    |  |____| |    |       |    |   \( /    /  )/  |    |  |    ||    |_|    |
|    |    ____ |    |  ____ |    |    ' |   |   '   |    |  |____||    .-.    |
|    |   |    ||    | |    ||    |      |   |       |    |   ____ |    | |    |
|    |   |_,  ||    | |    ||    |     /   //       |    |  |    ||    | |    |
|\ ___\___/  /||____|/____/||____|    /___//        |\ ___\/    /||____| |____|
| |   /____ / ||    |     |||    |   |`   |         | |   /____/ ||    | |    |
 \|___|    | / |____|_____|/|____|   |____|          \|___|    | /|____| |____|
   \( |____|/    \(    )/     \(       \(              \( |____|/   \(     )/  
    '   )/        '    '       '        '               '   )/       '     '   
           GLİTCH CONSOLE v1.0

User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Type 'help' for available commands
==================================================
glitch-console:~$ connect example.com
Scanning example.com for SSH ports...
Scanning port 22... OPEN
Scanning port 2222... CLOSED
Scanning port 2200... CLOSED
Scanning port 2022... CLOSED
Open SSH ports found: [22]
Attempting to connect to example.com on SSH ports [22]...
ssh connect:
Connected to example.com via SSH
SSH Terminal Mode - Commands for SSH connection
Type commands. Type 'exit' to return to console

==================================================
SSH TERMINAL - Connected to: example.com
Commands for SSH connection
Type 'exit' to return to main console
==================================================
ssh---> ls
file1.txt
file2.txt
directory/
script.sh
ssh---> exit
Exiting SSH terminal...
```

### Web Interface Mode:

1. Select option 1 when prompted
2. The application will start a local server and open in your browser
3. Enter a target URL/IP in the input field
4. Choose a scan configuration (aggressive or normal)
5. The application will scan and connect accordingly

## License

MIT License