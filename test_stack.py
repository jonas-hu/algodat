from stack import Stack, EmptyStackException
import pytest

# setup
# teardown
@pytest.fixture()
def stack():
    stack = Stack()
    return stack


def test_new_stack_is_empty(stack):
    assert stack.is_empty()


def test_stack_is_not_empty_after_push(stack):
    stack.push(1)
    assert not stack.is_empty()


def test_pop_will_return_pushed_item(stack):
    item = 1
    stack.push(item)
    assert stack.pop() == item


def test_check_if_stack_is_lifo(stack):
    first_item = 1
    second_item = 2
    stack.push(first_item)
    stack.push(second_item)

    assert stack.pop() == second_item
    assert stack.pop() == first_item


def test_peek_doesnt_remove_item(stack):
    item = 1
    stack.push(1)
    assert stack.peek() == 1
    assert stack.peek() == 1


def test_pop_an_empty_stack(stack):
    with pytest.raises(EmptyStackException):
        stack.pop()
