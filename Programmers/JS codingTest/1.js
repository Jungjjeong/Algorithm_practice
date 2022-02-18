process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data;
  var i = 1;
  var str = "";
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
      str += "*";
    }
    console.log(str);
    str = "";
  }
});
