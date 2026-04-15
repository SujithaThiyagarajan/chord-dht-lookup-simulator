import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from chord import ChordNode, chord_lookup

st.set_page_config(layout="wide")
st.title("Chord Distributed Hash Table Simulator")

# Sidebar controls
st.sidebar.header("Controls")
m = st.sidebar.slider("Identifier bits (m)", 3, 6, 4)
num_nodes = st.sidebar.slider("Number of Nodes", 3, 10, 5)

max_id = 2**m

# Generate nodes
nodes = sorted(set(np.random.randint(0, max_id, num_nodes)))
st.write("### Nodes in Ring:", nodes)

# Build node objects
node_objects = {}
for n in nodes:
    node_objects[n] = ChordNode(n, m, nodes)

for node in node_objects.values():
    node.build_finger_table()

# Select start node & key
start_node = st.selectbox("Select Start Node", nodes)
key = st.number_input("Enter Key", 0, max_id - 1)

# ----------- DRAW RING -----------
st.subheader("Chord Ring")

angles = np.linspace(0, 2*np.pi, len(nodes), endpoint=False)
x = np.cos(angles)
y = np.sin(angles)

fig, ax = plt.subplots()

# Draw nodes
ax.scatter(x, y)

# Connect circular ring
for i in range(len(nodes)):
    ax.plot([x[i], x[(i+1)%len(nodes)]],
            [y[i], y[(i+1)%len(nodes)]],
            'gray')

# Label nodes
for i, node in enumerate(nodes):
    ax.text(x[i], y[i], str(node), fontsize=10, ha='center')

# ----------- LOOKUP -----------
if st.button("Run Lookup"):
    path = chord_lookup(start_node, key, node_objects)

    # Highlight path
    for i in range(len(path) - 1):
        if path[i] in nodes and path[i+1] in nodes:
            a = nodes.index(path[i])
            b = nodes.index(path[i+1])
            ax.plot([x[a], x[b]], [y[a], y[b]], linewidth=2)

    st.pyplot(fig)

    st.subheader("Lookup Path")
    st.write(" → ".join(map(str, path)))

    st.subheader("Number of Hops")
    st.write(len(path))

else:
    st.pyplot(fig)

# ----------- FINGER TABLE -----------
st.subheader("Finger Table")

selected = st.selectbox("Select Node for Finger Table", nodes)

table_data = []
for i, (start, node) in enumerate(node_objects[selected].finger_table):
    table_data.append({
        "Entry": i,
        "Start": start,
        "Points To": node
    })

st.table(table_data)