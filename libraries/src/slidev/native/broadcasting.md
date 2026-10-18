---
layout: default
title: Three Factors for Every Pixel
pills: ["demo13 · broadcasting"]
---

# Three Factors for Every Pixel

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "Shapes align from the right",
          "values": [
            [
              48,
              64,
              3
            ],
            [
              "",
              "",
              3
            ],
            [
              "",
              "",
              ""
            ]
          ],
          "columns": [
            "height",
            "width",
            "channels"
          ],
          "labels": [
            "photo",
            "factors",
            "result"
          ],
          "selected": [
            [
              0,
              2
            ],
            [
              1,
              2
            ],
            [
              2,
              2
            ]
          ]
        },
        {
          "name": "Channel multipliers",
          "values": [
            [
              1.1,
              1.0,
              0.9
            ]
          ],
          "columns": [
            "red",
            "green",
            "blue"
          ],
          "labels": [
            "factor"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Shapes align from the right",
          "values": [
            [
              48,
              64,
              3
            ],
            [
              "",
              "",
              3
            ],
            [
              48,
              64,
              3
            ]
          ],
          "columns": [
            "height",
            "width",
            "channels"
          ],
          "labels": [
            "photo",
            "factors",
            "result"
          ],
          "selected": [
            [
              0,
              2
            ],
            [
              1,
              2
            ],
            [
              2,
              2
            ]
          ]
        },
        {
          "name": "Channel multipliers",
          "values": [
            [
              1.1,
              1.0,
              0.9
            ]
          ],
          "columns": [
            "red",
            "green",
            "blue"
          ],
          "labels": [
            "factor"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Shapes align from the right",
          "values": [
            [
              48,
              64,
              3
            ],
            [
              "",
              "",
              3
            ],
            [
              48,
              64,
              3
            ]
          ],
          "columns": [
            "height",
            "width",
            "channels"
          ],
          "labels": [
            "photo",
            "factors",
            "result"
          ],
          "selected": [
            [
              0,
              2
            ],
            [
              1,
              2
            ],
            [
              2,
              2
            ]
          ]
        },
        {
          "name": "Channel multipliers",
          "values": [
            [
              1.1,
              1.0,
              0.9
            ]
          ],
          "columns": [
            "red",
            "green",
            "blue"
          ],
          "labels": [
            "factor"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Shapes align from the right",
          "values": [
            [
              48,
              64,
              3
            ],
            [
              "",
              "",
              3
            ],
            [
              48,
              64,
              3
            ]
          ],
          "columns": [
            "height",
            "width",
            "channels"
          ],
          "labels": [
            "photo",
            "factors",
            "result"
          ],
          "selected": [
            [
              0,
              2
            ],
            [
              1,
              2
            ],
            [
              2,
              2
            ]
          ]
        },
        {
          "name": "Channel multipliers",
          "values": [
            [
              1.1,
              1.0,
              0.9
            ]
          ],
          "columns": [
            "red",
            "green",
            "blue"
          ],
          "labels": [
            "factor"
          ],
          "selected": []
        }
      ]
    }
  ],
  "output": [
    [],
    [],
    [
      "(48, 64, 3) (3,) (48, 64, 3)"
    ],
    [
      "(48, 64, 3)"
    ]
  ],
  "captions": [
    "A length-three factor vector aligns with the channel dimension.",
    "Every pixel receives the same three factors, followed by clipping.",
    "The result keeps the photo's height, width and channel count.",
    "broadcast_shapes confirms the compatible result shape."
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-1|1-2|1-3|1-4}
factors = np.array([1.1, 1.0, 0.9])
corrected = np.clip(photo * factors, 0.0, 1.0)
print(photo.shape, factors.shape, corrected.shape)
print(np.broadcast_shapes((48, 64, 3), (3,)))
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
