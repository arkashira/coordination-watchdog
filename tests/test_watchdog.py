import pytest
from datetime import datetime, timedelta
from watchdog import Watchdog, Event

def test_log_event():
    watchdog = Watchdog()
    event = watchdog.log_event('agent_start')
    assert event.type == 'agent_start'
    assert event.timestamp < datetime.now() + timedelta(seconds=1)
    assert event.id

def test_stream_events():
    watchdog = Watchdog()
    event1 = watchdog.log_event('agent_start')
    event2 = watchdog.log_event('message_send')
    events = watchdog.stream_events()
    assert len(events) == 2
    assert events[0].id == event1.id
    assert events[1].id == event2.id

def test_log_event_edge_case():
    watchdog = Watchdog()
    event = watchdog.log_event('')
    assert event.type == ''

def test_stream_events_edge_case():
    watchdog = Watchdog()
    events = watchdog.stream_events()
    assert len(events) == 0
