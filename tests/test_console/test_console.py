#!/usr/bin/python3
"""Unit tests for console.py."""

import unittest
from console import HBNBCommand
from unittest.mock import patch
import io


class TestHBNBCommand(unittest.TestCase):
    """test cases for the HBNBCommand class."""

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            HBNBCommand().onecmd("help")
            self.assertIn(
                    "Documented commands (type help <topic>):",
                    mock_stdout.getvalue()
            )

    def test_quit_command(self):
        """Test the quit command."""
        with patch('sys.stdout', new=io.StringIO()):
            with patch('builtins.input', return_value='quit'):
                self.assertEqual(HBNBCommand().cmdloop(), None)

    def test_EOF_command(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=io.StringIO()):
            with patch('builtins.input', return_value='EOF'):
                self.assertEqual(HBNBCommand().cmdloop(), None)

    def test_emptyline(self):
        """Test the empty line input."""
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            HBNBCommand().onecmd("")
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_noninteractive_help(self):
        """Test help command in non-interactive mode."""
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            with patch('sys.stdin', io.StringIO('help\n')):
                HBNBCommand().cmdloop()
                self.assertIn(
                        "Documented commands (type help <topic>):",
                        mock_stdout.getvalue()
                )


if __name__ == '__main__':
    unittest.main()
