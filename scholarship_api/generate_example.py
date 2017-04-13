import json
import numpy as np

def generate(size=20,max=100):
	return [[np.random.randint(max) for i in xrange(size)] for j in xrange(size)]

if __name__=='__main__':
	l = generate()
	print json.dumps({'array':l})