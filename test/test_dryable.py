import pytest
import dryable

class MyClass:
    def __init__( self ):
        self.calls = []

    @dryable.Dryable()
    def callMe( self, what ):
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
        subject.callMe( x )

    assert subject.calls == []

def test_decorator_with_return_value( subjectReturnsSomeValue ):
    dryable.set( True )
    subject = subjectReturnsSomeValue
    assert subject.callMe( 1 ) == 6666
    assert subject.callMe( 2 ) == 6666
    assert subject.calls == []
