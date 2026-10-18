---
layout: default
title: Updating Lists
pills: ["demo02 · updatinglists"]
---

# Updating Lists

````md magic-move [02_updatinglists.py] {duration:650, lines:true}
```python
li2 = [1, 2, 3]
```
```python
li2 = [1, 2, 3]
li2.append(4)
```
```python
li2 = [1, 2, 3]
li2.append(4)
li2.append(5)
```
```python
li2 = [1, 2, 3]
li2.append(4)
li2.append(5)
li2.insert(0, 99)
```
```python
li2 = [1, 2, 3]
li2.append(4)
li2.append(5)
li2.insert(0, 99)
li2.extend([33, 44, 55])
```
````

<CollectionState :states="[[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [99, 1, 2, 3, 4, 5], [99, 1, 2, 3, 4, 5, 33, 44, 55]]" />
