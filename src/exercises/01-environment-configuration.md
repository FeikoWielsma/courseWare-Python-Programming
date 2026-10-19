# Exercise 1 : Python Intro

Write a short Python program, change what it displays, and run it again. The aim is to practise working with a file in the editor and seeing the result in the terminal. The `wordle` folder you create here becomes your game project from Exercise 2 onwards.

Start with a folder of your own for course work. There is no starter for this exercise because you create the project here. The finished version is in `solutions/01-environment-configuration/`. From Exercise 2 onwards, a starter folder is also available if you need a fresh starting point.

If you are using the prepared GitHub Codespace, Python, uv and VS Code are already available. Start at Step 2 in the browser editor.

---

### Step 1 : Prepare the tools

Install Visual Studio Code from <https://code.visualstudio.com/>. Open it, select the Extensions icon on the left, search for `Python`, and install the extension published by Microsoft.

Python is the application that runs your code. The tool `uv` installs Python and starts it for your project. On Windows, open the Start menu, search for PowerShell and open it. Paste this command and press Enter :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On macOS or Linux, open the Terminal application and use this command instead :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen PowerShell or Terminal after the installation. Enter the following command and press Enter to install Python :

```bash
uv python install 3.14
```

Wait for the terminal prompt to return before entering another command. If `uv` is not recognised, close and reopen the terminal application. The slides *Preparing Python* and *Editor Setup* show these installation steps.

### Step 2 : Create the project folder

In VS Code, choose `File > Open Folder`. Create or select a folder for your course work, then open it. In Codespaces, use the folder already open in the editor. If VS Code asks whether you trust the folder, confirm for your own course-work folder.

Choose `Terminal > New Terminal`. A terminal panel opens below the editor. Commands go in this panel, after the prompt, rather than in a Python file. Enter these two commands separately, pressing Enter after each :

```bash
uv init --bare --python 3.14 wordle
cd wordle
```

The first command creates a project folder named `wordle` and a settings file named `pyproject.toml`. The second command moves the terminal into that folder. You do not need to edit the settings file.

Choose `File > Open Folder` again and open the new `wordle` folder. Its `pyproject.toml` should be visible in the Explorer panel on the left. Choose `Terminal > New Terminal` again so the new terminal also starts inside `wordle`.

:::hint
The slide *Creating a Project* shows `uv init` and `cd`. The slide *The Editor and the Terminal* identifies the Explorer panel and the terminal.
:::

### Step 3 : Write and run a message

In the Explorer panel, select New File and name it `wordle.py`. Include the `.py` ending. Type this line in the editor area :

```python
print("Welcome to Wordle!")
```

Choose `File > Save`, or press `Ctrl+S` on Windows and Linux, or `Cmd+S` on macOS. Then click in the terminal panel and run :

```bash
uv run python wordle.py
```

The first run may show setup messages. The program then displays :

```text
Welcome to Wordle!
```

`print()` displays the text between the quotes. The quotes and parentheses are Python code and do not appear in the output. The terminal prompt returns when the program finishes.

:::hint
The slides *Creating a Python File* and *Running a Python File* show where to type the code, how to save it and where to enter the run command.
:::

If Python reports `can't open file`, check that `wordle.py` is saved in the `wordle` folder and that the terminal is in that same folder. The slide *Finding a File to Run* explains this check.

### Step 4 : Change the message

Change the text inside the quotes so the program displays `Wordle is ready.`. Save the file and run the same terminal command again.

:::hint
The slide *Changing a Program* shows the edit, save and run cycle. Keep `print(`, the matching quotes and the closing `)` around the new message.
:::

:::output
```text
Wordle is ready.
```
:::

:::solution
```python
print("Wordle is ready.")
```
:::

### Step 5 : Add another statement

Add a second line that displays `Guess a five-letter word.`. Predict which message appears first, then save and run the program. Does the order match your prediction?

:::hint
The slide *Statements Run in Order* shows two `print()` statements. Put each statement on its own line, starting at the left edge of the editor.
:::

:::output
```text
Wordle is ready.
Guess a five-letter word.
```
:::

:::solution
```python
print("Wordle is ready.")
print("Guess a five-letter word.")
```
:::

### Step 6 : Add a comment

Add this comment above the two statements, then save and run the program again :

```python
# Show the instructions before the game starts.
```

Does the comment appear in the output? Compare the result with the previous run.

:::hint
The slide *Comments in Python* shows a line starting with `#`. Python ignores that line, so the two messages should stay the same.
:::

### Step 7 : Read and repair an error

On the first `print()` line, remove the closing quote after the full stop. Leave the closing parenthesis in place. Save and run the file.

Find the filename, line number and `SyntaxError` in the error message. Python checks the syntax before running the script, so neither message appears. The line number depends on where you put the comment and any blank lines.

Put the closing quote back, save, and run the file again. The two messages should return. The earlier error remains in the terminal; read the output from the latest run.

:::hint
The slides *Reading a Syntax Error* and *Correcting and Rerunning* show the same missing-quote problem. Both ends of the string need a double quote.
:::

:::solution
```python
# Show the instructions before the game starts.
print("Wordle is ready.")
print("Guess a five-letter word.")
```
:::

Keep the `wordle` folder and its `wordle.py` file for Exercise 2. No word list or extra package is needed yet.

### If time permits

- Swap the two `print()` lines. Predict the output, then save and run the file to check it. Restore their original order afterwards.
- Add a blank line between the statements. Save and run again. Does a blank line in the source add a blank line to the output?

:::hint
The slides *Statements Run in Order* and *Comments in Python* explain statement order and blank lines.
:::
