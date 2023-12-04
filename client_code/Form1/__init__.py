from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from plotly import graph_objects as go


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    fig = anvil.server.call('base')
    #self.plot_1.figure = fig 
    # Plot some data 
    contador = {}
    for elem in fig:
        contador[elem] = contador.get(elem, 0) + 1
    print(contador)
    self.plot_1.data = [
      go.Scatter(
        x = list(contador.keys()),
        y = list(contador.values()),
        marker = dict(
          color= 'rgb(16, 32, 77)'
        )
      ),
      go.Bar(
        x = list(contador.keys()),
        y = list(contador.values()),
        name = 'block figura'
      )
    ]

