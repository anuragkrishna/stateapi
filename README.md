# stateapi
Rest API for retrieving all states in USA

This application is currently hosted on http://usstateapi-pzero.rhcloud.com/

Sample Request:

1. http://usstateapi-pzero.rhcloud.com/

2. http://usstateapi-pzero.rhcloud.com/state

3. http://usstateapi-pzero.rhcloud.com/state?offset=1&limit=10

4. http://usstateapi-pzero.rhcloud.com/state?sortBy=name&order=asc

5. http://usstateapi-pzero.rhcloud.com/state?sortBy=name&order=desc

4. http://usstateapi-pzero.rhcloud.com/state?sortBy=name&order=asc&offset=6&limit=20

5. http://usstateapi-pzero.rhcloud.com/state/{state_abbreviation}

   Ex - http://usstateapi-pzero.rhcloud.com/state/al
 
   
Error Handling (Bad Request) : 

 offset/limit out of bound
 
 offset/limit should only be digits,
 
 state_abbreviation not valid, 
 
 sortBy/order currently not supported   
 
   
Local Hosting:

Ensure Flask 0.10.1 is installed

Command - python wsgi.py

Check the application on http://127.0.0.1:8051/


   
