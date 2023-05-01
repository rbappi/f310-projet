param num_nodes;
param num_edges;

set NODES := 1..num_nodes;
set EDGES := 1..num_edges;

param capacity{EDGES};
param source;
param sink;

var flow{EDGES} >= 0, <= capacity{EDGES};
var flow_out_of_source;

maximize obj: flow_out_of_source;

s.t. flow_conservation{i in NODES: i != source and i != sink}:
    sum{j in NODES: (i,j) in EDGES} flow[(i,j)] =
    sum{j in NODES: (j,i) in EDGES} flow[(j,i)];

s.t. capacity_constraints{(i,j) in EDGES}:
    flow[(i,j)] <= capacity[(i,j)];

s.t. non_negativity{(i,j) in EDGES}:
    flow[(i,j)] >= 0;

s.t. flow_out_of_source_constraint:
    flow_out_of_source = sum{j in NODES: (source,j) in EDGES} flow[(source,j)];

solve;

printf "Maximum flow out of source: %g\n", flow_out_of_source;

for{(i,j) in EDGES: flow[(i,j)] > 0} {
    printf "Flow from %d to %d: %g\n", i, j, flow[(i,j)];
}
