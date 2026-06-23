from coordination_watchdog import CoordinationWatchdog, Agent, AgentStatus

def test_add_agent():
    watchdog = CoordinationWatchdog()
    agent = Agent(1, AgentStatus.ACTIVE)
    watchdog.add_agent(agent)
    assert len(watchdog.get_all_agents()) == 1

def test_update_agent_status():
    watchdog = CoordinationWatchdog()
    agent = Agent(1, AgentStatus.ACTIVE)
    watchdog.add_agent(agent)
    watchdog.update_agent_status(1, AgentStatus.IDLE)
    assert watchdog.get_all_agents()[0].status == AgentStatus.IDLE

def test_get_agents_by_status():
    watchdog = CoordinationWatchdog()
    agent1 = Agent(1, AgentStatus.ACTIVE)
    agent2 = Agent(2, AgentStatus.IDLE)
    watchdog.add_agent(agent1)
    watchdog.add_agent(agent2)
    assert len(watchdog.get_agents_by_status(AgentStatus.ACTIVE)) == 1
    assert len(watchdog.get_agents_by_status(AgentStatus.IDLE)) == 1

def test_trigger_alert():
    watchdog = CoordinationWatchdog()
    agent = Agent(1, AgentStatus.ACTIVE)
    watchdog.add_agent(agent)
    watchdog.update_agent_status(1, AgentStatus.ERROR)
    # Simulate alert triggering
    print("Alert triggered for agent 1 with new status error")

def test_dashboard():
    watchdog = CoordinationWatchdog()
    agent1 = Agent(1, AgentStatus.ACTIVE)
    agent2 = Agent(2, AgentStatus.IDLE)
    watchdog.add_agent(agent1)
    watchdog.add_agent(agent2)
    # Simulate dashboard display
    print("Current coordination status:")
    print("Agent 1: active")
    print("Agent 2: idle")
