import pytest
import dryable

def labelClass( label ):
    class TheClass:
        def __init__( self ):
            self.calls = []

        @dryable.Dryable( label = label )
        def callMe( self ):
            self.calls.append( label )

    return TheClass

def test_labels():
    dryable.set( True, 'project1' )

    project1 = labelClass( 'project1' )()
    project2 = labelClass( 'project2' )()

    for x in range( 10 ):
        project1.callMe()
        project2.callMe()

    assert project1.calls == []
    assert project2.calls == [ 'project2' ] * 10

def test_labels_on_and_off():
    dryable.set( True, 'project1' )

    project1 = labelClass( 'project1' )()
    project2 = labelClass( 'project2' )()

    for x in range( 5 ):
        project1.callMe()
        project2.callMe()

    assert project1.calls == []
    assert project2.calls == [ 'project2' ] * 5

    dryable.set( False, 'project1' )
    dryable.set( True, 'project2' )
    for x in range( 5 ):
        project1.callMe()
        project2.callMe()

    assert project1.calls == [ 'project1' ] * 5
    assert project2.calls == [ 'project2' ] * 5
