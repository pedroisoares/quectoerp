#!/usr/bin/env bash
# Checks that every non-merge commit in a range carries a DCO sign-off from its author.
# Usage: check-dco.sh <base-ref> <head-ref>
# See CONTRIBUTING.md, "Developer Certificate of Origin (DCO)", and docs/adr/0002-license-agpl-and-dco.md.
set -euo pipefail

base="${1:?usage: check-dco.sh <base-ref> <head-ref>}"
head="${2:?usage: check-dco.sh <base-ref> <head-ref>}"

failed=0
checked=0
while IFS= read -r sha; do
  [ -n "$sha" ] || continue
  checked=$((checked + 1))
  author_name="$(git log -1 --format='%an' "$sha")"
  author_email="$(git log -1 --format='%ae' "$sha")"
  subject="$(git log -1 --format='%s' "$sha")"
  expected="Signed-off-by: ${author_name} <${author_email}>"
  # Trailers only, so a sign-off quoted in the body does not count.
  if git log -1 --format='%(trailers:key=Signed-off-by,unfold)' "$sha" | grep -qiF -- "<${author_email}>"; then
    echo "ok      ${sha:0:12} ${subject}"
  else
    echo "MISSING ${sha:0:12} ${subject}"
    echo "        expected trailer: ${expected}"
    failed=$((failed + 1))
  fi
done < <(git rev-list --no-merges "${base}..${head}")

echo
if [ "$failed" -gt 0 ]; then
  echo "${failed} of ${checked} commit(s) are not signed off by their author."
  echo "Fix with: git rebase --signoff ${base} && git push --force-with-lease"
  echo "Corrija com: git rebase --signoff ${base} && git push --force-with-lease"
  exit 1
fi
echo "All ${checked} commit(s) are signed off. / Todos os ${checked} commit(s) estão assinados."
