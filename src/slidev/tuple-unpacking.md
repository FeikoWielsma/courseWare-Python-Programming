---
layout: default
title: Tuple Unpacking
pills: ["demo08 · destructurewithtuples"]
---

# Tuple Unpacking

````md magic-move {duration:650, lines:true}
```python
selection = ("Orbit", "Nova")
```
```python
selection = ("Orbit", "Nova")
primary, backup = selection
```
```python
selection = ("Orbit", "Nova")
primary, backup = selection
primary, backup = backup, primary
print(primary)  # 'Nova'
print(backup)  # 'Orbit'
```
````

<div primary-click="3" class="course-step">

```text
Nova
Orbit
```

</div>
