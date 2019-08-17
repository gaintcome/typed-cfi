#!/usr/bin/python

import angr
import archinfo

p = angr.Project('./1', load_options={'auto_load_libs' : False})

state = p.factory.blank_state(addr=0x000000000040055f)

j = state.se.BVS('j', 32) # j definition
state.memory.store(0x601040, j)

pg = p.surveyors.Explorer(start=state, find=(0x0000000000400536,)) # start from f2 -> ret@f4
pg.run()

print pg.found
state = pg.found[0].state
print 'j =', state.solver.eval(state.memory.load(0x601040, 4, endness=archinfo.Endness.LE))


