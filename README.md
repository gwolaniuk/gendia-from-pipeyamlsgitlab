# gendia-from-pipeyamlsgitlab
generate diagrams from yaml gitlab pipelines files
- Installation:
install python and graphviz (i.e. with winget install python graphviz)
...remember to add PATH to your environment
next
install required python packages via pip
```bash# pip install -r required.txt```

- Running:
# python squarepilot.py NAME-OF-YAML-FILE NAME-OF-OUTPUT
so for ex.yml yaml file and test.png desired output run in your terminal:
```bash# python squarepilot.py ex.yml test.png```
...and the result should be generated dot file and desired diagram in above mentioned fimlename (test.png)

