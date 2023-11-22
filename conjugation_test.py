class quiz(object):
    def __init__(self) -> None:
        self.verb_dict = {}
        self.score = 0

    def add_verb(self,verb):
        self.verb_dict[verb.root] = verb

    def random_verb(self):
        import random
        return random.choice(list(self.verb_dict.values()))
    
    def random_category(self):
        import random
        pronouns = ["je","tu","il","nous","vous","ils","meaning"]
        return random.choice(pronouns)

    """what is the french word for the english word"""
    def test_english_to_french(self):
        #order keys in verb_dict randomly
        import random
        keys = list(self.verb_dict.keys())
        random.shuffle(keys)
        self.num_questions = len(keys)
        while len(keys) > 0:
            for key in keys:
                print("What is the french word for: " + self.verb_dict[key].meaning)
                user_input = input()
                self.score += 1
                if user_input == key:
                    print("Correct!\n")
                    keys.remove(key)
                else:
                    print("Incorrect! The correct answer is: " + key + "\n")

    def user_input_test(self):
        verb = self.random_verb()
        print("What is the meaning of the verb: " + verb.root + "?")
        user_input = input()
        if user_input == verb.meaning:
            print("Correct!")
        else:
            print("Incorrect! The correct answer is: " + verb.meaning)

    def user_input_conjugation_random_category(self):
        verb = self.random_verb()
        category = self.random_category()
        if category != "meaning":
            print("What is the conjugation of the verb: " + verb.root + " for the pronoun: " + category + "?")
        else:
            print("What is the meaning of the verb: " + verb.root + "?")
        user_input = input()
        if user_input == verb.__getattribute__(category):
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect! The correct answer is: " + verb.__getattribute__(category) + "\n")



class verb(object):
    def __init__(self,root) -> None:
        self.root = root
        self.je = None
        self.tu = None
        self.il = None
        self.nous = None
        self.vous = None
        self.ils = None
        self.meaning = None

Q = quiz()

avoir = verb("avoir")
avoir.je = "ai"
avoir.tu = "as"
avoir.il = "a"
avoir.nous = "avons"
avoir.vous = "avez"
avoir.ils = "ont"
avoir.meaning = "to have"
Q.add_verb(avoir)


etre = verb("etre")
etre.je = "suis"
etre.tu = "es"
etre.il = "est"
etre.nous = "sommes"
etre.vous = "etes"
etre.ils = "sont"
etre.meaning = "to be"
Q.add_verb(etre)

aller = verb("aller")
aller.je = "vais"
aller.tu = "vas"
aller.il = "va"
aller.nous = "allons"
aller.vous = "allez"
aller.ils = "vont"
aller.meaning = "to go"
Q.add_verb(aller)

faire = verb("faire")
faire.je = "fais"
faire.tu = "fais"
faire.il = "fait"
faire.nous = "faisons"
faire.vous = "faites"
faire.ils = "font"
faire.meaning = "to do"
Q.add_verb(faire)

pouvoir = verb("pouvoir")
pouvoir.je = "peux"
pouvoir.tu = "peux"
pouvoir.il = "peut"
pouvoir.nous = "pouvons"
pouvoir.vous = "pouvez"
pouvoir.ils = "peuvent"
pouvoir.meaning = "to be able to"
Q.add_verb(pouvoir)

savoir = verb("savoir")
savoir.je = "sais"
savoir.tu = "sais"
savoir.il = "sait"
savoir.nous = "savons"
savoir.vous = "savez"
savoir.ils = "savent"
savoir.meaning = "to know"
Q.add_verb(savoir)

mettre = verb("mettre")
mettre.je = "mets"
mettre.tu = "mets"
mettre.il = "met"
mettre.nous = "mettons"
mettre.vous = "mettez"
mettre.ils = "mettent"
mettre.meaning = "to put"

devoir = verb("devoir")
devoir.je = "dois"
devoir.tu = "dois"
devoir.il = "doit"
devoir.nous = "devons"
devoir.vous = "devez"
devoir.ils = "doivent"
devoir.meaning = "to have to"
Q.add_verb(devoir)

venir = verb("venir")
venir.je = "viens"
venir.tu = "viens"
venir.il = "vient"
venir.nous = "venons"
venir.vous = "venez"
venir.ils = "viennent"
venir.meaning = "to come"
Q.add_verb(venir)

voir = verb("voir")
voir.je = "vois"
voir.tu = "vois"
voir.il = "voit"
voir.nous = "voyons"
voir.vous = "voyez"
voir.ils = "voient"
voir.meaning = "to see"
Q.add_verb(voir)

prendre = verb("prendre")
prendre.je = "prends"
prendre.tu = "prends"
prendre.il = "prend"
prendre.nous = "prenons"
prendre.vous = "prenez"
prendre.ils = "prennent"
prendre.meaning = "to take"
Q.add_verb(prendre)

donner = verb("donner")
donner.je = "donne"
donner.tu = "donnes"
donner.il = "donne"
donner.nous = "donnons"
donner.vous = "donnez"
donner.ils = "donnent"
donner.meaning = "to give"
Q.add_verb(donner)

if __name__ == "__main__":
    user_choice = input("What would you like to do?\n1. Test your knowledge of conjugation \n2. Test your knowledge of the meaning of verbs\n")
    if user_choice == "1":
        num_questions = input("How many questions would you like to answer?\n")
        for i in range(int(num_questions)):
            Q.user_input_conjugation_random_category()
        print("Your score is: " + str(Q.score) + "/" + str(num_questions) + "\n")
    elif user_choice == "2":
        Q.test_english_to_french()
        print ("It took: " + str(Q.score) + " attempts to get " + str(Q.num_questions) + " verbs correct.")
    