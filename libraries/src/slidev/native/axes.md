---
layout: default
title: Reducing Days and Hours
pills: ["demo15 · the_axis_argument"]
---

# Reducing Days and Hours

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "Days by hours",
          "values": [
            [
              1.0,
              2.0,
              3.0,
              4.0
            ],
            [
              2.0,
              0.0,
              1.0,
              3.0
            ],
            [
              0.0,
              1.0,
              2.0,
              1.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        },
        {
          "name": "axis=0 removes days",
          "values": [
            [
              "",
              "",
              "",
              ""
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "sum"
          ],
          "selected": []
        },
        {
          "name": "axis=1 removes hours",
          "values": [
            [
              ""
            ],
            [
              ""
            ],
            [
              ""
            ]
          ],
          "columns": [
            "sum"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Days by hours",
          "values": [
            [
              1.0,
              2.0,
              3.0,
              4.0
            ],
            [
              2.0,
              0.0,
              1.0,
              3.0
            ],
            [
              0.0,
              1.0,
              2.0,
              1.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        },
        {
          "name": "axis=0 removes days",
          "values": [
            [
              "",
              "",
              "",
              ""
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "sum"
          ],
          "selected": []
        },
        {
          "name": "axis=1 removes hours",
          "values": [
            [
              ""
            ],
            [
              ""
            ],
            [
              ""
            ]
          ],
          "columns": [
            "sum"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Days by hours",
          "values": [
            [
              1.0,
              2.0,
              3.0,
              4.0
            ],
            [
              2.0,
              0.0,
              1.0,
              3.0
            ],
            [
              0.0,
              1.0,
              2.0,
              1.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        },
        {
          "name": "axis=0 removes days",
          "values": [
            [
              3.0,
              3.0,
              6.0,
              8.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "sum"
          ],
          "selected": []
        },
        {
          "name": "axis=1 removes hours",
          "values": [
            [
              ""
            ],
            [
              ""
            ],
            [
              ""
            ]
          ],
          "columns": [
            "sum"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Days by hours",
          "values": [
            [
              1.0,
              2.0,
              3.0,
              4.0
            ],
            [
              2.0,
              0.0,
              1.0,
              3.0
            ],
            [
              0.0,
              1.0,
              2.0,
              1.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        },
        {
          "name": "axis=0 removes days",
          "values": [
            [
              3.0,
              3.0,
              6.0,
              8.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "sum"
          ],
          "selected": []
        },
        {
          "name": "axis=1 removes hours",
          "values": [
            [
              10
            ],
            [
              6
            ],
            [
              4
            ]
          ],
          "columns": [
            "sum"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Days by hours",
          "values": [
            [
              1.0,
              2.0,
              3.0,
              4.0
            ],
            [
              2.0,
              0.0,
              1.0,
              3.0
            ],
            [
              0.0,
              1.0,
              2.0,
              1.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        },
        {
          "name": "axis=0 removes days",
          "values": [
            [
              3.0,
              3.0,
              6.0,
              8.0
            ]
          ],
          "columns": [
            "08",
            "09",
            "10",
            "11"
          ],
          "labels": [
            "sum"
          ],
          "selected": []
        },
        {
          "name": "axis=1 removes hours",
          "values": [
            [
              10
            ],
            [
              6
            ],
            [
              4
            ]
          ],
          "columns": [
            "sum"
          ],
          "labels": [
            "Mon",
            "Tue",
            "Wed"
          ],
          "selected": []
        }
      ]
    }
  ],
  "output": [
    [],
    [
      "20"
    ],
    [
      "[3 3 6 8]"
    ],
    [
      "[10  6  4]"
    ],
    [
      "(3, 1)"
    ]
  ],
  "captions": [
    "Each row is one day; each column is one selected hour.",
    "Without an axis, all twelve counts reduce to one total.",
    "axis=0 adds down the days and leaves four hour totals.",
    "axis=1 adds across hours and leaves three day totals.",
    "keepdims retains a size-one column dimension."
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="300px">

```python {1-1|1-2|1-3|1-4|1-5}
plays = np.array([[1, 2, 3, 4], [2, 0, 1, 3], [0, 1, 2, 1]])
print(plays.sum())
print(plays.sum(axis=0))
print(plays.sum(axis=1))
print(plays.sum(axis=1, keepdims=True).shape)
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
