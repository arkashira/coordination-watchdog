import pytest
from src.coordination_watchdog import CoordinationWatchdog, Metrics

def test_integrate_with_prometheus():
    watchdog = CoordinationWatchdog("http://prometheus", "http://grafana")
    assert watchdog.integrate_with_prometheus() == True
    assert watchdog.metrics.system_uptime == 100
    assert watchdog.metrics.integration_status == "success"

def test_integrate_with_grafana():
    watchdog = CoordinationWatchdog("http://prometheus", "http://grafana")
    assert watchdog.integrate_with_grafana() == True
    assert watchdog.metrics.system_uptime == 100
    assert watchdog.metrics.integration_status == "success"

def test_get_metrics():
    watchdog = CoordinationWatchdog("http://prometheus", "http://grafana")
    watchdog.integrate_with_prometheus()
    metrics = watchdog.get_metrics()
    assert metrics["system_uptime"] == 100
    assert metrics["integration_status"] == "success"

def test_configure_integration():
    watchdog = CoordinationWatchdog("http://prometheus", "http://grafana")
    watchdog.configure_integration("http://new_prometheus", "http://new_grafana")
    assert watchdog.prometheus_url == "http://new_prometheus"
    assert watchdog.grafana_url == "http://new_grafana"

def test_edge_case_empty_urls():
    with pytest.raises(AttributeError):
        CoordinationWatchdog("", "")
