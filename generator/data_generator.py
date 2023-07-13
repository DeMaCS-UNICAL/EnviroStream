#!/usr/bin/python
import json
import socket
import argparse
import yaml
from pymongo import MongoClient
from dateutil import parser
import datetime
import time
import sys


class Receiver:
    def __init__(self):
        print("new receiver")

    def send_event(self, event):
        print(event)


class MongoDBReceiver(Receiver):
    def __init__(self, collection):
        super().__init__()
        self.collection = collection

    def send_event(self, event):
        self.collection.insert_one(event)


class TCPSocketReceiver:
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def send_event(self, event):
        to_send = json.dumps(event)
        self.connection.sendall(to_send.encode())


def get_database(connection_string="mongodb://localhost:27017/"):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = connection_string

    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    print("[INFO]", client)
    # Create the database
    return client


def simulate_original_arrival(receiver, j_obj, start=None, end=None):
    event = find_start(0, j_obj, start)

    prev_timestamp = parser.parse(j_obj[event]['timestamp']).timestamp()
    # collection.insert_one(j_obj[event])
    receiver.send_event(j_obj[event])

    print("[INFO] sent event:", event)
    t_freq = 0
    d = event + 1

    if end is not None:
        end_datetime = parser.parse(end)
        check_validity(end_datetime, start)
    else:
        end_datetime = None

    for d in range(event + 1, len(j_obj)):
        event_timestamp = parser.parse(j_obj[d]['timestamp'])
        if end_datetime is not None:
            if event_timestamp > end_datetime:
                d -= 1
                break
        crr_timestamp = event_timestamp.timestamp()
        freq = crr_timestamp - prev_timestamp
        # print(freq)
        t_freq += freq
        # freq = 1
        print(f"[INFO] wait for:{freq}s")
        time.sleep(freq)
        # collection.insert_one(j_obj[d])
        receiver.send_event(j_obj[d])
        print("[INFO] sent event:", d)
        prev_timestamp = crr_timestamp
        # print(d)
    avg_freq = t_freq / d
    print("[INFO] avg frequency", avg_freq)


def simulate_event_arrival(receiver, j_obj, freq, start=None, end=None):
    event = find_start(0, j_obj, start)
    receiver.send_event(j_obj[event])
    # collection.insert_one(j_obj[event])
    print("[INFO] sent event:", event)

    d = event + 1

    if end is not None:
        end_datetime = parser.parse(end)
        check_validity(end_datetime, start)
    else:
        end_datetime = None

    for d in range(event + 1, len(j_obj)):
        event_timestamp = parser.parse(j_obj[d]['timestamp'])
        if end_datetime is not None:
            if event_timestamp > end_datetime:
                d -= 1
                break
        print("[INFO] wait for:", freq)
        time.sleep(freq)
        receiver.send_event(j_obj[d])
        # collection.insert_one(j_obj[d])
        print("[INFO] sent event:", d)
        # print(d)
    # print("[INFO] events sent: ", d)


def check_validity(end_datetime, start):
    if start is None:
        return
    if end_datetime < parser.parse(start):
        print("[ERROR] invalid date range")
        sys.exit(1)


def find_start(event, j_obj, start):
    if start is not None:
        found_start = False
        start_datetime = parser.parse(start)
        for event in range(0, len(j_obj)):
            event_timestamp = parser.parse(j_obj[event]['timestamp'])
            if event_timestamp >= start_datetime:
                found_start = True
                break
        if not found_start:
            print("[ERROR] invalid date range")
            sys.exit(1)
    return event


def get_interval(data_loaded):
    if "from" in data_loaded:
        start = data_loaded["from"]
    else:
        start = None
    if "to" in data_loaded:
        end = data_loaded["to"]
    else:
        end = None
    return end, start


def publish_to_mongodb(config_file):
    with open(config_file, 'r') as config:
        data_loaded = yaml.safe_load(config)
        print(data_loaded)

        # Get the database
        db = get_database(data_loaded["connection_string"])

        # Get the collection
        collection = db[data_loaded["database_name"]][data_loaded["collection_name"]]
        print("[INFO]", collection)
        # Remove previous insertion
        x = collection.delete_many({})
        print("[INFO] clean collection")
        print("[INFO]", x.deleted_count, " documents deleted.")
        receiver = MongoDBReceiver(collection)
        # Read the log
        with open(data_loaded["log_path"], 'r') as data:
            j_obj = json.load(data)
            end, start = get_interval(data_loaded)
            if data_loaded["frequency"] == "original":
                simulate_original_arrival(receiver, j_obj, start, end)
            else:
                freq = float(data_loaded["frequency"])
                simulate_event_arrival(receiver, j_obj, freq, start, end)


def publish_to_stdout(config_file):
    with open(config_file, 'r') as config:
        data_loaded = yaml.safe_load(config)
        # print(data_loaded)
        # Read the log
        with open(data_loaded["log_path"], 'r') as data:
            j_obj = json.load(data)
            end, start = get_interval(data_loaded)
            if end is not None:
                end_datetime = parser.parse(end)
                check_validity(end_datetime, start)
            else:
                end_datetime = None
            event = find_start(0, j_obj, start)
            selection_result = []
            for d in range(event, len(j_obj)):
                event_timestamp = parser.parse(j_obj[d]['timestamp'])
                if end_datetime is not None:
                    if event_timestamp > end_datetime:
                        break
                selection_result.append(j_obj[d])
            json.dump(selection_result, indent=4, fp=sys.stdout)


def publish_to_socket(config_file):
    with open(config_file, 'r') as config:
        data_loaded = yaml.safe_load(config)
        print(data_loaded)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((data_loaded["host"], int(data_loaded["port"])))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('[INFO] Connected by', addr)
                with open(data_loaded["log_path"], 'r') as data:
                    j_obj = json.load(data)
                    end, start = get_interval(data_loaded)
                    receiver = TCPSocketReceiver(conn)
                    if data_loaded["frequency"] == "original":
                        simulate_original_arrival(receiver, j_obj, start, end)
                    else:
                        freq = float(data_loaded["frequency"])
                        simulate_event_arrival(receiver, j_obj, freq, start, end)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='A customizable data source simulator')

    arg_parser.add_argument('-o', '--output', metavar='output',
                            required=True, dest='output',
                            action='store',
                            help='where to publish the extracted events',
                            choices={'mongodb', 'socket', 'stdout'})
    arg_parser.add_argument('-c', '--config-file', metavar='path/to/your/config/file.yaml',
                            required=True, dest='config_file',
                            action='store',
                            help='path to the yaml configuration file')
    args = arg_parser.parse_args()
    print(args.output)
    if args.output == "mongodb":
        publish_to_mongodb(args.config_file)
    elif args.output == "stdout":
        publish_to_stdout(args.config_file)
    elif args.output == "socket":
        publish_to_socket(args.config_file)
    else:
        print("[ERROR]")
