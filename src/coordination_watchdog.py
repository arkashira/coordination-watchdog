import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class AgentStatus(Enum):
    ACTIVE = "active"
    IDLE = "idle"
    ERROR = "error"

@dataclass
class Agent:
    id: int
    status: AgentStatus

class CoordinationWatchdog:
    def __init__(self):
        self.agents: Dict[int, Agent] = {}
        self.status_filters: Dict[AgentStatus, List[int]] = {status: [] for status in AgentStatus}

    def add_agent(self, agent: Agent):
        self.agents[agent.id] = agent
        self.status_filters[agent.status].append(agent.id)

    def update_agent_status(self, agent_id: int, new_status: AgentStatus):
        if agent_id in self.agents:
            old_status = self.agents[agent_id].status
            self.agents[agent_id].status = new_status
            self.status_filters[old_status].remove(agent_id)
            self.status_filters[new_status].append(agent_id)
        else:
            raise ValueError("Agent not found")

    def get_agents_by_status(self, status: AgentStatus) -> List[Agent]:
        return [self.agents[agent_id] for agent_id in self.status_filters[status]]

    def get_all_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def trigger_alert(self, agent_id: int, new_status: AgentStatus):
        # Simulate alert triggering
        print(f"Alert triggered for agent {agent_id} with new status {new_status}")

    def dashboard(self):
        # Simulate dashboard display
        print("Current coordination status:")
        for agent in self.get_all_agents():
            print(f"Agent {agent.id}: {agent.status.value}")
