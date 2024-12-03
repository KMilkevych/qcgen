#!/usr/bin/env python3
import argparse
from src.generator import build_simple_circuit
from qiskit.qasm2 import dumps
from qiskit.compiler import transpile

parser = argparse.ArgumentParser()
parser.add_argument("depth", help="Depth of unary gate chain", type=int)
parser.add_argument("slant_0", help="Slant of the first qubit", type=int)
parser.add_argument("slant_1", help="Slant of the second qubit", type=int)
parser.add_argument("-p", "--platform", help="Transpile circuit to platform", choices=["guadalupe", "tenerife", "cambridge"])
parser.add_argument("-o", "--output")
args = parser.parse_args()

print(args)

# Check errors
if args.slant_0 < 0 or args.slant_1 < 0:
    raise ValueError("Slant must not be negative")

# Generate the circuit
circuit = build_simple_circuit(args.depth, (args.slant_0, args.slant_1))

print("Generated circuit:")
print(circuit)

# Perform transpilation to supported gates
if args.platform is not None:

    basis_gates = []
    match args.platform:
        case "guadalupe":
            basis_gates = ["id", "rz", "sx", "x", "cx", "reset"]
        case "tenerife":
            basis_gates = ["u1", "u2", "u3", "cx", "id"]
        case "cambridge":
            basis_gates = ["u1", "u2", "u3", "cx", "id"]

    print(f"Transpiling circuit to {args.platform}")
    circuit = transpile(circuit, basis_gates=basis_gates, optimization_level=0)
    print(circuit)

if args.output is not None:
    qasm_str = dumps(circuit)
    with open(args.output, "w") as f:
        f.write(qasm_str)
        f.write("\n")
