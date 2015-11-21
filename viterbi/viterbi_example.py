# coding: utf-8
# https://en.wikipedia.org/wiki/Viterbi_algorithm

import sys

OUTPUT_ENCODING="shift-jis"

states = ('Healthy', 'Fever') 
observations = ('normal', 'cold', 'dizzy')
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
 
transition_probability = {
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
   }
 
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
   }


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath
    
    # Return the most likely sequence over the given time frame
    n = len(obs) - 1
    ###
    print_yield(V)
    
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

def print_yield(V):
    for e in dptable(V):
        sys.stdout.write(e)
    

# Don't study this; it just prints a table of the steps.
def dptable(V):
    yield "    "
    yield " ".join(("%7d" % i) for i in range(len(V)))
    yield "\n"
    for y in V[0]:
        yield "%.5s: " % y
        yield " ".join("%.7s" % ("%f" % v[y]) for v in V)
        yield "\n"

def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
def main():
    print(example())

if __name__ == '__main__':
    main()
