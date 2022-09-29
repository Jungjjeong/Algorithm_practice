function solution(s) {
  var answer = [];
  const splitS = s
    .substr(1, s.length - 2)
    .split('{')
    .map((str) =>
      str
        .split(',')
        .filter((str) => str.length > 0)
        .map((str) => str.replace('}', ''))
    )
    .filter((str) => str.length > 0)
    .sort((a, b) => a.length - b.length);

  splitS.forEach((strArr, idx) => {
    let addStr = [...strArr];

    if (answer.length !== 0) {
      answer.forEach((a) => (addStr = addStr.filter((add) => add !== a)));
    }

    answer.push(addStr[0]);
  });

  return answer.map((a) => parseInt(a));
}
