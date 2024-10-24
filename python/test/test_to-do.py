import pytest
import sys
sys.path.insert(0,"../")
sys.path.insert(0,"./")
from pylint.lint import Run
from pylint.reporters import CollectingReporter
from todo import *


class TestTodoList():
    
    def test_reading_data(self):

