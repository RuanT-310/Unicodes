import rpyc
import time

SERVER_HOST = "localhost"
SERVER_PORT = 18861
NUM_CALLS = 100 # Number of RPC calls to make

if __name__ == "__main__":
    conn = None
    try:
        print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}...")
        conn = rpyc.connect(SERVER_HOST, SERVER_PORT)
        print("Connected.")

        # Optional: Test connection with ping
        # pong = conn.root.ping()
        # print(f"Ping response: {pong}")

        print(f"Making {NUM_CALLS} calls to exposed_calc...")
        start_time = time.time()

        for i in range(NUM_CALLS):
            try:
                # Call the remote method
                result = conn.root.exposed_calc(i, i + 1)
                # Optional: print each result, but can slow down measurement
                # print(f"Call {i+1}/{NUM_CALLS}: Input=({i}, {i+1}), Result={result}")
            except EOFError:
                print("Server closed the connection prematurely.")
                break # Exit loop if connection lost
            except Exception as e:
                print(f"Error during call {i+1}: {e}")
                # Decide if you want to break or continue
                # break

        end_time = time.time()
        duration = end_time - start_time

        print("-" * 30)
        print(f"Single client finished.")
        print(f"{NUM_CALLS} calls took {duration:.4f} seconds")
        print(f"Average time per call: {(duration/NUM_CALLS)*1000:.4f} ms")
        print("-" * 30)

    except ConnectionRefusedError:
        print(f"Connection refused. Is the server running at {SERVER_HOST}:{SERVER_PORT}?")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            print("Closing connection.")
            conn.close()