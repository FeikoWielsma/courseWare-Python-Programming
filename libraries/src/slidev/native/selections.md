---
layout: default
title: Labels and Positions
pills: ["demo10 · iloc_by_position"]
---

# Labels and Positions

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "Same table, two selectors",
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
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Same table, two selectors",
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
              1,
              1
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Same table, two selectors",
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
              1
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Same table, two selectors",
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
              1
            ],
            [
              1,
              1
            ]
          ]
        }
      ]
    }
  ],
  "output": [
    [],
    [
      "28"
    ],
    [
      "11"
    ],
    [
      "           plays",
      "title           ",
      "Imagine       11",
      "Yesterday     28"
    ]
  ],
  "captions": [
    "The three-row sample has title labels and zero-based positions.",
    "loc selects Yesterday by its label.",
    "iloc selects the first row by position.",
    "The label slice includes both Imagine and Yesterday."
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="300px">

```python {1-1|1-2|1-3|1-4}
frame = tracks.iloc[:3][["genre", "plays"]]
print(frame.loc["Yesterday", "plays"])
print(frame.iloc[0, 1])
print(frame.loc["Imagine":"Yesterday", ["plays"]])
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
