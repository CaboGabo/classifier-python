const fs = require("fs");

function getDataset(filename) {
  fs.readFile(`./datasets/${filename}.txt`, "utf8", (err, data) => {
    if (err) throw err;
    let phrases = [];
    let lines = [];
    let string = "";
    for (const letter of data) {
      if (letter === "\t" || letter === "\r") {
        continue;
      }
      if (letter === "\n") {
        lines.push(string);
        string = "";
        continue;
      }
      string += letter;
    }

    for (const line of lines) {
      let [text, tag] = line
        .split("manager.addDocument('es',")[1]
        .split(")")[0]
        .split(",");

      text = text.slice(2, -1);
      tag = tag.slice(2, -1);

      phrases.push(JSON.stringify({
        text,
        tag
      }));
    }

    fs.writeFile(`./outputs/${filename}.txt`, phrases, err => {
      if (err) throw err;
      console.log("File saved");
    });
  });
}

let fileNames = ['datasetA2', 'datasetA3', 'datasetA4', 'datasetA6', 'datasetA7', 'datasetA8', 'datasetA9', 'datasetB1', 'datasetB4', 'datasetB6', 'datasetC1'];
for (const filename of fileNames) {
  getDataset(filename);
}