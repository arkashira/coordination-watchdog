from agent_monitor import Agent, AgentMonitor

def test_add_agent():
    monitor = AgentMonitor()
    agent = Agent(1, "active")
    monitor.add_agent(agent)
    assert agent.id in monitor.agents

def test_remove_agent():
    monitor = AgentMonitor()
    agent = Agent(1, "active")
    monitor.add_agent(agent)
    monitor.remove_agent(agent.id)
    assert agent.id not in monitor.agents

def test_detect_failures():
    monitor = AgentMonitor()
    agent1 = Agent(1, "active")
    agent2 = Agent(2, "failed")
    monitor.add_agent(agent1)
    monitor.add_agent(agent2)
    failed_agents = monitor.detect_failures()
    assert len(failed_agents) == 1
    assert failed_agents[0].id == 2

def test_report_failures():
    monitor = AgentMonitor()
    agent1 = Agent(1, "active")
    agent2 = Agent(2, "failed")
    monitor.add_agent(agent1)
    monitor.add_agent(agent2)
    report = monitor.report_failures()
    assert report == '[{"id": 2, "status": "failed"}]'

def test_report_no_failures():
    monitor = AgentMonitor()
    agent1 = Agent(1, "active")
    agent2 = Agent(2, "active")
    monitor.add_agent(agent1)
    monitor.add_agent(agent2)
    report = monitor.report_failures()
    assert report == '[]'
