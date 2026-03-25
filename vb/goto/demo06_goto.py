# Example 6: What happens when a label is missing:
from goto import goto, label
label .real
goto .unreal      # Raises a MissingLabelError exception.