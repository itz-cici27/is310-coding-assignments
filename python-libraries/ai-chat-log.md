# AI Chat Log

## Summary of how I used AI

I uploaded the assignment page and asked Claude to help me work through the assignment step by step. Claude explained that having it generate code would put me in Pathway 2, and I chose that pathway. I chose a social media use diary as my topic because it connects to my group project on social media and academic performance, and it could work as a pilot for the diary study in our Milestone 2 proposal. I chose CSV as the file format.

## What Claude contributed

- **`cli_data_entry.py`:** Claude wrote the CLI script, which shows example entries in a Rich table, collects each field with validation (date format, minutes above 0, listed choices), asks the user to confirm each entry and re-enter it if wrong, saves confirmed entries to `social_media_diary.csv`, and prints the full file path.
- **`social_media_diary.html`:** Claude wrote the HTML version with the same fields, required-field validation, a review step before saving, a table of saved entries, and a CSV download.
- **Testing and fixes:** Claude tested both versions and fixed small issues (case-insensitive choices, "1 entry" vs "1 entries," dates wrapping in the HTML table).
- **Supporting files:** Claude drafted `requirements.txt`, the README, and this log.

## Learning and troubleshooting

I also asked Claude to teach me the assignment step by step. It laid out this roadmap:

1. Set up a virtual environment and install Rich
2. Display example data in a Rich table
3. Collect one diary entry from the user
4. Show the entry back and ask the user to confirm it (re-enter if wrong)
5. Loop so the user can add multiple entries
6. Save confirmed entries to a CSV file and print its full path
7. Build the HTML form
8. Add JavaScript for validation, review, and a records table
9. Add the CSV download button
10. Write `requirements.txt`, the README, and this log, then push and peer test