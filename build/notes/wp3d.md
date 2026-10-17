# WP3d notes : modules 10 and 11

## Done
- 10 : tracked .db files removed; demo03/04 (re)create Cars, readers say so; every demo
  closes its connection; `with con:` claims corrected; row_factory slide (demo07) moved
  before fetchone (demo08); DB API module list current; commit in demo11 live.
- 11 : rewritten. Demos 01 simplestclass, 02 employee, 03 classattributes, 04 strrepr,
  05 publicattributes, 06 computedproperty, 07 validatingsetter, 08 internalattributes,
  09 inheritance. Old 02-11 removed. Section 6 followed on slides 05-07 + Rule of Thumb.
- Gates: check-fences, ruff clean; lint prints no warnings but crashes at the final
  browser.close() with EBUSY on the puppeteer temp profile (Windows).

## Left
- Coordinator : .gitignore entry for demos/10-python-database-access/*.db

## Decisions
- getattr/setattr shown with the name in a variable (the real use, and ruff B009/B010 clean).
- Encapsulation get/set diagram dropped; a new property -> _length diagram on Rule of Thumb.
- OO terminology slide cut (function overloading is not a Python feature).
