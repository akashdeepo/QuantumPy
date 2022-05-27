# %%
# Visualize Quantum gates on Bloch's Sphere
#example the X-gate represents the Pauli-X matrix X=[[0,1],[1,0]]

# %%
#install qiskit- new virtual environment may be needed
#pip install qiskit

# %%
#import libraries
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
from tkinter import *
import warnings
import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

warnings.filterwarnings('ignore')
# %%
#define the UI window
root =tkinter.Tk()
root.title('QuantumPy')

#set the icon
root.iconbitmap(default='QPy.ico')
root.geometry('398x425')
#blocking the resize
root.resizable(0,0)



# %%
#define colors and styling
background = '#d43410'
buttons = '#FFFFFF'
special_buttons = '#d43415'
button_font = ('Times New Roman',18)
display_font = ('Arial',32)

# %%
# Initialise the Quantum Circuit
# Note we cannot visualise measurments in the app--The state vector collapses into one of the basis vectors
def initialize_circuit():
    """
    Initializes the Quantum Circuit
    """
    global circuit 
    circuit = QuantumCircuit(1)

initialize_circuit()
theta=0

# %%
# Define Functions
def display_gate(gate_input):
    """
    Adds a gate notation to track operations in the display
    Max # of operations = 10
    Disables all buttons 
    """
    #Insert the defined gate
    display.insert(END,gate_input)

    #Check if # has reached 10 and disable
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word=["R","D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed-= sum(count_double_valued_gates)
    if num_gates_pressed==10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard_gate]
        for gate in gates:
            gate.config(state=DISABLED)



# %%
# Define the clear button
def clear(circuit):
    """
    a.Clears the display
    b.reset for fresch calculations
    c.check if # reached 10 and reenable the buttons
    """
    #clear display
    display.delete(0, END)

    #reset the circuit back to |0> (zero ket)
    initialize_circuit()

    #check if buttons are disable -if yes enable them---trick--if x_gate is disable all buttons will be disable by nature
    if x_gate['state']==DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard_gate]
        for gate in gates:
            gate.config(state=NORMAL)

# %%
#define visualize circuit fnction
def visualize_circuit(circuit,window):
    """
    visualizes the single cubit rotations corresponding to applied gates in separate window
    handles visualisation errors
    """

    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()
        

# %%
#defining variable theta entered by user
def change_theta(num,window,circuit,key):
    """
    Changes te global variable + change back theta to 0 and closes the window

    """
    global theta
    theta = num* np.pi
    if key=='x':
        circuit.rx(theta,0)
        theta=0
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()

# %%
# Define user Input
def user_input(circuit,key):
    """
    Take the rotation angle input 
    for parameterized rotation gates(Rx,Ry,Rz)
    """

    #initialize and define properties of window
    get_input = tkinter.Tk()
    get_input.title('Select Theta')
    get_input.geometry('360x160')
    get_input.resizable(0,0)

    val1 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='Pi/4', command=lambda:change_theta(0.25, get_input, circuit, key))
    val1.grid(row=0, column=0), key

    val2 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='Pi/2', command=lambda:change_theta(0.50, get_input, circuit, key))
    val2.grid(row=0, column=1)
    
    val3 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='Pi', command=lambda:change_theta(1.0, get_input, circuit, key))
    val3.grid(row=0, column=2)

    val4 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='2*Pi', command=lambda:change_theta(2.0, get_input, circuit, key))
    val4.grid(row=0, column=3, stick='W')

    nval1 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='-Pi/4', command=lambda:change_theta(-0.25, get_input, circuit, key))
    nval1.grid(row=1, column=0)

    nval2 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='-Pi/2', command=lambda:change_theta(-0.50, get_input, circuit, key))
    nval2.grid(row=1, column=1)

    nval3 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='-Pi', command=lambda:change_theta(-1.0, get_input, circuit, key))
    nval3.grid(row=1, column=2)

    nval4 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=('Arial',10), text='-2Pi', command=lambda:change_theta(-2.0, get_input, circuit, key))
    nval4.grid(row=1, column=3, sticky='W')

    text_object = tkinter.Text(get_input, height=20, width=20, bg='#d43415')

    note="""
    Select Value for theta
    Range = [-2pi,2pi]
    """
    text_object.grid(sticky='WE', columnspan=4)
    text_object.insert(END,note)

    get_input.insert(END,note)


    


