---
layout: default
title: Traversing a Book Card
pills: ["demo05 · walking_the_tree"]
---

# Traversing a Book Card

<script setup>
const run = {
  "frames": [
    {
      "id": "selection",
      "label": "Tree cursor"
    }
  ],
  "states": [
    {
      "names": {
        "selection": {
          "cursor": "price"
        }
      },
      "objects": {
        "price": {
          "type": "price",
          "value": "p"
        },
        "container": {
          "type": "container",
          "value": "div"
        },
        "book": {
          "type": "book",
          "value": "article"
        },
        "title": {
          "type": "title",
          "value": "a"
        },
        "stock": {
          "type": "stock",
          "value": "p"
        }
      },
      "active": [
        "selection.cursor"
      ]
    },
    {
      "names": {
        "selection": {
          "cursor": "container"
        }
      },
      "objects": {
        "price": {
          "type": "price",
          "value": "p"
        },
        "container": {
          "type": "container",
          "value": "div"
        },
        "book": {
          "type": "book",
          "value": "article"
        },
        "title": {
          "type": "title",
          "value": "a"
        },
        "stock": {
          "type": "stock",
          "value": "p"
        }
      },
      "active": [
        "selection.cursor"
      ]
    },
    {
      "names": {
        "selection": {
          "cursor": "book"
        }
      },
      "objects": {
        "price": {
          "type": "price",
          "value": "p"
        },
        "container": {
          "type": "container",
          "value": "div"
        },
        "book": {
          "type": "book",
          "value": "article"
        },
        "title": {
          "type": "title",
          "value": "a"
        },
        "stock": {
          "type": "stock",
          "value": "p"
        }
      },
      "active": [
        "selection.cursor"
      ]
    },
    {
      "names": {
        "selection": {
          "cursor": "title"
        }
      },
      "objects": {
        "price": {
          "type": "price",
          "value": "p"
        },
        "container": {
          "type": "container",
          "value": "div"
        },
        "book": {
          "type": "book",
          "value": "article"
        },
        "title": {
          "type": "title",
          "value": "a"
        },
        "stock": {
          "type": "stock",
          "value": "p"
        }
      },
      "active": [
        "selection.cursor"
      ]
    },
    {
      "names": {
        "selection": {
          "cursor": "stock"
        }
      },
      "objects": {
        "price": {
          "type": "price",
          "value": "p"
        },
        "container": {
          "type": "container",
          "value": "div"
        },
        "book": {
          "type": "book",
          "value": "article"
        },
        "title": {
          "type": "title",
          "value": "a"
        },
        "stock": {
          "type": "stock",
          "value": "p"
        }
      },
      "active": [
        "selection.cursor"
      ]
    }
  ],
  "output": [
    [],
    [
      "div"
    ],
    [],
    [
      "Sharp Objects"
    ],
    [
      "In stock"
    ]
  ],
  "captions": [
    "Select the price paragraph in the fixture.",
    "parent is the surrounding div.",
    "find_parent walks up to the containing article.",
    "select_one finds the title link below the article.",
    "find_next_sibling finds the stock paragraph beside the price."
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-1|1-2|1-4|1-5|1-7}
price = soup.select_one("p.price_color")
print(price.parent.name)

pod = price.find_parent("article")
print(pod.select_one("h3 a")["title"])

print(price.find_next_sibling("p").get_text(strip=True))
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" direction="row" :cell-width="100" :frame-width="170" :pitch="110" :gap="65" />
</template>
</DataStructuresRun>
