class Teacher:
    def teach(self):
        print("Teaching academic subjects.")

class SportsCoach:
    def train(self):
        print("Training students in sports.")

class Tutor(Teacher, SportsCoach):
    def guide(self):
        print("Guiding students in studies and sports.")


t = Tutor()
t.teach()
t.train()
t.guide()
