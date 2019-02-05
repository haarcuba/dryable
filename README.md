# Dryable - enabling `--dry-run` functionality

Sometimes we are want to check the basic logic of our
programs without running certain operations that are lengthy and
cause side effects.

E.g. we would like some script to tell us what it *would have* done,
but without actually doing it: a good example is when you have a script
that is supposed to delete some old files or database entries, and you want to 
use a "dry run" to see what it *would* do, before actually letting it loose.

```shell
$ ./my-deleting-script --dry-run # don't really delete anything, just show me
```

The problem with that sort of thing is that your code gets filled with
annoying `if` statements like:
```python
if not dryRun:
    doTheThing()
else:
    logTheThing()
```

This is precisely what `Dryable` is for. You set the "dry run" mode like this:

```python
dryable.set( True ) # or False to turn it off
```

Here's an example if how to use it:
 

```python
import dryable
import requests
import sys

def findOldFilesForDeletion():
    return [ 'some', 'results' ]

@dryable.Dryable()
def deleteFiles( results ):
    print( 'will now open an real world connection'
           'that requires a server and will make side effects' )
    requests.post( 'http://url.to.some.server/results', data = str( results ) )


# the next line ensures that deleteFiles
# will not run if --dry-run is specified on the command line
dryable.set( '--dry-run' in sys.argv )

# now code as usual
results = findOldFilesForDeletion()
print( 'got: {}'.format( results ) )
deleteFiles( results )
```

## Installation

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
E.g. you want to have `--dont-delete-files` and separately `--dont-save-to-db` or something.
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

### Logging

Dryable logs to a logger called `dryable` which is available via `Dryable.logger`
