#here's awhole bunch of dicts that link a persons name to all the people ty're friends with
friends = {
'Daigo' : ['Gonzo', 'Animal'],
'Kermit' : ['Beaker', 'Sam Eagle', 'Miss Piggy'],
'Gonzo' : ['Beaker'],
'Miss Piggy' : ['Animal', 'Swedish Chef', 'Fozzie Bear'],
'Sam Eagle' : ['Animal'],
'Swedish Chef' : ['Beaker'],
'Beaker' : ['Miss Piggy'],
'Animal' : ['Gonzo'],
'Fozzie Bear' : ['Sam Eagle', 'Swedish Chef']
}


class person:

    def __init__(self, name):
        self.friends = friends[name]

    def get_friends(self):
        return self.friends







name = sys.argv[1]
degree = int(sys.argv[2])



# New milestone! write a recursive function that returns a list of muppets that are X degrees apart from somebody!
def kevin_bacon(_name, _degree):
    """
    WRITE ME
    """



kevin_bacon(name, degree)
