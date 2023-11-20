class GrammarStats:
    def __init__(self):
        # total passed
        self.total_passed = 0
        # total checked
        self.total_checked = 0
  
    def check(self, text):
        # self.text = text    # Probably I don't need to have it here. Why?

        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.total_checked += 1
        if text[0].isupper() and (text[-1] in ['!', '?', '.']):
            self.total_passed += 1 
            return True
        else:
            False

  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
    

        passed_test = (self.total_passed / self.total_checked) * 100
        return passed_test