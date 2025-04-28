import rpyc
import time
# Import the server types
from rpyc.utils.server import (
    OneShotServer, 
    ForkingServer,
    ThreadedServer, 
    ThreadPoolServer
)

# Define the service exposed to clients
class MyService(rpyc.Service):
    # 'exposed_' prefix makes the method callable remotely
    def exposed_calc(self, a, b):
        """
        Simple calculation simulating some server work.
        Adds a small delay to make concurrency effects more noticeable.
        """
        print(f"Received calc request: ({a}, {b})")
        # Simulate work/delay
        time.sleep(0.01) # 10 milliseconds delay
        result = a + b
        print(f"Returning result: {result}")
        return result

    # Optional: Add a simple ping to test connection without calculation
    def exposed_ping(self):
        print("Received ping")
        return "pong"

if __name__ == "__main__":
    PORT = 18861

    # --- !!! IMPORTANT !!! ---
    # --- Uncomment only ONE of the following server types at a time ---

    # 1. OneShotServer: Handles one connection then exits
    #server_type = "OneShotServer"
    #server = OneShotServer(MyService, port=PORT)

    # 3. ThreadedServer: Spawns a new thread for each client
    #server_type = "ThreadedServer"
    #server = ThreadedServer(MyService, port=PORT)

    # 3. ThreadPoolServer: Uses a pool of threads (often most efficient)
    server_type = "ThreadPoolServer"
    server = ThreadPoolServer(MyService, port=PORT)
    # You can configure the pool size, e.g.:
    # server = ThreadPoolServer(MyService, port=PORT, nbThreads=20)


    print(f"Starting {server_type} on port {PORT}...")
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        # Ensure server resources are cleaned up if possible
        # Note: Not all servers might exit cleanly on KeyboardInterrupt alone
        if hasattr(server, 'close'):
             server.close()
        print("Server shut down.")