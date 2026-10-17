sites = ["AMS", "RTM"]
counts = dict.fromkeys(sites, 0)
print(counts)  # {'AMS': 0, 'RTM': 0}
groups: dict[str, list[str]] = {site: [] for site in sites}
groups["AMS"].append("web01")
print(groups)  # {'AMS': ['web01'], 'RTM': []}
