import dryable
import logging

import requests
import sys

def runCalculations():
    return [ 'some', 'results' ]

@dryable.Dryable()
def saveToRemoteDatabase( results ):
    print( 'will now open an real world connection'
           'that requires a server and will make side effects' )
    requests.post( 'http://url.to.some.server/results', data = str( results ) )


# the next line ensures that saveToRemoteDatabase
# will not run if --dry-run is specified on the command line
logging.basicConfig(level=logging.INFO)
dryable.set( '--dry-run' in sys.argv )
results = runCalculations()
print( 'got: {}'.format( results ) )
saveToRemoteDatabase( results )
