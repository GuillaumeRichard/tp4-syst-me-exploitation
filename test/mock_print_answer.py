class MockPrintAnswer:
    printed_answers = []

    def print_answer(self, answer):
        self.printed_answers.append(answer)

    # nécessaire car même quand j'instancie un mock print par méthode,
    # le tableau de réponse ne se réinitialise pas.
    def delete_all_answers(self):
        del self.printed_answers[:]
