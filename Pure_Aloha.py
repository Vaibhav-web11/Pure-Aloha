import random
node=10
q_generate=0.8
p_send=0.25

states=[False]*node
result=[]
latencies=[0]*node
node_latencies = {i: [] for i in range(node)}

def generation(q_generate):
    for i in range(len( states)):
        if random.random() <=  q_generate:
             states[i] = True

def transmission( states,node_latencies,latencies,p_send):
    senders = []
    actives = []

    actives = [i for i in range(len( states)) if  states[i]==True]

    senders = [actv for actv in actives if random.random() <=  p_send]
    
    if len(senders) > 1:
        result.append(False)
        for i in actives:
             latencies[i] += 1

    else:
        if not senders:
            result.append(True)
            for i in actives:
                 latencies[i] += 1
        else:
            states[senders[0]] = False
            node_latencies[senders[0]].append( latencies[senders[0]])                # the sender is not latent now
            latencies[senders[0]] = 0
            actives.remove(senders[0])
            for i in actives:
                 latencies[i] += 1
            result.append(True)
            
epochs=20
for i in range( epochs):
    generation(q_generate)
    transmission(states,node_latencies,latencies,p_send)
avg = 0
for i in range(node):
    y = [value for value in node_latencies[i] if value]

    if y:
        avg += sum(y) / len(y)

v=avg / node
print('Exhibition:')
print('Result: ' , result)
print('Node latencies: ' ,node_latencies)
print('Average node latency: ' ,v)