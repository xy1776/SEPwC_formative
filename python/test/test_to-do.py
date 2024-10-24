import pytest
import sys
sys.path.insert(0,"../")
sys.path.insert(0,"./")
from pylint.lint import Run
from pylint.reporters import CollectingReporter
import todo
expected_list ="""1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5"""


class TestTodoList():
    
    def test_list_tasks(self, capsys):
        todo.TASK_FILE = "test/test_list.txt"
        task_list = todo.list_tasks()
        assert task_list == expected_list
        

