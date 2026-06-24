import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

@dataclass
class Agent:
    id: str
    last_heartbeat: datetime

class AgentMonitor:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def register_agent(self, agent_id: str):
        self.agents[agent_id] = Agent(agent_id, datetime.now())

    def update_heartbeat(self, agent_id: str):
        if agent_id in self.agents:
            self.agents[agent_id].last_heartbeat = datetime.now()

    def detect_failures(self) -> List[str]:
        failed_agents = []
        for agent in self.agents.values():
            if datetime.now() - agent.last_heartbeat > timedelta(minutes=1):
                failed_agents.append(agent.id)
        return failed_agents

    def report_status(self):
        status = {}
        for agent_id, agent in self.agents.items():
            status[agent_id] = "OK" if datetime.now() - agent.last_heartbeat < timedelta(minutes=1) else "FAILED"
        return status
