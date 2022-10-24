function checkArr(skillArr, treeArr) {
  if (treeArr.length === 0) return true;
  if (skillArr[0] !== treeArr[0]) return false;

  const skill = skillArr.join('');
  const tree = treeArr.join('');
  if (skill.indexOf(tree) === -1) return false;

  return true;
}

function solution(skill, skill_trees) {
  let answer = 0;
  const skillArr = skill.split('');

  skill_trees.forEach((skillTree) => {
    const skillTreeArr = skillTree.split('');
    const filterArr = skillTreeArr.filter(
      (tree) => skillArr.indexOf(tree) !== -1
    );
    if (checkArr(skillArr, filterArr)) answer += 1;
  });

  return answer;
}
