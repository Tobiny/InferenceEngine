class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent


    def __str__(self):
        return f"Si {' y '.join(list(self.antecedents))}, entonces {self.consequent}"


class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.facts = set()
        self.steps = [] # Para guardar los pasos de la inferencia

    def print_rules(self):
        for rule in self.rules:
            print(f"Antecedents: {', '.join(rule.antecedents)}, Consequent: {rule.consequent}")

    def find_conflict_set(self):
        conflict_set = []
        for rule in self.rules:
            if rule.antecedents.issubset(self.facts):
                conflict_set.append(rule)
        return conflict_set

    def select_rule(self, conflict_set):
        selected_rule = conflict_set[0]
        print("Regla seleccionada:", selected_rule)
        return selected_rule

    def fire_rule(self, rule):
        self.facts.add(rule.consequent)

    def forward_chain(self, goal):
        fired_rules = set()
        while goal not in self.facts:
            conflict_set = self.find_conflict_set()
            conflict_set = [rule for rule in conflict_set if rule not in fired_rules]
            if not conflict_set:
                return False
            selected_rule = self.select_rule(conflict_set)
            self.fire_rule(selected_rule)
            fired_rules.add(selected_rule)
            self.steps.append(str(selected_rule))
        return True

    def backward_chain(self, goal):
        if goal in self.facts:
            return True
        for rule in self.rules:
            if rule.consequent == goal:
                if all(self.backward_chain(antecedent) for antecedent in rule.antecedents):
                    self.fire_rule(rule)
                    self.steps.append(str(rule))
                    return True
        return False

def get_rules_manually(rules_input):
    rules = []
    for rule_input in rules_input.split("\n"):
        if rule_input.strip() != '':
            antecedents, consequent = rule_input.split("->")
            antecedents = set(antecedent.strip() for antecedent in antecedents.split(","))
            rules.append(Rule(antecedents, consequent.strip()))
    return rules


def get_rules_from_file(filename):
    rules = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            antecedents, consequent = line.strip().split("->")
            antecedents = set(antecedent.strip() for antecedent in antecedents.split(","))
            rules.append(Rule(antecedents, consequent.strip()))
    return rules

def get_facts_from_user(facts_input):
    return set(fact.strip() for fact in facts_input.split(","))


def get_goal_from_user(goal_input):
    return goal_input.strip()
