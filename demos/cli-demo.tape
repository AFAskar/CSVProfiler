# Generate a small CLI demo GIF for README usage
# Run via: vhs demos/cli-demo.tape

Require jq
Require less

Output "docs/cli-demo.gif"

# Keep the recording compact/readable
Set Width 900
Set Height 520
Set FontSize 16


# Run the CLI
Type "csv-profiler cli data/data.csv -o output/demo -f both"
Enter
Sleep 1s

# Show generated files
Type "ls output/demo/"
Enter
Sleep 2s

# show the generate file with styling (scroll)
Type "jq . output/demo/report.json | less -SR"
Enter
Sleep 1s

PageDown 3
Sleep 700ms
PageDown 3
Sleep 700ms

Type "q"
Sleep 500ms
