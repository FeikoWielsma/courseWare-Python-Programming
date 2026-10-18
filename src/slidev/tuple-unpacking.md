---
layout: default
title: Tuple Unpacking
pills: ["demo08 · destructurewithtuples"]
---

# Tuple Unpacking

````md magic-move {duration:650, lines:true}
```python
selection = ("Imagine", "Toxic")
```
```python
selection = ("Imagine", "Toxic")
primary, backup = selection
```
```python
selection = ("Imagine", "Toxic")
primary, backup = selection
primary, backup = backup, primary
print(primary)  # 'Toxic'
print(backup)  # 'Imagine'
```
````

<div primary-click="3" class="course-step">

```text
Toxic
Imagine
```

</div>
