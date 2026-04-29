# Unit tests pentru functia find
def test_find_existing_data():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.find(3).data == 3, "Test failed: existing data not found"


def test_find_non_existing_data():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.find(10) is None, "Test failed: non-existing data should return None"


def test_find_empty_tree():
    tree = Tree()
    assert tree.find(5) is None, "Test failed: finding data in an empty tree should return None"


