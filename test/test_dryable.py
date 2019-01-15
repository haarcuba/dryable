import pytest
import dryable

class MyClass:
    def __init__( self ):
        self.calls = []

    @dryable.Dryable()
    def callMe( self, what, * args, ** kwargs ):
        """this is the correct docstring"""
        self.calls.append( what )

class MyClassReturnsSomeValue:
    def __init__( self ):
        self.calls = []

    @dryable.Dryable( 6666 )
    def callMe( self, what ):
        self.calls.append( what )

@pytest.fixture
def subject():
    return MyClass()

@pytest.fixture
def subjectReturnsSomeValue():
    return MyClassReturnsSomeValue()

@pytest.fixture
def dryRun():
    dryable.set( True )

def test_nonDryRun( subject ):
    dryable.set( False )
    for x in range( 10 ):
        subject.callMe( x )

    assert subject.calls == list( range( 10 ) )

def test_decorator( subject ):
    dryable.set( True )
    for x in range( 10 ):
        subject.callMe( x, 1, 2, 3, x='x', y='y' )

    assert subject.calls == []

def test_decorator_leaves_docstring_intact_issue_2( subject ):
    assert subject.callMe.__doc__ == "this is the correct docstring"
    assert subject.callMe.__name__ == "callMe"

def test_decorator_with_return_value( subjectReturnsSomeValue ):
    dryable.set( True )
    subject = subjectReturnsSomeValue
    assert subject.callMe( 1 ) == 6666
    assert subject.callMe( 2 ) == 6666
    assert subject.calls == []
