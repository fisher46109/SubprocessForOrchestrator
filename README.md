# Subprocess for orchestrator

## This is an example "empty" program demonstrating the usage of the AgentHandler class in any bot to enable safe program shutdown at a specific point, sending information to the agent about program start and execution results.

### Usage in the program:
1. Place the module agent_handler.py in the project folder.
2. Import the module:
  ``` python
  from agent_handler import AgentHandler
  ```
3. Create an instance of the AgentHandler class (an information about the bot's start is sent to the Agent during initialization).
  ``` python
  agent = AgentHandler()
  ```
4. At the point where certain program logic ends and a safe shutdown point may be set (after the stop command), include a condition check:
  ``` python
  if agent.stop_bot_flag():
  ```
5. If the above condition is met, send the result using:
  ``` python
  agent.send_result(result: str)
  ```
6. Perform program termination using ```break``` or another terminating function.
