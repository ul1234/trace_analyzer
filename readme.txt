1. Usage: python trace_analyzer.py {trace_file} {trace_config.py}
{trace_file}: generated from TraceViewer, right click menu->show Text View
{trace_config.py}: trace config file, it's a python file imported by trace_analyzer.py. It can be changed to adjust the diagram show for the traces.

example: 
python trace_analyzer.py trace_94641_40M_1.txt trace_config_lan.py
python trace_analyzer.py trace_1.txt trace_config_example.py

2. How to draw line on the diagram:
1) Press Ctrl or Shift or Alt Key and Click Left Button to Start to draw line.
   Ctrl Key: choose any point
   Shift Key: auto choose the left point of a block
   Alt Key: auto choose the right point of a block
2) Click Left Button (or Press Shift or Alt Key and Click Left Button) to Finish, line saved.
   No Key pressed: choose any point
   Shift Key: auto choose the left point of a block
   Alt Key: auto choose the right point of a block
3) Click Right Button to Finish, line canceled.
4) Press Delete Key to remove the last drawed line.


