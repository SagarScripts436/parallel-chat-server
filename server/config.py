"""
Server Configuration File
Modify these values if needed
"""

# ===============================
# Network Configuration
# ===============================

HOST = "0.0.0.0"      # Accept connections from any IP
PORT = 5000           # Server port number
BUFFER_SIZE = 1024    # Maximum message size (bytes)

# ===============================
# Server Behavior Settings
# ===============================

MAX_CONNECTIONS = 10          # Maximum number of simultaneous clients
WELCOME_MESSAGE = "Welcome to the Parallel Chat Server!\n"
DISCONNECT_MESSAGE = "You have been disconnected from the server.\n"

# ===============================
# Logging Configuration
# ===============================

ENABLE_LOGGING = True
LOG_FILE = "server.log"