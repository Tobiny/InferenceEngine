from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QPlainTextEdit, QInputDialog, QFileDialog
from motor import InferenceEngine, get_rules_manually, get_rules_from_file, get_facts_from_user, get_goal_from_user


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motor de inferencia")

        self.layout = QVBoxLayout()

        self.rulesButton = QPushButton("Ingresar reglas")
        self.importRulesButton = QPushButton("Importar reglas desde archivo")
        self.factsButton = QPushButton("Ingresar hechos iniciales")
        self.goalButton = QPushButton("Ingresar objetivo")

        self.forwardButton = QPushButton("Encadenamiento hacia adelante")
        self.backwardButton = QPushButton("Encadenamiento hacia atrás")

        self.resultLabel = QLabel("Resultado:")
        self.resultOutput = QPlainTextEdit()

        self.layout.addWidget(self.rulesButton)
        self.layout.addWidget(self.importRulesButton)
        self.layout.addWidget(self.factsButton)
        self.layout.addWidget(self.goalButton)
        self.layout.addWidget(self.forwardButton)
        self.layout.addWidget(self.backwardButton)
        self.layout.addWidget(self.resultLabel)
        self.layout.addWidget(self.resultOutput)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)

        self.forwardButton.clicked.connect(self.run_forward_chain)
        self.backwardButton.clicked.connect(self.run_backward_chain)
        self.rulesButton.clicked.connect(self.get_rules_manually)
        self.importRulesButton.clicked.connect(self.import_rules_from_file)
        self.factsButton.clicked.connect(self.get_facts_from_user)
        self.goalButton.clicked.connect(self.get_goal_from_user)

        self.setStyleSheet("""
             QMainWindow {
        background-color: #f5f5f5;
    }
    QLabel {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 15px;
    }
    QTextEdit, QPlainTextEdit {
        border: 2px solid #aaa;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        color: #333;
        background-color: #fff;
    }
    QPushButton {
        background-color: #5f87d6;
        color: #fff;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        margin: 15px 0px;
        font-size: 18px;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
    }
    QPushButton:hover {
        background-color: #3564b4;
    }
""")

        self.rules = []
        self.facts = []
        self.goal = ""

    def run_forward_chain(self):
        if not self.rules:
            self.resultOutput.setPlainText("Por favor, ingrese las reglas antes de ejecutar el encadenamiento.")
            return

        if not self.facts:
            self.resultOutput.setPlainText("Por favor, ingrese los hechos iniciales antes de ejecutar el encadenamiento.")
            return

        if not self.goal:
            self.resultOutput.setPlainText("Por favor, ingrese el objetivo antes de ejecutar el encadenamiento.")
            return

        self.resultOutput.setPlainText("Realizando encadenamiento hacia adelante...")
        engine = InferenceEngine(self.rules)
        engine.facts = self.facts

        result = engine.forward_chain(self.goal)

        if result:
            self.resultOutput.setPlainText("El objetivo fue alcanzado con éxito a través del encadenamiento hacia adelante.\n\nPasos tomados:\n" + "\n".join(
                f"Paso {i + 1}: {step}" for i, step in enumerate(engine.steps)))
        else:
            self.resultOutput.setPlainText("El encadenamiento hacia adelante no logró alcanzar el objetivo.\n\nPasos tomados:\n" + "\n".join(
                f"Paso {i + 1}: {step}" for i, step in enumerate(engine.steps)))

    def run_backward_chain(self):
        if not self.rules:
            self.resultOutput.setPlainText("Por favor, ingrese las reglas antes de ejecutar el encadenamiento.")
            return

        if not self.facts:
            self.resultOutput.setPlainText("Por favor, ingrese los hechos iniciales antes de ejecutar el encadenamiento.")
            return

        if not self.goal:
            self.resultOutput.setPlainText("Por favor, ingrese el objetivo antes de ejecutar el encadenamiento.")
            return

        self.resultOutput.setPlainText("Realizando encadenamiento hacia atrás...")
        engine = InferenceEngine(self.rules)
        engine.facts = self.facts

        result = engine.backward_chain(self.goal)

        if result:
            self.resultOutput.setPlainText("El objetivo fue alcanzado con éxito a través del encadenamiento hacia atrás.\n\nPasos tomados:\n" + "\n".join(engine.steps))
        else:
            self.resultOutput.setPlainText(
                "El encadenamiento hacia atrás no logró alcanzar el objetivo.\n\nPasos tomados:\n" + "\n".join(engine.steps))

    def get_rules_manually(self):
        rules_input, ok = QInputDialog.getMultiLineText(self, 'Ingresar reglas',
                                                        'Ingrese una regla por línea en formato: "antecedente1,antecedente2->consecuente". Los antecedentes y consecuentes deben estar separados por comas.')
        if ok and rules_input:
            self.rules = get_rules_manually(rules_input)
            self.resultOutput.setPlainText(
                f"{len(self.rules)} reglas han sido ingresadas manualmente.\n\nLas reglas ingresadas se han guardado correctamente.")

    def import_rules_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home', 'Text Files (*.txt)')
        if filename:
            self.rules = get_rules_from_file(filename)
            self.resultOutput.setPlainText(
                f"{len(self.rules)} reglas importadas desde el archivo: {filename}\n\nLas reglas se han cargado correctamente.")

    def get_facts_from_user(self):
        facts_input, ok = QInputDialog.getText(self, 'Ingresar hechos iniciales',
                                               'Ingrese los hechos iniciales separados por comas. Cada hecho debe ser una afirmación simple.')
        if ok and facts_input:
            self.facts = get_facts_from_user(facts_input)
            self.resultOutput.setPlainText(
                f"{len(self.facts)} hechos iniciales han sido ingresados.\n\nLos hechos ingresados se han guardado correctamente.")

    def get_goal_from_user(self):
        goal_input, ok = QInputDialog.getText(self, 'Ingresar objetivo', 'Ingrese el objetivo. El objetivo debe ser una afirmación simple.')
        if ok and goal_input:
            self.goal = get_goal_from_user(goal_input)
            self.resultOutput.setPlainText(f"Objetivo '{self.goal}' ha sido ingresado.\n\nEl objetivo ha sido guardado correctamente.")


if __name__ == "__main__":
    app = QApplication([])
    mainWin = App()
    mainWin.show()
    app.exec()
