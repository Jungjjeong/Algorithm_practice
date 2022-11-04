function solution(s) {
  let stack = [];

  s.split('').forEach((str) => {
    if (stack.length === 0) {
      stack.push(str);
      return;
    }

    if (stack[stack.length - 1] === str) stack.pop();
    else stack.push(str);
  });

  return stack.length === 0 ? 1 : 0;
}
