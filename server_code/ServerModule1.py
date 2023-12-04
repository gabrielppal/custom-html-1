import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
from anvil.google.drive import app_files
import plotly.graph_objects as go
import anvil.tables.query as q


@anvil.server.callable
def base():
  db=app_files.base_school_survey
  ws=db['Hoja1']
  l = ws.rows
  s = []
  for i in range(len(l)):
      s.append(l[i]['block_game'])
  base = ','.join(s)
  base=base.split(sep=',')
  base=base[:]
  base = list(map(int, base))
  print(base)
  return base
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
