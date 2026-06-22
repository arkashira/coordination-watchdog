import argparse
import json
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

@dataclass
class Event:
    id: str
    timestamp: datetime
    type: str

class Watchdog:
    def __init__(self):
        self.events = []

    def log_event(self, event_type):
        event = Event(str(uuid4()), datetime.now(), event_type)
        self.events.append(event)
        return event

    def stream_events(self):
        return self.events

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--instrument', action='store_true')
    args = parser.parse_args()
    if args.instrument:
        watchdog = Watchdog()
        watchdog.log_event('agent_start')
        watchdog.log_event('message_send')
        watchdog.log_event('message_receive')
        events = watchdog.stream_events()
        print(json.dumps([event.__dict__ for event in events]))
    else:
        print("Watchdog not instrumented")

if __name__ == '__main__':
    main()
