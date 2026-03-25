def load_grammar(self, grammar):
    self.grammar = self._load(grammar)
    self.refs = {}
    for ref in self.grammar.get_elements_by_tag_name("ref"):
        self.refs[ref.attributes["id"].value] = ref
