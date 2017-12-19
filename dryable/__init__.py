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
                return self._value
            return function( * args, ** kwargs )

        return _decorated

set = Dryable.set
