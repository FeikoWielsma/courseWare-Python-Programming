---
layout: default
title: Tuple Unpacking
pills: ["demo08 · destructurewithtuples"]
---

# Tuple Unpacking

````md magic-move {duration:650, lines:true}
```python
t = ("Albert", "Einstein")
```
```python
t = ("Albert", "Einstein")
v, s = t
```
```python
t = ("Albert", "Einstein")
v, s = t
v, s = s, v
print(v)  # 'Einstein'
print(s)  # 'Albert'
```
````

<div v-click="3" class="course-step">

```text
Einstein
Albert
```

</div>
