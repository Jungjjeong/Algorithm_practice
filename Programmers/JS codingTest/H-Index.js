function solution(citations) {
  if (citations.length === 1) return citations[0];

  const sortCitations = citations.sort((a, b) => b - a);

  for (let i = sortCitations[0]; i > -1; i -= 1) {
    const hCitations = sortCitations.filter((citation) => citation >= i).length;
    if (hCitations >= i) return i;
  }

  return 0;
}
