const fs = require("fs");
const google = require('./google/google');

function getDataset(filename) {
  fs.readFile(`./datasets/${filename}.txt`, "utf8", async (err, data) => {
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
      if (line.startsWith("//") || line === "\n") {
        continue;
      }
      let [text, tag] = line
        .split("manager.addDocument('es',")[1]
        .split(")")[0]
        .split(",");

      text = text.slice(2, -1);
      tag = tag.slice(2, -1);

      const results = await google.analyze(text);

      phrases.push(JSON.stringify({
        text,
        ...results,
        tag
      }));
    }

    fs.writeFile(`./outputs/${filename}.txt`, phrases, err => {
      if (err) throw err;
      console.log("File saved");
    });
  });
}