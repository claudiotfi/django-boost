const fs = require('fs');
const path = require('path');

const cssFilePath = path.resolve(__dirname, '../static/css/styles.css');
const suffix = '-' + Date.now();

fs.rename(cssFilePath, `${cssFilePath.replace('.css', `${suffix}.css`)}`, (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`Sufixo "${suffix}" adicionado ao arquivo CSS.`);
});
