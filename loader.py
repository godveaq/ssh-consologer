import os
import sys
import subprocess
import webbrowser
import socket
import threading
import time
import json
import random
from http.server import HTTPServer, SimpleHTTPRequestHandler

class GlitchConsoleTerminal:
    def __init__(self):
        self.current_mode = "disconnected"
        self.current_target = None
        self.user_agent = ""
        self.load_user_agent()
        self.show_banner()
    
    def load_user_agent(self):
        """Load a random user agent from the JSON file"""
        try:
            with open('user_agents.json', 'r') as f:
                user_agents = json.load(f)
                self.user_agent = random.choice(user_agents)
        except FileNotFoundError:
            # Default user agent if file not found
            self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    def show_banner(self):
        """Display the Glitch Console banner"""
        banner = '''
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
        '''
        print(banner)
        print(f"User Agent: {self.user_agent}")
        print("Type 'help' for available commands")
        print("="*50)
    
    def show_help(self):
        """Display available commands"""
        help_text = """Available commands:
    help                    - Show this help message
    scan <target>           - Scan target for SSH ports
    connect <target>        - Connect to target via SSH/console
    config <type>           - Set scan configuration (aggressive/normal)
    load_user_agents        - Reload user agents
    clear                   - Clear the terminal
    exit                    - Exit the console
    """
        print(help_text)
    
    def scan_target(self, target):
        """Simulate scanning a target for SSH ports"""
        print(f"Scanning {target} for SSH ports...")
        
        # Simulate scan process
        ports = [22, 2222, 2200, 2022]
        open_ports = []
        
        for port in ports:
            print(f"Scanning port {port}...", end=" ")
            time.sleep(0.3)  # Simulate scanning delay
            
            # Randomly determine if port is open (70% chance)
            if random.random() < 0.7:
                print(f"OPEN")
                open_ports.append(port)
            else:
                print(f"CLOSED")
        
        if open_ports:
            print(f"Open SSH ports found: {open_ports}")
            return True, open_ports
        else:
            print("No SSH ports found open")
            return False, []
    
    def connect_to_target(self, target, ports):
        """Simulate connecting to a target"""
        print(f"Attempting to connect to {target} on SSH ports {ports}...")
        
        time.sleep(1)  # Simulate connection attempt
        
        # Randomly determine if connection is successful (50% chance)
        if random.random() < 0.5:
            print("ssh connect:")
            self.current_mode = "ssh"
            print(f"Connected to {target} via SSH")
            print("SSH Terminal Mode - Commands for SSH connection")
            print("Type commands. Type 'exit' to return to console")
        else:
            print("ssh-console:")
            self.current_mode = "console"
            print(f"Connected to {target} console")
            print("Console Terminal Mode - Commands for site console")
            print("Type commands. Type 'exit' to return to console")
        
        self.current_target = target
        return True
    
    def process_command(self, command):
        """Process a command in the current mode"""
        if self.current_mode == "ssh":
            # Simulate SSH command processing
            responses = {
                'ls': ['file1.txt', 'file2.txt', 'directory/', 'script.sh'],
                'pwd': ['/home/user'],
                'whoami': ['root'],
                'ps aux': ['PID TTY TIME CMD', '1 ? 00:01 init', '123 ? 00:00 sshd'],
                'uname -a': ['Linux server 5.4.0-ubuntu #1 SMP'],
                'df -h': ['Filesystem Size Used Avail Use%', '/dev/sda1 50G 20G 28G 42%'],
                'free -m': ['Mem: 4096 2048 1024 0 1024 3072']
            }
            
            if command in responses:
                for line in responses[command]:
                    print(line)
            else:
                print(f"Command not found: {command}")
        
        elif self.current_mode == "console":
            # Simulate console command processing
            responses = {
                'info': ['Site: example.com', 'IP: 192.168.1.1', 'Status: Active'],
                'status': ['System: Operational', 'Uptime: 42 days'],
                'users': ['admin', 'guest', 'testuser'],
                'files': ['index.html', 'style.css', 'script.js']
            }
            
            if command in responses:
                for line in responses[command]:
                    print(line)
            else:
                print(f"Console command: {command}")
    
    def run_ssh_terminal(self):
        """Run the SSH terminal specifically"""
        print("\n" + "="*60)
        print("SSH TERMINAL - Connected to:", self.current_target)
        print("Commands for SSH connection")
        print("Type 'exit' to return to main console")
        print("="*60)
        
        while True:
            try:
                # SSH-specific prompt
                command = input(f"ssh---> ").strip()
                
                if not command:
                    continue
                
                if command.lower() == "exit":
                    print("Exiting SSH terminal...")
                    break
                elif command.lower() == "help":
                    print("Available SSH commands: ls, pwd, whoami, ps aux, uname -a, df -h, free -m")
                else:
                    # Process SSH command
                    self.process_command_ssh(command)
            
            except KeyboardInterrupt:
                print("\nUse 'exit' to return to main console")
            except EOFError:
                print("\nExiting SSH terminal...")
                break
    
    def process_command_ssh(self, command):
        """Process SSH-specific commands"""
        responses = {
            'ls': ['file1.txt', 'file2.txt', 'directory/', 'script.sh'],
            'pwd': ['/home/user'],
            'whoami': ['root'],
            'ps aux': ['PID TTY TIME CMD', '1 ? 00:01 init', '123 ? 00:00 sshd'],
            'uname -a': ['Linux server 5.0.0-ubuntu #1 SMP'],
            'df -h': ['Filesystem Size Used Avail Use%', '/dev/sda1 50G 20G 28G 42%'],
            'free -m': ['Mem: 4096 2048 1024 0 1024 3072']
        }
        
        if command in responses:
            for line in responses[command]:
                print(line)
        else:
            print(f"bash: {command}: command not found")
    
    def run_console_terminal(self):
        """Run the console terminal specifically"""
        print("\n" + "="*60)
        print("CONSOLE TERMINAL - Connected to:", self.current_target)
        print("Commands for site console")
        print("Type 'exit' to return to main console")
        print("="*60)
        
        while True:
            try:
                # Console-specific prompt
                command = input(f"console---> ").strip()
                
                if not command:
                    continue
                
                if command.lower() == "exit":
                    print("Exiting console terminal...")
                    break
                elif command.lower() == "help":
                    print("Available console commands: info, status, users, files")
                else:
                    # Process console command
                    self.process_command_console(command)
            
            except KeyboardInterrupt:
                print("\nUse 'exit' to return to main console")
            except EOFError:
                print("\nExiting console terminal...")
                break
    
    def process_command_console(self, command):
        """Process console-specific commands"""
        responses = {
            'info': ['Site: example.com', 'IP: 192.168.1.1', 'Status: Active'],
            'status': ['System: Operational', 'Uptime: 42 days'],
            'users': ['admin', 'guest', 'testuser'],
            'files': ['index.html', 'style.css', 'script.js']
        }
        
        if command in responses:
            for line in responses[command]:
                print(line)
        else:
            print(f"Console command: {command}")
    
    def run_terminal(self):
        """Run the main terminal interface"""
        while True:
            try:
                if self.current_mode == "disconnected":
                    prompt = "glitch-console:~$ "
                    command = input(prompt).strip()
                    
                    if not command:
                        continue
                    
                    # Handle main commands
                    if command.lower() == "exit":
                        print("Goodbye!")
                        break
                    elif command.lower() == "help":
                        self.show_help()
                    elif command.lower() == "clear":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.show_banner()
                    elif command.lower() == "load_user_agents":
                        self.load_user_agent()
                        print(f"User Agent updated: {self.user_agent}")
                    elif command.lower().startswith("scan "):
                        target = command[5:].strip()
                        if target:
                            self.scan_target(target)
                        else:
                            print("Usage: scan <target>")
                    elif command.lower().startswith("connect "):
                        target = command[8:].strip()
                        if target:
                            # First scan the target
                            is_open, ports = self.scan_target(target)
                            if is_open:
                                # Randomly determine if connection is successful (50% chance)
                                if random.random() < 0.5:
                                    print("ssh connect:")
                                    print(f"Connected to {target} via SSH")
                                    # Switch to SSH terminal mode
                                    self.current_target = target
                                    self.run_ssh_terminal()
                                    self.current_mode = "disconnected"
                                    self.current_target = None
                                else:
                                    print("ssh-console:")
                                    print(f"Connected to {target} console")
                                    # Switch to console terminal mode
                                    self.current_target = target
                                    self.run_console_terminal()
                                    self.current_mode = "disconnected"
                                    self.current_target = None
                            else:
                                print("ssh-console:")
                                print(f"Connected to {target} console")
                                # Switch to console terminal mode
                                self.current_target = target
                                self.run_console_terminal()
                                self.current_mode = "disconnected"
                                self.current_target = None
                        else:
                            print("Usage: connect <target>")
                    elif command.lower().startswith("config "):
                        config_type = command[7:].strip()
                        if config_type in ["aggressive", "normal"]:
                            print(f"Configuration set to: {config_type}")
                            if config_type == "aggressive":
                                print("Aggressive scan: High thread count for faster scanning")
                            else:
                                print("Normal scan: Standard thread count for stealth")
                        else:
                            print("Usage: config <aggressive|normal>")
                    else:
                        print(f"Unknown command: {command}. Type 'help' for available commands.")
                
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit the console")
            except EOFError:
                print("\nGoodbye!")
                break

def start_server():
    """Start the HTTP server in a separate thread"""
    port = 3000
    
    # Change to the console directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create HTTP server
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    # Start server in a thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    print(f"Server started on http://localhost:{port}")
    return httpd, server_thread

def main():
    print("Choose mode:")
    print("1. Web Interface (opens in browser)")
    print("2. Terminal Interface (command line)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        print("Starting Glitch Console Web Interface...")
        print("Loading assets...")
        
        # Start the server
        httpd, server_thread = start_server()
        
        # Wait a bit for server to start
        time.sleep(1)
        
        # Open the web browser
        webbrowser.open('http://localhost:3000')
        
        print("Glitch Console is running!")
        print("Press Ctrl+C to stop the server")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()
            print("Server stopped. Goodbye!")
    elif choice == "2":
        # Run the terminal interface
        console = GlitchConsoleTerminal()
        console.run_terminal()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()