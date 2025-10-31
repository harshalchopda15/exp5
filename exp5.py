from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from IPython.display import display

# 1. Build the circuit for the Bell State |Ψ->
qc = QuantumCircuit(2)

# Start by flipping qubit 1 to |1⟩, making the initial state |01⟩
qc.x(1)

qc.h(0)     # Apply Hadamard to qubit 0
qc.cx(0, 1) # Apply CNOT (control=0, target=1)
qc.z(0)     # **Apply Z-gate to qubit 0 to flip the phase**

print("Circuit Diagram:")
display(qc.draw('mpl')) # 'mpl' gives a nice image

# --- Part 1: Plot State Vector (NO MEASUREMENT) ---
# We get the ideal statevector (no measurement)
sv_sim = Aer.get_backend('statevector_simulator')
statevector = sv_sim.run(qc).result().get_statevector()
print("\nPlotting Bloch spheres (shows pure state):")
display(plot_bloch_multivector(statevector))

# --- Part 2: Visualize Histogram (NEEDS MEASUREMENT) ---
# **Now** we add measurements to the circuit to get counts.
qc.measure_all()
qasm_sim = Aer.get_backend('qasm_simulator') # Use 'qasm_simulator' for shots
counts = qasm_sim.run(qc, shots=1024).result().get_counts()
print("\nPlotting histogram (shows measurement results):")
display(plot_histogram(counts))
