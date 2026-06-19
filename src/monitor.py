from enum import Enum

class AgentStatus(Enum):
    ONLINE = 1
    OFFLINE = 2

class Agent:
    def __init__(self, agent_id: int):
        self.agent_id = agent_id
        self.status = AgentStatus.ONLINE

class AgentMonitor:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_id: int):
        self.agents[agent_id] = Agent(agent_id)

    def remove_agent(self, agent_id: int):
        if agent_id in self.agents:
            del self.agents[agent_id]

    def update_agent_status(self, agent_id: int, status: AgentStatus):
        if agent_id in self.agents:
            self.agents[agent_id].status = status

    def get_agent_status(self, agent_id: int) -> AgentStatus:
        if agent_id in self.agents:
            return self.agents[agent_id].status
        else:
            return None

class CoordinationWatchdog:
    def __init__(self):
        self.monitor = AgentMonitor()

    def add_agent(self, agent_id: int):
        self.monitor.add_agent(agent_id)

    def remove_agent(self, agent_id: int):
        self.monitor.remove_agent(agent_id)

    def update_agent_status(self, agent_id: int, status: bool):
        self.monitor.update_agent_status(agent_id, AgentStatus.ONLINE if status else AgentStatus.OFFLINE)

    def get_agent_status(self, agent_id: int) -> bool:
        status = self.monitor.get_agent_status(agent_id)
        return status == AgentStatus.ONLINE if status else False
