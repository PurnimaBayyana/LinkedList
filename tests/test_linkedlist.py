from linkedlist import __version__
from linkedlist.LinkedList import LinkedList, Node

def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_creation():
    ll = LinkedList()
    assert ll.head == None

def test_node():
    node = Node("one")
    assert node.value == "one"
    assert node.next == None

def test_insert():
    result = LinkedList()
    result.insert("a")
    assert result.head.value == "a"
    assert result.head.next == None
   

def test_includes():
    result = LinkedList()
    result.insert("one")
    result.insert("two")
    result.insert("three")
    assert result.includes("three")
    

def test_not_includes():
    result = LinkedList()
    result.insert("one")
    result.insert("two")
    result.insert("three")
    assert result.includes("two") == False 

def test_tostring():
    result = LinkedList()
    result.insert('c')
    result.insert('b')
    result.insert('a')
    assert result.tostring() == '{a} -> {b} -> {c} -> NULL'


