function solution(numbers, hand) {
  const keypad = [
    [3, 1],
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
  ];
  let rightHand = [3, 2];
  let leftHand = [3, 0];
  let answer = '';

  numbers.forEach((num) => {
    const keyCoord = keypad[num];
    if (num === 1 || num === 4 || num === 7) {
      leftHand = keyCoord;
      answer += 'L';
    } else if (num === 3 || num === 6 || num === 9) {
      rightHand = keyCoord;
      answer += 'R';
    } else {
      const rightHandDistance =
        Math.abs(rightHand[0] - keyCoord[0]) +
        Math.abs(rightHand[1] - keyCoord[1]);
      const leftHandDistance =
        Math.abs(leftHand[0] - keyCoord[0]) +
        Math.abs(leftHand[1] - keyCoord[1]);

      if (rightHandDistance > leftHandDistance) {
        answer += 'L';
        leftHand = keyCoord;
      } else if (rightHandDistance < leftHandDistance) {
        answer += 'R';
        rightHand = keyCoord;
      } else {
        if (hand === 'right') {
          answer += 'R';
          rightHand = keyCoord;
        } else {
          answer += 'L';
          leftHand = keyCoord;
        }
      }
    }
  });

  return answer;
}
