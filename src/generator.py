from qiskit import QuantumCircuit
# from qiskit.circuit.library import (
#     IGate,
#     HGate,
#     TGate,
#     CXGate
# )


def build_simple_circuit(depth: int, slants: tuple[int, int]) -> QuantumCircuit:

    qc = QuantumCircuit(2)

    # Insert single-qubit gates based on slants
    for _ in range(slants[0]):
        qc.t(0)
    for _ in range(slants[1]):
        qc.t(1)
    qc.cx(0, 1)
    qc.cx(1, 0)
    qc.cx(0, 1)
    for _ in range(depth-slants[0]):
        qc.t(0)
    for _ in range(depth-slants[1]):
        qc.t(1)

    return qc
