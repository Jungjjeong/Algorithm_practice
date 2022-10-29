function solution(brown, yellow) {
  for (let x = 2; x < brown / 2; x += 1) {
    const y = brown / 2 - x;
    const area = (x + 1) * (y + 1);

    if (area - brown === yellow)
      return y >= x ? [y + 1, x + 1] : [x + 1, y + 1];
  }
}
