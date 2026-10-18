---
layout: default
title: Summing Each Genre
pills: ["demo16 · groupby_agg"]
---

# Summing Each Genre

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "Input tracks",
          "values": [
            [
              "Rock",
              11
            ],
            [
              "Rock",
              28
            ],
            [
              "Soul",
              45
            ]
          ],
          "columns": [
            "genre",
            "plays"
          ],
          "labels": [
            "Imagine",
            "Yesterday",
            "Respect"
          ],
          "selected": []
        },
        {
          "name": "One sum per genre",
          "values": [
            [
              ""
            ],
            [
              ""
            ]
          ],
          "columns": [
            "plays"
          ],
          "labels": [
            "Rock",
            "Soul"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input tracks",
          "values": [
            [
              "Rock",
              11
            ],
            [
              "Rock",
              28
            ],
            [
              "Soul",
              45
            ]
          ],
          "columns": [
            "genre",
            "plays"
          ],
          "labels": [
            "Imagine",
            "Yesterday",
            "Respect"
          ],
          "selected": [
            [
              0,
              0
            ],
            [
              1,
              0
            ],
            [
              2,
              0
            ]
          ]
        },
        {
          "name": "One sum per genre",
          "values": [
            [
              ""
            ],
            [
              ""
            ]
          ],
          "columns": [
            "plays"
          ],
          "labels": [
            "Rock",
            "Soul"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input tracks",
          "values": [
            [
              "Rock",
              11
            ],
            [
              "Rock",
              28
            ],
            [
              "Soul",
              45
            ]
          ],
          "columns": [
            "genre",
            "plays"
          ],
          "labels": [
            "Imagine",
            "Yesterday",
            "Respect"
          ],
          "selected": [
            [
              0,
              0
            ],
            [
              1,
              0
            ],
            [
              2,
              0
            ]
          ]
        },
        {
          "name": "One sum per genre",
          "values": [
            [
              39
            ],
            [
              45
            ]
          ],
          "columns": [
            "plays"
          ],
          "labels": [
            "Rock",
            "Soul"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input tracks",
          "values": [
            [
              "Rock",
              11
            ],
            [
              "Rock",
              28
            ],
            [
              "Soul",
              45
            ]
          ],
          "columns": [
            "genre",
            "plays"
          ],
          "labels": [
            "Imagine",
            "Yesterday",
            "Respect"
          ],
          "selected": [
            [
              0,
              0
            ],
            [
              1,
              0
            ],
            [
              2,
              0
            ]
          ]
        },
        {
          "name": "One sum per genre",
          "values": [
            [
              39
            ],
            [
              45
            ]
          ],
          "columns": [
            "plays"
          ],
          "labels": [
            "Rock",
            "Soul"
          ],
          "selected": []
        }
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [
      "genre",
      "Rock    39",
      "Soul    45",
      "Name: plays, dtype: int64"
    ]
  ],
  "captions": [
    "The input contains three tracks and their fictional play counts.",
    "groupby assigns rows with the same genre to a group.",
    "sum applies to each group's plays and combines the results by genre.",
    "The result has one indexed value per genre."
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="300px">

```python {1-1|1-2|1-3|1-4}
sample = tracks.iloc[:3][["genre", "plays"]]
groups = sample.groupby("genre")
totals = groups["plays"].sum()
print(totals)
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
