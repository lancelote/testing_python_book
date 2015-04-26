# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
from bank.bank.bank_app import app
#
# with PyCallGraph(output=GraphvizOutput()):
app.run(debug=True)