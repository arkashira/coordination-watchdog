import pytest
import sys
sys.path.insert(0, './src')

from monitor import CoordinationWatchdog, AgentStatus

def test_coordination_watchdog_add_agent():
    watchdog = CoordinationWatchdog()
    watchdog.add_agent(1)
    assert watchdog.monitor.agents[1].status == AgentStatus.ONLINE

def test_coordination_watchdog_remove_agent():
    watchdog = CoordinationWatchdog()
    watchdog.add_agent(1)
    watchdog.remove_agent(1)
    assert 1 not in watchdog.monitor.agents

def test_coordination_watchdog_update_agent_status():
    watchdog = CoordinationWatchdog()
    watchdog.add_agent(1)
    watchdog.update_agent_status(1, False)
    assert watchdog.monitor.agents[1].status == AgentStatus.OFFLINE

def test_coordination_watchdog_get_agent_status():
    watchdog = CoordinationWatchdog()
    watchdog.add_agent(1)
    assert watchdog.get_agent_status(1) == True
    watchdog.update_agent_status(1, False)
    assert watchdog.get_agent_status(1) == False
