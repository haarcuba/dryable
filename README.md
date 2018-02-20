# Dryable - enabling `--dry-run` functionality

Sometimes we are want to check the basic logic of our
programs without running certain operations that are lengthy and
cause side effects.

This is precisely what `Dryable` is for. You set the "dry run" mode like this:

```python
dryable.set( True ) # or False to turn it off
```
 

```python
import dryable
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
dryable.set( '--dry-run' in sys.argv )
results = runCalculations()
print( 'got: {}'.format( results ) )
saveToRemoteDatabase( results )
```

## Intallation

Install dryable like so

    $ pip install dryable

## Returning Custom Values

By default a `Dryable` decorated function will return `None` in dry-run mode. If you need some other value, specify it like so:


```python
@dryable.Dryable( [ 'fake person 1', 'fake person 2' ] )
def getPeopleFromDatabase():
    return actualQueryFromDB()
```

## What If I Have Different Things I Want To Dry-Run?

If you're using `dryable`, you may run into situations in which you want to dry-run some code, but not some other code.
The way to handle this situation is with *labels*

```python
import dryable

@dryable.Dryable( label = 'labelA' )
def functionA():
    print( "Hi, I am A" )

@dryable.Dryable( label = 'labelB' )
def functionB():
    print( "Hi, I am B" )

dryable.set( True, 'labelA' )
functionA() # this will be dried up
functionB() # this will run for real
```
