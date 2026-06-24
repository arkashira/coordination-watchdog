# Agent Monitor
A basic agent monitoring system to detect coordination layer failures.

## Usage
1. Register an agent using `AgentMonitor.register_agent()`.
2. Update the agent's heartbeat using `AgentMonitor.update_heartbeat()`.
3. Detect failed agents using `AgentMonitor.detect_failures()`.
4. Report the status of all agents using `AgentMonitor.report_status()`.
