const fs = require('fs');
const path = require('path');
const cssDirectory = path.resolve(__dirname, '../static/css');

// Obtenha a lista de arquivos CSS no diretório
fs.readdir(cssDirectory, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  // Filtrar arquivos com a extensão .css
  const cssFiles = files.filter((file) => path.extname(file) === '.css');

  if (cssFiles.length === 0) {
    console.error('Nenhum arquivo CSS encontrado.');
    return;
  }

  // Obter o nome do último arquivo CSS modificado
  const latestFile = cssFiles.reduce((latest, file) => {
    const filePath = path.join(cssDirectory, file);
    const stats = fs.statSync(filePath);

    if (!latest || stats.mtime > latest.stats.mtime) {
      return {
        file,
        stats,
      };
    }

    return latest;
  }, null);

  if (!latestFile) {
    console.error('Nenhum arquivo CSS encontrado.');
    return;
  }

  const fileName = latestFile.file;
  console.log(`Arquivo CSS gerado: ${fileName}`);
});
