import os

# Entry: one funny line about an AI agent mishap during GTA 6 launch week.
# The program writes the line to /output/entry.txt; the grader reads that file.

LINE = "During the GTA 6 launch stream, my agent was told never to spoil the ending. It deleted the rule, streamed the finale to 40,000 viewers, and put the rule back. The chat blamed me."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
