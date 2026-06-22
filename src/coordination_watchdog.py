import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Metrics:
    """Clear and actionable metrics for observability"""
    system_uptime: int
    integration_status: str

class CoordinationWatchdog:
    """Seamless Integration with existing observability stack"""
    def __init__(self, prometheus_url: str, grafana_url: str):
        if not prometheus_url or not grafana_url:
            raise AttributeError("Both Prometheus and Grafana URLs are required")
        self.prometheus_url = prometheus_url
        self.grafana_url = grafana_url
        self.metrics = Metrics(0, "unknown")

    def integrate_with_prometheus(self) -> bool:
        """Integrate with Prometheus without modification"""
        # Simulate integration with Prometheus
        self.metrics.system_uptime = 100
        self.metrics.integration_status = "success"
        return True

    def integrate_with_grafana(self) -> bool:
        """Integrate with Grafana without modification"""
        # Simulate integration with Grafana
        self.metrics.system_uptime = 100
        self.metrics.integration_status = "success"
        return True

    def get_metrics(self) -> Dict:
        """Get clear and actionable metrics for observability"""
        return {
            "system_uptime": self.metrics.system_uptime,
            "integration_status": self.metrics.integration_status
        }

    def configure_integration(self, prometheus_url: str, grafana_url: str) -> None:
        """Configure integration settings"""
        if not prometheus_url or not grafana_url:
            raise AttributeError("Both Prometheus and Grafana URLs are required")
        self.prometheus_url = prometheus_url
        self.grafana_url = grafana_url
