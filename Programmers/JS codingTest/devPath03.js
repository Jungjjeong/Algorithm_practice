function solution(pixels) {
  const alphabetObj = {
    111101101101111: 0,
    110010010010111: 1,
    111001111100111: 2,
    111001111001111: 3,
    101101111001001: 4,
    111100111001111: 5,
    111100111101111: 6,
    111101001001001: 7,
    111101111101111: 8,
    111101111001111: 9,
  };
  let answer = [];

  const splitP = pixels.map((pixel) => {
    const pixelLen = pixel.length;
    const pixelArr = [];

    for (let i = 2; i < pixelLen; i += 3) {
      pixelArr.push([pixel[i - 2], pixel[i - 1], pixel[i]]);
    }

    return pixelArr;
  });

  for (let j = 0; j < splitP[0].length; j += 1) {
    const alphabetArr = [];

    for (let i = 0; i < splitP.length; i += 1) {
      alphabetArr.push(splitP[i][j].join(''));
    }

    answer.push(alphabetArr.join(''));
  }

  return answer.map((a) => alphabetObj[a]).join('');
}
