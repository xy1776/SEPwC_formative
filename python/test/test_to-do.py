import pytest
import sys
import os
import shutil
from pylint.lint import Run
from pylint.reporters import CollectingReporter
sys.path.insert(0,"../")
sys.path.insert(0,"./")
import todo
expected_list ="""1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5"""
test_file = "test/test_list.txt"


class TestTodoList():
    
    def test_list_tasks(self):
        todo.TASK_FILE = test_file
        task_list = todo.list_tasks()
        assert task_list == expected_list

    def test_remove_task(self):
        temp_list = ".temp_test.txt"
        shutil.copyfile(test_file, temp_list)
        todo.TASK_FILE = temp_list
        # should error (need to catch?)
        todo.remove_task(0)
        # list should be the same
        task_list = todo.list_tasks()
        assert task_list == expected_list
        # should also error
        todo.remove_task(10)
        # list should be the same
        task_list = todo.list_tasks()
        assert task_list == expected_list
        # should not error!
        todo.remove_task(1)
        task_list = todo.list_tasks()
        new_expected = "1. Item 2\n2. Item 3\n3. Item 4\n4. Item 5"
        # note assert checks from 1 as we remove line 0
        assert task_list == new_expected
        os.remove(temp_list)

        

    def test_add_task(self):
        pass

    def test_main(self):
        pass
        

