class CustomStack:
    def __init__(self):
        self.text = ""  
        self.history = []  
    
    def insert(self, value):
        # Add the current text state to history before modifying it
        self.history.append(self.text)
        self.text += value  # Append the new string to the current text
    
    def delete(self, value):
        # Add the current text state to history before modifying it
        self.history.append(self.text)
        # Delete the last 'value' characters from the text
        self.text = self.text[:-int(value)]
    
    def get(self, value):
        # Get the character at the 1-based index 'value'
        index = int(value) - 1
        if 0 <= index < len(self.text):
            print(self.text[index])
        else:
            print("Index out of bounds")
    
    def undo(self):
        if self.history:
            # Revert to the last saved state in the history
            self.text = self.history.pop()
    
    def process_commands(self, commands):
        for command in commands:
            parts = command.split()
            cmd_type = parts[0]

            if cmd_type == '1':  # Insert
                self.insert(parts[1])
            elif cmd_type == '2':  # Delete
                self.delete(parts[1])
            elif cmd_type == '3':  # Get
                self.get(parts[1])
            elif cmd_type == '4':  # Undo
                self.undo()

# Input handling
if __name__ == "__main__":
   
    input_commands = input().split(',')
    
 
    editor = CustomStack()
    editor.process_commands(input_commands)
