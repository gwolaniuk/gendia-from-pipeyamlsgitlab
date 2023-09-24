import argparse
import yaml
from graphviz import Digraph

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input', help='Input YAML file')
parser.add_argument('output', help='Output PNG file')
args = parser.parse_args()

# Load YAML file
with open(args.input, 'r') as f:
    data = yaml.safe_load(f)

# Create Graphviz graph
dot = Digraph(comment='Pipeline Diagram')
if 'stages' in data:
    for stage in data['stages']:
        dot.node(stage, stage)
        if 'jobs' in data:
            for job in data['jobs']:
                if 'stage' in job and job['stage'] == stage:
                    dot.node(job['name'], job['name'])
                    if 'needs' in job:
                        for need in job['needs']:
                            dot.edge(need, job['name'])
                    dot.edge(stage, job['name'])

# Generate diagram
dot.format = 'png'
dot.render(args.output, view=True)

# Generate DOT file
dot.format = 'dot'
dot.render(args.output + '.dot', view=True)