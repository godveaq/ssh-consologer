// Glitch Console Application
class GlitchConsole {
    constructor() {
        this.userAgent = '';
        this.currentConnection = null;
        this.connectionStatus = 'disconnected';
        this.selectedConfig = null;
        
        this.initializeApp();
    }
    
    async initializeApp() {
        // Show loading screen with animation
        this.animateLoading();
        
        // Load user agent
        await this.loadRandomUserAgent();
        
        // Initialize UI elements
        this.setupEventListeners();
        
        // Hide loading screen and show main app after delay
        setTimeout(() => {
            document.getElementById('loading-screen').classList.add('hidden');
            document.getElementById('main-app').classList.remove('hidden');
        }, 3000);
    }
    
    animateLoading() {
        const loadingProgress = document.getElementById('loading-progress');
        const loadingStatus = document.getElementById('loading-status');
        
        const steps = [
            { percent: 10, text: 'Loading assets...' },
            { percent: 30, text: 'Initializing core modules...' },
            { percent: 50, text: 'Loading configurations...' },
            { percent: 70, text: 'Setting up connections...' },
            { percent: 90, text: 'Finalizing setup...' },
            { percent: 100, text: 'Ready!' }
        ];
        
        let stepIndex = 0;
        
        const progressInterval = setInterval(() => {
            if (stepIndex < steps.length) {
                const step = steps[stepIndex];
                loadingProgress.style.width = `${step.percent}%`;
                loadingStatus.textContent = step.text;
                stepIndex++;
            } else {
                clearInterval(progressInterval);
            }
        }, 400);
    }
    
    async loadRandomUserAgent() {
        try {
            const response = await fetch('user_agents.json');
            const userAgents = await response.json();
            
            // Select a random user agent
            this.userAgent = userAgents[Math.floor(Math.random() * userAgents.length)];
            
            // Update UI
            document.getElementById('current-user-agent').textContent = this.userAgent;
        } catch (error) {
            console.warn('Failed to load user agents, using default:', error);
            this.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
            document.getElementById('current-user-agent').textContent = this.userAgent;
        }
    }
    
