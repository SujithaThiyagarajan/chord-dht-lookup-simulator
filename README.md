# Chord Distributed Hash Table (DHT) Lookup Simulator

## Objective
The objective of this project is to simulate the Chord Peer-to-Peer Lookup Protocol using a Distributed Hash Table (DHT). The system models an N-node Chord ring and demonstrates efficient key lookup using finger tables, achieving O(log N) lookup complexity.

---

## Overview
Chord is a distributed lookup protocol used in peer-to-peer systems to efficiently locate the node responsible for a given key. Nodes are arranged in a circular identifier space, and each node maintains a finger table to route queries efficiently.

This project simulates:
- Chord ring formation
- Finger table construction
- Key lookup using hop-by-hop routing
- Lookup path visualization
- Hop count analysis

---

## Key Concepts
- Distributed Hash Table (DHT)
- Chord Ring Topology
- Finger Table
- Successor and Predecessor
- O(log N) Lookup Complexity

---

## System Design

### Chord Ring
- Nodes are arranged in a circular identifier space of size 2^m
- Each node is responsible for a range of keys

### Finger Table
Each node maintains a routing table:
finger[i] = (n + 2^i) % (2^m)

This helps in skipping nodes and improves lookup efficiency.

### Lookup Process
- Lookup starts from a selected node
- Query is forwarded using finger table
- At each step, the query moves closer to the target key
- Process continues until the responsible node is found

---

## Features
- Dynamic generation of Chord ring
- Visualization of node placement
- Finger table display for selected node
- Key lookup simulation
- Hop-by-hop routing path display
- Number of hops calculation

---

## Tools and Technologies
- Python
- Streamlit
- NumPy
- Matplotlib

---

## Implementation Details
- Nodes are randomly generated within identifier space
- Finger tables are constructed for each node
- Lookup uses closest preceding node logic
- Path of lookup is tracked and displayed
- Hop count is calculated to demonstrate efficiency

---

## Output
- Nodes in the Chord ring
- Circular topology visualization
- Lookup path between nodes
- Number of hops
- Finger table entries

---

## How to Run

pip install -r requirements.txt  
streamlit run app.py

---

## Applications
- Peer-to-peer networks
- Distributed storage systems
- Content delivery networks
- Blockchain systems

---

## Conclusion
This project demonstrates how the Chord protocol efficiently performs key lookups in distributed systems using finger tables. It reduces lookup complexity from O(N) to O(log N), improving scalability.

---
