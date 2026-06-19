import json
from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    id: int
    status: str

class AgentMonitor:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent: Agent):
        self.agents[agent.id] = agent

    def remove_agent(self, agent_id: int):
        if agent_id in self.agents:
            del self.agents[agent_id]

    def detect_failures(self) -> List[Agent]:
        failed_agents = [agent for agent in self.agents.values() if agent.status == "failed"]
        return failed_agents

    def report_failures(self) -> str:
        failed_agents = self.detect_failures()
        report = json.dumps([{"id": agent.id, "status": agent.status} for agent in failed_agents])
        return report
