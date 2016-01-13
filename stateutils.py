from operator import itemgetter
from werkzeug.exceptions import BadRequest

DEFAULT_STATES_PER_PAGE=10

#Get Paginated States
def getPaginatedStates(states, offset=1, limit=DEFAULT_STATES_PER_PAGE, len_states=50):
	try:
		offset_t=int(offset)
		limit_t=int(limit)	
	except ValueError:
		raise BadRequest('Bad Request: offset/limit should only contain digits.')	
	if((offset_t <1 or offset_t >len_states) or (limit_t<1) or ((offset_t + limit_t) <1 or (offset_t + limit_t)>len_states+1)):
		raise BadRequest('Bad Request: offset/limit out of bounds.')
	return states[offset_t-1:offset_t+limit_t-1]


#Get Sorted States
def sortStates(states, sortBy='name', order='asc'):
	if(sortBy=='name' and order=='asc'):
		return sorted(states, key=itemgetter('name'))
	if(sortBy=='name' and order=='desc'):
		return sorted(states, key=itemgetter('name'), reverse=True)
	raise BadRequest('Bad Request: Current supported sort options are - sortBy=name, order=asc/desc.')	