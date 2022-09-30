function solution(progresses, speeds) {
  let answer = [];
  const completeProgress = progresses.map((progress, idx) =>
    Math.ceil((100 - progress) / speeds[idx])
  );

  let max = completeProgress[0];
  let count = 0;

  completeProgress.forEach((pro) => {
    if (max < pro) {
      max = pro;
      answer.push(count);
      count = 1;
    } else count += 1;
  });

  answer.push(count);
  return answer;
}
