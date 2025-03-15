import threading
import time

class Process:
    def __init__(self, id, num_processes):
        self.id = id
        self.matrix_clock = [[0] * num_processes for _ in range(num_processes)]
        self.message_queue = []

    def send_message(self, receiver, network):
        self.matrix_clock[self.id][self.id] += 1  # Increment own clock
        message = (self.matrix_clock[:], self.id)
        network[receiver].receive_message(message)
        print(f"Process {self.id} sent message to Process {receiver} with matrix clock {message[0]}")

    def receive_message(self, message):
        sender_matrix, sender_id = message
        for i in range(len(self.matrix_clock)):
            for j in range(len(self.matrix_clock[i])):
                self.matrix_clock[i][j] = max(self.matrix_clock[i][j], sender_matrix[i][j])
        self.matrix_clock[self.id][self.id] += 1  # Update own clock
        print(f"Process {self.id} received message from Process {sender_id}, updated matrix clock: {self.matrix_clock}")

# Simulating Matrix Clock Algorithm
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
