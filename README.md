# gendia-from-pipeyamlsgitlab
generate diagrams from yaml gitlab pipelines files
---Installation:
install python and graphviz (i.e. with winget install python graphviz)
...remember to add PATH to your environment
next
install required python packages via pip
```python
# pip install -r required.txt
```

for now we are using these libs in these versions:
- graphviz==0.20.1
- pygame==2.5.2
- PyYAML==6.0.1

---Running:
```python
# python squarepilot.py NAME-OF-YAML-FILE NAME-OF-OUTPUT
```
so for ex.yml yaml file and test.png desired output run in your terminal:
```python
# python squarepilot.py ex.yml test.png```

...and the result should be generated dot file and desired diagram in above mentioned fimlename (test.png)

