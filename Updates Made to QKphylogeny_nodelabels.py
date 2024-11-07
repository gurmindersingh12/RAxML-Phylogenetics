## Updates Made to QKphylogeny_nodelabels.py

## The original script was written in Python 2, which uses some outdated syntax and functions that aren’t supported in Python 3. Below are the specific changes we made:

### Replacing string.replace(line, '\n', ''):
1. Original: `line = string.replace(line, '\n', '')`
2. Updated: `line = line.replace('\n', '')`
3. Reason: string.replace was removed in Python 3. Now, we use the replace method directly on the string object.

    Replacing string.split(line):
        Original: sline = string.split(line)
        Updated: sline = line.split()
        Reason: string.split was also removed in Python 3, so we use the split() method directly on the string.

    Replacing string.split(node, ':')[0]:
        Original: ID = string.split(node, ':')[0]
        Updated: ID = node.split(':')[0]
        Reason: We use split() directly on node to make the syntax compatible with Python 3.

    Updating Other string.replace Instances:
        Any other use of string.replace was similarly updated to call replace directly on the string object.
