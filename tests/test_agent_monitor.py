import pytest
from datetime import datetime, timedelta
from agent_monitor import AgentMonitor

@pytest.fixture
def monitor():
    return AgentMonitor()

def test_register_agent(monitor):
    monitor.register_agent("agent1")
    assert "agent1" in monitor.agents

def test_update_heartbeat(monitor):
    monitor.register_agent("agent1")
    monitor.update_heartbeat("agent1")
    assert monitor.agents["agent1"].last_heartbeat > datetime.now() - timedelta(seconds=1)

def test_detect_failures(monitor):
    monitor.register_agent("agent1")
    monitor.register_agent("agent2")
    monitor.update_heartbeat("agent1")
    # simulate failure
    monitor.agents["agent2"].last_heartbeat = datetime.now() - timedelta(minutes=2)
    failed_agents = monitor.detect_failures()
    assert "agent2" in failed_agents
    assert "agent1" not in failed_agents

def test_report_status(monitor):
    monitor.register_agent("agent1")
    monitor.register_agent("agent2")
    monitor.update_heartbeat("agent1")
    # simulate failure
    monitor.agents["agent2"].last_heartbeat = datetime.now() - timedelta(minutes=2)
    status = monitor.report_status()
    assert status["agent1"] == "OK"
    assert status["agent2"] == "FAILED"
