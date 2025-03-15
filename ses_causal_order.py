import threading
import time

class Process:
    def __init__(self, id, num_processes):
        self.id = id
        self.interval = [id * 5, (id * 5) + 5]  # Assign an interval [start, end]
        self.message_queue = []

    def send_message(self, receiver, network):
        message = (self.interval[:], self.id)
        network[receiver].receive_message(message)
        print(f"Process {self.id} sent message to Process {receiver} with interval {self.interval}")

    def receive_message(self, message):
        sender_interval, sender_id = message
        if sender_interval[1] < self.interval[0]:  # Check causal order
            self.interval[0] = sender_interval[1]  # Adjust interval start
        print(f"Process {self.id} received message from Process {sender_id}, updated interval: {self.interval}")

# Simulating SES Algorithm
num_processes = 3
network = {i: Process(i, num_processes) for i in range(num_processes)}

def simulate():
    network[0].send_message(1, network)
    time.sleep(1)
    network[1].send_message(2, network)
    time.sleep(1)
    network[0].send_message(2, network)

# Run simulation
t = threading.Thread(target=simulate)
t.start()
t.join()