# %%
#defining 'about' section
def about():
    """
    Display project info and button details
    """
    info = tkinter.Tk()
    info.title('About')
    info.geometry('700x800')
    info.resizable(0,0)

    text = tkinter.Text(info, height=20, width=20)

    # Creating the label
    label = tkinter.Label(info, text= "About Quantum Py")
    label.config(font =("Times", 14))

    text_to_display = """
    About: Visualizing effect of different Quantum Gates 
           for single Qubit Rotation on Bloch Sphere

    Project by: Akash Deep
    Keywords: Python, Tkinter, Qiskit
    
    Info about the gate buttons and associated Qiskit commands:

    X  = flips the state of qubit-------------------------------- circuit.x()
    Y  = rotates the state vector about Y-axis------------------- circuit.y()
    Z  = flips the phase by PI radians--------------------------- circuit.z()
    Rx = parameterized rotation about the X axis----------------- circuit.rx()
    Ry = parameterized rotation about the Y axis----------------- circuit.ry()
    Rz = parameterized rotation about the 2 axis----------------- circuit.rz()
    S  = rotates the state vector about 2 axis by PI/2 radians--- circuit.s()
    I  = rotates the state vector about 2 axis by PI/4 radians--- circuit.t()
    Sd = rotates the state vector about 2 axis by -PI/2 radians-- circuit.sdg()
    Td = rotates the state vector about 2 axis by -PI/4 radians-- circuit.tdg()
    H  = creates the state of superposition---------------------- circuit.h()
    
    For Rx, Ry and Rz, 
    theta (rotation angle) allowed range in the app is [-2*PI, 2*PI]
    
    In case of a Visualization Error, the app closes automatically. 
    This indicates that vigualization of your circuit is not possible,
    
    Note: At a time, only ten operations can be visualized.
   
   """


    label.pack()
    text.pack(fill='both',expand=True)

    #inserting text
    text.insert(END,text_to_display)

    root.mainloop()


# %%


# %%


# %%
# Define layout and Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

# %%
#Defining the layout for Display frame
display= tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3,pady=4)

# %%
#1 Defining first set of buttons- x,y,z gates
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command=lambda:[display_gate('x'), circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command=lambda:[display_gate('y'), circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command=lambda:[display_gate('z'), circuit.z(0)])

x_gate.grid(row=0, column=0,ipadx=45, pady=1)
y_gate.grid(row=0, column=1,ipadx=45, pady=1)
z_gate.grid(row=0, column=2,ipadx=53, pady=1, sticky='E')

# %%
#2 Defining second set of buttons- Rx, Rx, Rz
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX', command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY', command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ', command=lambda:[display_gate('Rz'),user_input(circuit,'z')])

Rx_gate.grid(row=1, column=0, columnspan=1, pady=1, sticky='WE')
Ry_gate.grid(row=1, column=1, columnspan=1, pady=1, sticky='WE')
Rz_gate.grid(row=1, column=2, columnspan=1, pady=1, sticky='WE')

# %%
#3 Defining third set of buttons - S, S dagger, Hadamard
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda:[display_gate('s'), circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command=lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda:[display_gate('H'), circuit.h(0)])

s_gate.grid(row=2, column=0, columnspan=1, pady=1, sticky='WE')
sd_gate.grid(row=2, column=1, pady=1, sticky='WE')
hadamard_gate.grid(row=2, column=2, rowspan=2, pady=1, sticky='WENS')

# %%
#4 Defining fourth set of buttons T and T dagger
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda:[display_gate('t'), circuit.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command=lambda:[display_gate('TD'),circuit.tdg(0)])

t_gate.grid(row=3, column=0, pady=1, sticky='WE')
td_gate.grid(row=3, column=1, pady=1, sticky='WE')


# %%
#5 Defining fifth set of buttons - Quit and Visualise
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Quit', command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Visualize', command=lambda:visualize_circuit(circuit,root))

quit.grid(row=4, column=0, columnspan=1, pady=1, sticky='WE', ipadx=5)
visualize.grid(row=4, column=2, pady=1, sticky='WE', ipadx=8)


# %%
#6 Defining sixth set of buttons - About and Clear
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='About', command=about)
clear_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Clear', command=lambda:clear(circuit))

about_button.grid(row=5, column=0, columnspan=3, sticky='WE')
clear_button.grid(row=6, column=0, columnspan=3, sticky='WE')


# %%
#final run
root.mainloop()

# %%


# %%


# %%




