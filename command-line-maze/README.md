Welcome to the travel maze made by Cici for IS 310!

This maze is built around Jules Verne's *Around the World in Eighty Days*. Navigate from London to New York using only real details from the book, everything you need is in the clue files or in the full text (around-the-world-in-80-days.txt) inside the zip.

## Rules
- Command line only, no file explorer.
- Read each clues.txt before choosing a folder.
- A folder containing an empty file (0 bytes/words) means you took a wrong turn. Go back and try again.
- There is one hidden folder in the maze.

## Windows/PowerShell users
Unzip the maze, then run .\hide-dotfiles.ps1 first. If you hit a permissions error, run this:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\hide-dotfiles.ps1


## Useful commands
- `cd foldername` to move into a folder
- `cat clues.txt` (Mac/Linux) or `Get-Content clues.txt` (PowerShell) to read a clue
- `ls -a` (Mac/Linux) or `Get-ChildItem -Force` (PowerShell) to reveal hidden files

Good luck!