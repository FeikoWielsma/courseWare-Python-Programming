---
layout: default
title: Keeping Unmatched Artists
pills: ["demo19 · merge_how"]
---

# Keeping Unmatched Artists

<script setup>
const run = {
  "states": [
    {
      "grids": [
        {
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "UK"
            ],
            [
              "USA"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
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
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "UK"
            ],
            [
              "USA"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
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
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "NA"
            ],
            [
              "UK"
            ],
            [
              "USA"
            ]
          ],
          "columns": [
            "country"
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
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "NA"
            ],
            [
              "UK"
            ],
            [
              "USA"
            ]
          ],
          "columns": [
            "country"
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
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "UK"
            ],
            [
              "USA"
            ],
            [
              "UK"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
            "Yesterday",
            "Respect",
            "NA"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "UK"
            ],
            [
              "USA"
            ],
            [
              "UK"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
            "Yesterday",
            "Respect",
            "NA"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "USA"
            ],
            [
              "UK"
            ],
            [
              "NA"
            ],
            [
              "UK"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
            "Respect",
            "NA",
            "Imagine",
            "Yesterday"
          ],
          "selected": []
        }
      ]
    },
    {
      "grids": [
        {
          "name": "Input keys",
          "values": [
            [
              "Imagine",
              "NA"
            ],
            [
              "Yesterday",
              "UK"
            ],
            [
              "Respect",
              "USA"
            ],
            [
              "NA",
              "UK"
            ]
          ],
          "columns": [
            "track title",
            "country"
          ],
          "labels": [
            "John Lennon",
            "The Beatles",
            "Aretha Franklin",
            "Fleetwood Mac"
          ],
          "selected": [
            [
              0,
              1
            ],
            [
              3,
              0
            ]
          ],
          "labelWidth": 160
        },
        {
          "name": "Join result",
          "values": [
            [
              "USA"
            ],
            [
              "UK"
            ],
            [
              "NA"
            ],
            [
              "UK"
            ]
          ],
          "columns": [
            "country"
          ],
          "labels": [
            "Respect",
            "NA",
            "Imagine",
            "Yesterday"
          ],
          "selected": []
        }
      ]
    }
  ],
  "output": [
    [],
    [
      "2"
    ],
    [],
    [
      "3"
    ],
    [],
    [
      "3"
    ],
    [],
    [
      "4"
    ]
  ],
  "captions": [
    "Inner keeps only the two matching artists.",
    "The inner join has two rows.",
    "Left also keeps Imagine, with a missing country.",
    "The left join has three rows.",
    "Right also keeps Fleetwood Mac, with no track title.",
    "The right join has three rows.",
    "Outer keeps both unmatched keys as well as the matches.",
    "The outer join has four rows."
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="300px">

```python {1-1|1-2|1-3|1-4|1-5|1-6|1-7|1-8}
inner = tracks.merge(artists, on="artist", how="inner")
print(len(inner))
left = tracks.merge(artists, on="artist", how="left")
print(len(left))
right = tracks.merge(artists, on="artist", how="right")
print(len(right))
outer = tracks.merge(artists, on="artist", how="outer")
print(len(outer))
```

<template #visual="{ step }">
<ArrayGrid :run="run" :step="step" />
</template>
</DataStructuresRun>
