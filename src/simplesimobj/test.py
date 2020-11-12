import m5
from m5.objects import *

root = Root(full_system = False)
root.hello = HelloObject(latency="2us", number_of_fires = 10)

m5.instantiate()

print("Beginning Simulation")
exit_event = m5.simulate()
print("Exiting @ tick {} because {}"
    .format(m5.curTick(), exit_event.getCause()))
