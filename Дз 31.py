import queue
import threading
import time
class Server:
    def __init__(self):
        self.request_queue = queue.PriorityQueue()
        self.stats_queue = queue.Queue()

    def add_request(self, client_id, priority):
        self.request_queue.put((priority, client_id, time.time()))
        self.stats_queue.put((client_id, time.time()))

    def process_requests(self):
        while True:
            priority, client_id, timestamp = self.request_queue.get()
            print(f"Запит від клієнта {client_id} з пріоритетом {priority} оброблено о {time.strftime('%H:%M:%S', time.localtime())}")
            time.sleep(1)


server = Server()

processing_thread = threading.Thread(target=server.process_requests)
processing_thread.start()

clients = [("Client1", 2), ("Client2", 1), ("Client3", 3)]

for client_id, priority in clients:
    server.add_request(client_id, priority)
    time.sleep(0.5)
