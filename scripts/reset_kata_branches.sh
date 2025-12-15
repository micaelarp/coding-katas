#!/bin/bash

# List of branches to reset (edit as needed)
BRANCHES=("kata-base" "kata-template" "kata-solid" "kata-ddd")

# Base branch to reset from
BASE_BRANCH="main"

# If an argument is provided, only reset that branch
if [ -n "$1" ]; then
  BRANCHES=("$1")
fi

# Fetch latest changes from remote
echo "Fetching latest changes from origin..."
git fetch origin

for BRANCH in "${BRANCHES[@]}"; do
  echo "\n---"
  echo "Resetting branch: $BRANCH to $BASE_BRANCH"
  # Checkout the branch (create if doesn't exist)
  if git show-ref --verify --quiet refs/heads/$BRANCH; then
    git checkout $BRANCH
  else
    git checkout -b $BRANCH origin/$BASE_BRANCH
  fi
  # Reset to base branch
  git reset --hard origin/$BASE_BRANCH
  # Force push to remote
  git push origin $BRANCH --force
  echo "Branch $BRANCH has been reset to $BASE_BRANCH and pushed to origin."
done

echo "\nAll specified branches have been reset to $BASE_BRANCH."

