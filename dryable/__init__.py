import logging

class Dryable:
    _dryRun = False

    def __init__( self, value = None ):
        self._value = value

    @classmethod
    def set( cls, value ):
        cls._dryRun = value

    def __call__( self, function ):
        def _decorated( * args, ** kwargs ):
            if self._dryRun:
                argsString = ', '.join( [ str( argument ) for argument in args ] )
                kwargsString = ', '.join( [ '{}={}'.format( key, value ) for ( key, value ) in kwargs.items() ] )
                if len( kwargs ) > 0:
                    if len( args ) > 0:
                        kwargsString = ', {}'.format( kwargsString )
                logging.info( 'dryable skip: {}( {}{} )'.format( function.__qualname__, argsString, kwargsString ) )
                return self._value
            return function( * args, ** kwargs )

        return _decorated

set = Dryable.set
