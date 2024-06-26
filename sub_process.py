import time
from agent_handler import AgentHandler

agent = AgentHandler()

while True:
    for i in range(10):
        # print(i)
        time.sleep(1)
    if agent.stop_bot_flag():
        agent.send_result("")
        break