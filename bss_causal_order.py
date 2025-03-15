import threading
import time

class Process:
    def __init__(self, id, num_processes):
        self.id = id  # Process ID
        self.vector_clock = [0] * num_processes  # Initialize vector clock
        self.message_queue = []  # Queue to store incoming messages

    def send_message(self, receiver, network):
        self.vector_clock[self.id] += 1  # Increment own clock before sending
        message = (self.vector_clock[:], self.id)  # Send a copy of the vector clock
        network[receiver].receive_message(message)
        print(f"Process {self.id} sent message to Process {receiver} with clock {message[0]}")

    def receive_message(self, message):
        sender_clock, sender_id = message
        self.vector_clock = [max(self.vector_clock[i], sender_clock[i]) for i in range(len(self.vector_clock))]
        self.vector_clock[self.id] += 1  # Update own clock after receiving
        print(f"Process {self.id} received message from Process {sender_id}, updated clock: {self.vector_clock}")

# Simulating BSS Causal Ordering
num_processes = 3
network = {i: Process(i, num_processes) for i in range(num_processes)}

# Creating a causal message order
def simulate():
    network[0].send_message(1, network)  # P0 sends to P1
    time.sleep(1)
    network[1].send_message(2, network)  # P1 sends to P2
    time.sleep(1)
    network[0].send_message(2, network)  # P0 sends to P2

# Run simulation in a separate thread
t = threading.Thread(target=simulate)
t.start()
t.join()
