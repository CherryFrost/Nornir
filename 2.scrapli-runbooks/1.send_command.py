from nornir import InitNornir # <-- This turns the nornir engine on
from nornir_scrapli.tasks import send_command # <-- Send show commands utilizing scrapli
from nornir_utils.plugins.functions import print_result # <-- Print our results to the terminal

nr = InitNornir(config_file='config.yaml')

results = nr.run(task=send_command, command="sho run interface gig0/0")

print_result(results)