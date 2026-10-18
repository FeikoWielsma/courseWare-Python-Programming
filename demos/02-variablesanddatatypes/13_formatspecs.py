photo_id = 421
size_mb = 8.537
print(f"Photo {photo_id:05d}: {size_mb:6.2f} MB")
print(f"[{'Imagine':<10}]")  # [Imagine   ]
print(f"[{'Imagine':^10}]")  # [ Imagine  ]
print(f"[{'Imagine':>10}]")  # [   Imagine]
print(f"{1234567:,.0f} pixels")  # 1,234,567 pixels
print(f"{0.25:.0%} complete")  # 25% complete

# Recognise these older forms; use f-strings in new code.
print("Photo %05d: %6.2f MB" % (photo_id, size_mb))
print("Photo {:05d}: {:6.2f} MB".format(photo_id, size_mb))
