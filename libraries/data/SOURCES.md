# Teaching data

`track-catalogue.json` records 40 real songs, selected edition names and Apple
catalogue URLs, retrieved 2026-10-18. Durations describe those recordings; other
editions, including examples in the fundamentals, may differ. The generator's
docstring records rounding. No lyrics, audio or album artwork are included.

Genres are broad teaching categories. Play counts, last-played dates, listening
events and the days-by-hours grid are invented personal history, not streaming
statistics. `tracks-import.csv` deliberately adds a duplicate title and a missing
duration for the library-check exercise. The normal `tracks.csv` has complete
durations and three missing last-played dates.

`artists.csv` is a small historical lookup, not a current roster. `formed` applies
to groups only; solo artists have an empty value. `members` describes the familiar
recording lineup (four Beatles, four Queen members, five Oasis and Fleetwood Mac
members, two Daft Punk members). John Lennon is deliberately absent and Fleetwood
Mac has no tracks, so join types produce different results. Artist background:
[The Beatles](https://www.thebeatles.com/), [Queen](https://www.queenonline.com/),
[Oasis](https://oasisinet.com/), [Daft Punk](https://www.daftpunk.com/) and
[Fleetwood Mac](https://www.fleetwoodmacofficial.com/).

`photo-source.jpg` is NASA's 2002 Blue Marble western-hemisphere composite,
credited to NASA's Earth Observatory. It combines satellite observations; it is
not a single exposure. Source:
[NASA Blue Marble 2002](https://science.nasa.gov/resource/blue-marble-2002/),
[original JPEG](https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57723/globe_west_2048.jpg).
NASA imagery is generally available for educational reuse under its
[media guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/).
`photo.png` is a 64 by 48 crop for array examples, rebuilt from the original.

Rebuild offline from the repository root:

```bash
uv run --project libraries python tools/libraries/make-data.py
```
