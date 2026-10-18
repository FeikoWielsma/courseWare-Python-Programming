---
layout: default
title: A View Shares the Photo Buffer
pills: ["demo09 · views_and_copies"]
---

# A View Shares the Photo Buffer

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              "",
              "",
              ""
            ],
            [
              "",
              "",
              ""
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    },
    {
      "grids": [
        {
          "name": "photo red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "16",
            "17",
            "18"
          ],
          "labels": [
            "12",
            "13"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "crop red channel",
          "values": [
            [
              1.0,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        },
        {
          "name": "copy red channel",
          "values": [
            [
              0.51,
              0.58,
              0.447
            ],
            [
              0.353,
              0.651,
              0.773
            ]
          ],
          "columns": [
            "0",
            "1",
            "2"
          ],
          "labels": [
            "0",
            "1"
          ],
          "selected": [
            [
              0,
              0
            ]
          ]
        }
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [
      "[1. 0. 0.]"
    ],
    [
      "[0.50980395 0.5254902  0.7019608 ]"
    ],
    [
      "True"
    ],
    [
      "False"
    ],
    [
      "False"
    ]
  ],
  "captions": [
    "Slicing creates a view of the photo buffer.",
    "copy allocates an independent buffer.",
    "Writing red through the view changes the photo.",
    "The photo contains the new pixel.",
    "The independent copy retains the original pixel.",
    "The view shares memory with the photo.",
    "The copy does not share the buffer.",
    "Advanced indexing also creates a copy."
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="300px">

```python {1-1|1-2|1-3|1-4|1-5|1-6|1-7|1-8}
crop = photo[12:36, 16:48]
detached = crop.copy()
crop[0, 0] = [1.0, 0.0, 0.0]
print(photo[12, 16])
print(detached[0, 0])
print(np.shares_memory(crop, photo))
print(np.shares_memory(detached, photo))
print(np.shares_memory(photo[[0, 1]], photo))
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
