function solution(s) {
  return s
    .split(' ')
    .map((str) => {
      if (!str) return str;

      const strSplit = str.split('');
      return (
        strSplit[0].toUpperCase() + strSplit.slice(1).join('').toLowerCase()
      );
    })
    .join(' ');
}
