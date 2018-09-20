import logging
import collections

class Dryable:
    _dryRun = collections.defaultdict( lambda: False )
    logger = logging.getLogger( 'dryable' )

    def __init__( self, value = None, *, label = 'default' ):
        self._value = value
        self._label = label

    @classmethod
    def set( cls, value, label = 'default' ):
        if value:
            cls._dryRun[ label ] = True
        else:
            cls._dryRun[ label ] = False

    def __call__( self, function ):
        def _decorated( * args, ** kwargs ):
            if self._dryRun[ self._label ]:
                argsString = ', '.join( [ str( argument ) for argument in args ] )
                kwargsString = ', '.join( [ '{}={}'.format( key, value ) for ( key, value ) in kwargs.items() ] )
                if len( kwargs ) > 0:
                    if len( args ) > 0:
                        kwargsString = ', {}'.format( kwargsString )
                Dryable.logger.info( 'dryable[{label}] skip: {function}( {args}{kwargs} )'.format( label = self._label, function = function.__qualname__, args = argsString, kwargs = kwargsString ) )
                return self._value
            return function( * args, ** kwargs )

        _decorated.__doc__ = function.__doc__
        _decorated.__name__ = function.__name__
        return _decorated

set = Dryable.set
