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
