function solution(files) {
  return files.sort((a, b) => {
    const aNum = a.match(/\d+/)[0].replace(/^0+/, '');
    const bNum = b.match(/\d+/)[0].replace(/^0+/, '');
    const compareAHead = a.match(/^\D+/)[0].toLowerCase();
    const compareBHead = b.match(/^\D+/)[0].toLowerCase();

    if (compareAHead !== compareBHead) {
      return compareBHead < compareAHead ? 1 : -1;
    }

    return aNum - bNum;
  });
}
