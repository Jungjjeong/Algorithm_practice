function solution(operations) {
  let answer = [];

  operations.forEach((o) => {
    const [oper, num] = o.split(' ');
    const intNum = parseInt(num);

    if (oper === 'I') answer.push(intNum);
    else if (oper === 'D') {
      if (intNum === 1) answer.pop();
      else if (intNum === -1) answer.shift();
    }

    answer.sort((a, b) => a - b);
  });

  return answer.length === 0
    ? [0, 0]
    : [Math.max(...answer), Math.min(...answer)];
}
