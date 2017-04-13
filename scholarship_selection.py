import numpy as np

NUM_SCHOLARSHIPS 			= 11

def extend_row(scholarships, row):
	"""computes optimal sequence, total along new row of scholarships array"""
	col  					= 0
	max_prod 				= -np.inf
	while col+NUM_SCHOLARSHIPS-1 <= row:
		prod = np.prod(scholarships[row,col:col+NUM_SCHOLARSHIPS])
		if prod > max_prod:
			opt_interval 	= ((row,col),(row,col+NUM_SCHOLARSHIPS))
			max_prod 		= prod
		col += 1

	col 					= 0
	while col <= row:
		prod = np.prod(scholarships[row-NUM_SCHOLARSHIPS:row,col])
		if prod > max_prod:
			opt_interval 	= ((row-NUM_SCHOLARSHIPS,col),(row,col))
			max_prod     	= prod
		col += 1

	return opt_interval, max_prod

def extend_col(scholarships, col):
	"""computes optimal sequence, total along new col of scholarships array"""
	row 		= 0
	max_prod 	= -np.inf
	while row+NUM_SCHOLARSHIPS-1 <= col:
		prod = np.prod(scholarships[row:row+NUM_SCHOLARSHIPS,col])
		if prod > max_prod:
			opt_interval = ((row,col),(row+NUM_SCHOLARSHIPS,col))
			max_prod     = prod
		row += 1

	row 		= 0
	while row <= col:
		prod = np.prod(scholarships[row,col-NUM_SCHOLARSHIPS:col])
		if prod > max_prod:
			opt_interval = ((row,col-NUM_SCHOLARSHIPS),(row,col))
			max_prod 	 = prod
		row += 1

	return opt_interval, max_prod

def extend_diag(scholarships,d):
	"""computes (sequence, total) along diagonal ending at index (d,d)"""
	return ((d-NUM_SCHOLARSHIPS+1,d-NUM_SCHOLARSHIPS+1),(d,d)), np.prod(np.diagonal(scholarships[d-NUM_SCHOLARSHIPS+1:d,d-NUM_SCHOLARSHIPS+1:d]))

def extend(scholarships,n):

	opt_row, max_row  = extend_row(scholarships,n)
	opt_col, max_col  = extend_row(scholarships,n)
	opt_d  , max_diag = extend_diag(scholarships,n)
	
	choose 			  = np.argmax([max_row,max_col,max_diag])

	if choose == 0:
		return opt_row, max_row
	if choose == 1:
		return opt_col, max_col
	if choose == 2:
		return opt_d, max_diag

	
def scholarship_selection(scholarships):
	"""Implements a dynamic programming approach to determining the optimal sequence in O(n**2) time and O(1) space"""

	scholarships 		= np.array(scholarships)
	
	# iterates difference equation
	total    			= -np.inf
	opt_coords 			= None
	for i in xrange(NUM_SCHOLARSHIPS-1,scholarships.shape[0]):
		coord_pair, val = extend(scholarships,i)
		if val > total:
			total 		= val
			opt_coords 	= coord_pair 

	"""unpacks sequence from pairs of coordinates ( (x1,x2), (y1,y2) )"""
	# diagonal case
	if opt_coords[0][0] == opt_coords[0][1] and opt_coords[1][0] == opt_coords[1][1]:
		unpacked_sequence = [ int(scholarships[ opt_coords[0][0]+i,opt_coords[0][1]+i ]) for i in xrange(11)]
	# row case
	if opt_coords[0][0] == opt_coords[1][0]:
		unpacked_sequence = [ int(scholarships[ opt_coords[0][0],opt_coords[0][1]+i ]) for i in xrange(11)  ]
	# column case
	if opt_coords[0][1] == opt_coords[1][1]:
		unpacked_sequence = [ int(scholarships[ opt_coords[0][0]+i,opt_coords[0][1] ]) for i in xrange(11)  ]

	return {'sequence' : unpacked_sequence, 'total' : val}

if __name__=='__main__':
	
	sch =  np.array([ [ float(np.random.randint(10)) for i in xrange(20)] for i in xrange(20)])
	print scholarship_selection(sch)