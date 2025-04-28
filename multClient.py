import rpyc
import time
import threading

SERVER_HOST = "localhost"
SERVER_PORT = 18861
NUM_CLIENTS = 10  # Number of concurrent clients to simulate
CALLS_PER_CLIENT = 100 # Number of RPC calls each client makes

# List to store thread results (optional, e.g., durations)
results = []
results_lock = threading.Lock()

def run_client_thread(client_id):
    """Function executed by each client thread."""
    conn = None
    thread_start_time = time.time()
    duration = -1 # Default duration if error occurs before timing ends
    status = "ERROR"

    try:
        # print(f"[Client {client_id}] Connecting...")
        conn = rpyc.connect(SERVER_HOST, SERVER_PORT)
        # print(f"[Client {client_id}] Connected.")

        call_start_time = time.time() # Time just the calls

        for i in range(CALLS_PER_CLIENT):
            try:
                result = conn.root.exposed_calc(client_id * 1000 + i, i) # Unique inputs
                # Optional: print(f"[Client {client_id}] Call {i+1} result: {result}")
            except EOFError:
                print(f"[Client {client_id}] Server closed connection during call {i+1}.")
                status = "EOFError"
                break # Stop this client's calls
            except Exception as e_call:
                 print(f"[Client {client_id}] Error during call {i+1}: {e_call}")
                 status = "CallError"
                 # Decide whether to break or continue
                 break

        call_end_time = time.time()
        if status != "EOFError" and status != "CallError":
            status = "OK" # Mark as OK if loop completed without specific errors

        duration = call_end_time - call_start_time # Measure call loop duration

    except ConnectionRefusedError:
        print(f"[Client {client_id}] Connection refused.")
        status = "ConnectionRefused"
    except Exception as e_conn:
        print(f"[Client {client_id}] Connection or setup error: {e_conn}")
        status = "SetupError"
    finally:
        if conn:
            # print(f"[Client {client_id}] Closing connection.")
            conn.close()

        thread_end_time = time.time()
        total_thread_time = thread_end_time - thread_start_time

        # Safely store results
        with results_lock:
            results.append({
                "id": client_id,
                "status": status,
                "call_duration": duration if status == "OK" else -1,
                "total_thread_time": total_thread_time
            })
        #print(f"[Client {client_id}] Finished. Status: {status}, Call Duration: {duration:.4f}s")


if __name__ == "__main__":
    print(f"Starting {NUM_CLIENTS} concurrent clients, each making {CALLS_PER_CLIENT} calls...")
    threads = []
    overall_start_time = time.time()

    # Create and start threads
    for i in range(NUM_CLIENTS):
        thread = threading.Thread(target=run_client_thread, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    overall_end_time = time.time()
    total_duration = overall_end_time - overall_start_time
    print("-" * 40)
    print("All clients finished.")
    print(f"Total execution time for {NUM_CLIENTS} clients: {total_duration:.4f} seconds")
    print("-" * 40)

    # --- Analysis of Results ---
    successful_clients = [r for r in results if r["status"] == "OK"]
    failed_clients = [r for r in results if r["status"] != "OK"]

    print(f"Successful clients: {len(successful_clients)}")
    print(f"Failed clients: {len(failed_clients)}")

    if successful_clients:
        avg_call_duration = sum(r["call_duration"] for r in successful_clients) / len(successful_clients)
        max_call_duration = max(r["call_duration"] for r in successful_clients)
        min_call_duration = min(r["call_duration"] for r in successful_clients)
        print("\nStatistics for Successful Clients:")
        print(f"  Average call loop duration: {avg_call_duration:.4f} seconds")
        print(f"  Min call loop duration:     {min_call_duration:.4f} seconds")
        print(f"  Max call loop duration:     {max_call_duration:.4f} seconds")

    if failed_clients:
        print("\nFailure Summary:")
        # Count failures by type
        failure_counts = {}
        for r in failed_clients:
            failure_counts[r["status"]] = failure_counts.get(r["status"], 0) + 1
        for status, count in failure_counts.items():
            print(f"  {status}: {count} clients")
    print("-" * 40)
    