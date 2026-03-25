def loadGrammar(self, grammar): 
    self.grammar = self._load(grammar) 
    self.refs = {}                                 
    for ref in self.grammar.getElementsByTagName("ref"):     
        self.refs[ref.attributes["id"].value] = ref
