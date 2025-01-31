import unittest

class TextOperation:
    def __init__(self, operation_type, character=None):
        self.operation_type = operation_type
        self.character = character

class TextEditor:
    def __init__(self):
        self.text = []
        self.operation_stack = []

    def add_character(self,char):
        self.text.append(char)
        self.operation_stack.append(TextOperation('add', char))
        self.display_text()

    def delete_character(self):
        if self.text:
            delete_char = self.text.pop()
            self.operation_stack.append(TextOperation('delete', delete_char))
        self.display_text()
    
    def undo(self):
        if self.operation_stack:
            last_operation = self.operation_stack.pop()
            if last_operation.operation_type == 'add':
                self.text.pop()
            elif last_operation.operation_type == 'delete':
                self.text.append(last_operation.character)
            self.display_text()

    def display_text(self):
        print("Current Text:", "".join(self.text))

# Unit Tests
class TestTextEditor(unittest.TestCase):
    def test_add_character(self):
        editor = TextEditor()
        editor.add_character('A')
        self.assertEqual("".join(editor.text), "A")
    
    def test_delete_character(self):
        editor = TextEditor()
        editor.add_character('B')
        editor.delete_character()
        self.assertEqual("".join(editor.text), "")

    def test_undo_add(self):
        editor = TextEditor()
        editor.add_character('C')
        editor.undo()
        self.assertEqual("".join(editor.text), "")