    setupEventListeners() {
        // Connect button
        document.getElementById('connect-btn').addEventListener('click', () => {
            this.handleConnect();
        });
        
        // Enter key in target input
        document.getElementById('target-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleConnect();
            }
        });
        
        // Console command input
        document.getElementById('console-command').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.executeConsoleCommand();
            }
        });
        
        // Clear console button
        document.getElementById('clear-console').addEventListener('click', () => {
            this.clearConsole();
        });
        
        // Config options
        document.querySelectorAll('.config-option').forEach(option => {
            option.addEventListener('click', (e) => {
                this.selectConfig(e.target.closest('.config-option').dataset.config);
            });
        });
    }
    
    handleConnect() {
        const target = document.getElementById('target-input').value.trim();
        
        if (!target) {
            this.addConsoleMessage('Please enter a URL or IP address', 'error-message');
            return;
        }
        
        this.addConsoleMessage(`Attempting to connect to: ${target}`, 'info-message');
        
        // Show config selector
        document.getElementById('config-selector').classList.remove('hidden');
    }
    
    async selectConfig(configType) {
        this.selectedConfig = configType;
        
        // Update UI to show selected option
        document.querySelectorAll('.config-option').forEach(option => {
            option.classList.remove('selected');
        });
        
        document.querySelector(`[data-config="${configType}"]`).classList.add('selected');
        
        this.addConsoleMessage(`Selected configuration: ${configType}`, 'info-message');
        
        // Load the selected configuration
        await this.loadConfiguration(configType);
        
        // Simulate connection attempt after config selection
        setTimeout(() => {
            this.attemptSSHConnection();
        }, 1000);
    }
    
    async loadConfiguration(configType) {
        try {
            const response = await fetch(`${configType}_config.json`);
            const config = await response.json();
            
            this.addConsoleMessage(`Loaded config: ${config.name} (${config.threads} threads)`, 'info-message');
            
            // Store config for later use
            this.currentConfig = config;
        } catch (error) {
            console.error('Failed to load config:', error);
            this.addConsoleMessage(`Failed to load ${configType} config, using defaults`, 'error-message');
            
            // Use default config
            this.currentConfig = {
                name: configType,
                threads: configType === 'aggressive' ? 100 : 10,
                timeout: configType === 'aggressive' ? 5000 : 10000,
                retries: configType === 'aggressive' ? 3 : 2
            };
        }
    }
    
    async attemptSSHConnection() {
        this.addConsoleMessage('Scanning for SSH port...', 'info-message');
        
        // Simulate port scanning
        setTimeout(() => {
            const sshPortOpen = Math.random() > 0.3; // 70% chance of SSH being open
            
            if (sshPortOpen) {
                this.addConsoleMessage('SSH port found open', 'success-message');
                this.addConsoleMessage('ssh connect:', 'connection-success');
                
                // Update prompt to SSH console
                document.getElementById('console-prompt').textContent = 'ssh-console:~$ ';
                this.connectionStatus = 'connected';
                
                this.addConsoleMessage('Connected to SSH console. Type commands below.', 'info-message');
            } else {
                this.addConsoleMessage('SSH port not accessible', 'error-message');
                this.addConsoleMessage('Connecting to console...', 'info-message');
                
                // Update prompt to console
                document.getElementById('console-prompt').textContent = 'console:~$ ';
                this.connectionStatus = 'console';
                
                this.addConsoleMessage('Connected to site console. Type commands below.', 'info-message');
            }
        }, 2000);
    }
    
    executeConsoleCommand() {
        const commandInput = document.getElementById('console-command');
        const command = commandInput.value.trim();
        
        if (!command) return;
        
        // Add command to console
        this.addConsoleMessage(`$ ${command}`, 'command-input');
        
        // Clear input
        commandInput.value = '';
        
        // Process command based on connection type
        if (this.connectionStatus === 'connected') {
            this.processSSHCommand(command);
        } else if (this.connectionStatus === 'console') {
            this.processConsoleCommand(command);
        } else {
            this.addConsoleMessage('Not connected to any system', 'error-message');
        }
    }
    
    processSSHCommand(command) {
        // Simulate SSH command processing
        const responses = {
            'ls': ['file1.txt', 'file2.txt', 'directory/', 'script.sh'],
            'pwd': ['/home/user'],
            'whoami': ['root'],
            'ps aux': ['PID TTY TIME CMD', '1 ? 00:00:01 init', '123 ? 00:00:00 sshd'],
            'uname -a': ['Linux server 5.4.0-ubuntu #1 SMP'],
            'df -h': ['Filesystem Size Used Avail Use%', '/dev/sda1 50G 20G 28G 42%'],
            'free -m': ['Mem: 4096 2048 1024 0 1024 3072']
        };
        
        if (responses[command]) {
            responses[command].forEach(line => {
                this.addConsoleMessage(line, 'command-output');
            });
        } else {
            this.addConsoleMessage(`Command not found: ${command}`, 'error-message');
        }
    }
    
    processConsoleCommand(command) {
        // Simulate console command processing
        const responses = {
            'help': ['Available commands: info, status, users, files'],
            'info': ['Site: example.com', 'IP: 192.168.1.1', 'Status: Active'],
            'status': ['System: Operational', 'Uptime: 42 days'],
            'users': ['admin', 'guest', 'testuser'],
            'files': ['index.html', 'style.css', 'script.js']
        };
        
        if (responses[command]) {
            responses[command].forEach(line => {
                this.addConsoleMessage(line, 'command-output');
            });
        } else {
            this.addConsoleMessage(`Console command: ${command}`, 'command-output');
        }
    }
    
    addConsoleMessage(message, className = '') {
        const consoleOutput = document.getElementById('console-output');
        const lineElement = document.createElement('div');
        lineElement.className = `console-line ${className}`;
        lineElement.textContent = message;
        consoleOutput.appendChild(lineElement);
        
        // Scroll to bottom
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }
    
    clearConsole() {
        const consoleOutput = document.getElementById('console-output');
        consoleOutput.innerHTML = '';
        this.addConsoleMessage('Console cleared', 'info-message');
    }
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new GlitchConsole();
});