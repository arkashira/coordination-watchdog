import time
from dataclasses import dataclass
from typing import Dict

@dataclass
class CoordinationEvent:
    agent_id: str
    start_time: float
    end_time: float

class CoordinationWatchdog:
    def __init__(self):
        self.events = {}

    def start_coordination(self, agent_id: str) -> None:
        self.events[agent_id] = time.time()

    def end_coordination(self, agent_id: str) -> CoordinationEvent:
        if agent_id not in self.events:
            raise ValueError("Coordination not started for agent")
        start_time = self.events.pop(agent_id)
        end_time = time.time()
        event = CoordinationEvent(agent_id, start_time, end_time)
        return event
