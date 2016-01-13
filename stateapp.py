#!flask/bin/python
from werkzeug.exceptions import BadRequest
from flask import Flask, request, jsonify, make_response
from data import states
from stateutils import getPaginatedStates, sortStates, DEFAULT_STATES_PER_PAGE

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(offset=1, limit=10, sortBy='name', order='asc'):
	return make_response("Welcome! Please go to /state for a list of states in USA.")


@app.route('/state', methods=['GET'])
def getStates(offset=1, limit=DEFAULT_STATES_PER_PAGE, sortBy='name', order='asc'):
	#Get Request Arguments
	if("sortBy" in request.args):
		sortBy = request.args.get("sortBy")
	if("order" in request.args):
		order = request.args.get("order")	
	if("offset" in request.args):
		offset = request.args.get("offset")
	if("limit" in request.args):
		limit = request.args.get("limit")
	#Get sorted states	
	sorted_states = sortStates(sortBy=sortBy, order=order, states=states)
	#Verify offset and limit parameters are valid and get paginated states.
	pg_states = getPaginatedStates(offset=offset, limit=limit, len_states=len(states), states=sorted_states)
	return jsonify({'states': pg_states})


@app.route('/state/<state_abbr>', methods=['GET'])
def getStateByAbbr(state_abbr=""):
	found=False
	for state in states:
		if (state['abbreviation'].lower() == state_abbr.lower()):
			found_state=state
			found=True
	if not found:
		raise BadRequest('Bad Request: Abbreviation does not exist.')
	return jsonify({'state': found_state})
 

@app.errorhandler(400)
def bad_request(error):
    return make_response(error.get_description(), 400)
    
@app.errorhandler(500)
def internal_error(error):
    return make_response('error: Its a Server Error.', 500)

if __name__ == '__main__':
	app.run(debug=False)