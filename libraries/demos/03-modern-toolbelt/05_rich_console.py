from rich.console import Console

console = Console()
console.rule("Playlist")
console.print("[bold]Now playing [cyan]Imagine[/][/] ")
console.print({"title": "Imagine", "duration_s": 183})
