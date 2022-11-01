function solution(numbers) {
  return numbers.map((num) => {
    if (num % 2 === 0) return num + 1;

    const currentNum = '0' + num.toString(2);
    const idx = currentNum.lastIndexOf('01');
    return parseInt(
      currentNum.substr(0, idx) + '10' + currentNum.substr(idx + 2),
      2
    );
  });
}
