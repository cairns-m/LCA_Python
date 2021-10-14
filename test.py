from unittest import TestCase

from LCA1 import *


class Test(TestCase):
    def test_find_path(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 4, 5), 2)
        #test for LCA of balanced BST


class Test(TestCase):
    def test_find_path(self):
        root = Node(10)
        root.left = Node(11)
        root.right = Node(12)
        root.left.left = Node(13)
        root.left.left = Node(14)
        self.assertEqual(findLCA(root, 11, 14), 11)
        # testing for LCA of left-leaning BST


class Test(TestCase):
    def test_find_path(self):
        root = Node(10)
        root.left = Node(11)
        root.right = Node(12)
        root.left.left = Node(13)
        root.left.left = Node(14)
        self.assertEqual(findLCA(root, 11, 11), 11)
        #testing to find the LCA of itself is itself


class Test(TestCase):
    def test_find_path(self):
        root = Node(10)
        root.left = Node(11)
        root.right = Node(12)
        root.left.left = Node(13)
        root.left.left = Node(14)
        self.assertEqual(findLCA(root, 11, 12), -1)
        #testing to find the LCA of itself is itself


class Test(TestCase):
    def test_find_path(self):
        root = None
        self.assertEqual(findLCA(root, 1, 1), -1)
        #testing to find the LCA of an empty tree


class Test(TestCase):
    def test_find_path(self):
        root = Node(20)
        root.left = Node(21)
        root.right = Node(22)
        root.left.right = Node(23)
        root.right.left = Node(24)
        root.left.right.left = Node(25)
        root.right.left.right = Node(26)
        root.right.left.right.left = Node(27)
        self.assertEqual(findLCA(root, 25, 27), 20)
        #testing to find the LCA of unbalanced tree
