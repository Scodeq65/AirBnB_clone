#!/usrbin/python3
"""Test Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test review instance."""

    def setUp(self):
        """Set up for each test."""
        self.review = Review()

    def test_attributes(self):
        """Test that Review has the correct attributes."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test that Review is a subclass of BaseModel."""
        self.assertIsInstance(self.review, Review)


if __name__ == "__main__":
    unittest.main()
