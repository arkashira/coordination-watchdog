import pytest
from coordination_watchdog import CoordinationWatchdog, CoordinationEvent
import time

def test_start_coordination():
    watchdog = CoordinationWatchdog()
    agent_id = "test_agent"
    watchdog.start_coordination(agent_id)
    assert agent_id in watchdog.events

def test_end_coordination():
    watchdog = CoordinationWatchdog()
    agent_id = "test_agent"
    watchdog.start_coordination(agent_id)
    event = watchdog.end_coordination(agent_id)
    assert isinstance(event, CoordinationEvent)
    assert event.agent_id == agent_id

def test_end_coordination_before_start():
    watchdog = CoordinationWatchdog()
    agent_id = "test_agent"
    with pytest.raises(ValueError):
        watchdog.end_coordination(agent_id)

def test_coordination_latency():
    watchdog = CoordinationWatchdog()
    agent_id = "test_agent"
    start_time = time.time()
    watchdog.start_coordination(agent_id)
    watchdog.end_coordination(agent_id)
    end_time = time.time()
    latency = end_time - start_time
    assert latency < 0.005  # 5ms
