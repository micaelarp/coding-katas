# Helper Scripts

This directory contains scripts to facilitate the Pair Programming flow and rotation.

## `pp_commit.sh`
**Usage**: `bash scripts/pp_commit.sh [Pair Details]`

- Stages all changes (`git add -A`).
- Commits with a timestamped message: `PP rotation | YYYY-MM-DD HH:MM:SS | [Pair Details]`.
- Pushes to the current branch.
- Useful for quick commits when switching roles without running the full test suite (though running tests is recommended).

## `pp_rotate.sh`
**Usage**: `bash scripts/pp_rotate.sh [Optional Message]`

- **Runs Tests**: Executes `make test` (pytest) first.
- **Commits & Pushes**: If tests pass, calls `pp_commit.sh` to commit and push.
    - Example: `bash scripts/pp_rotate.sh "Refactored movement logic"`
- **Fails Safe**: If tests fail, it aborts the rotation so you can fix the code before handing over.

## `app-command.sh`
(Legacy/System script) - Used by the Docker container entrypoint.
