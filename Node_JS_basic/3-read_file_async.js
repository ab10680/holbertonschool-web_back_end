const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .map((line) => line.trim())
        .filter((line) => line.length > 0);

      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      const students = lines.slice(1); // skip header
      console.log(`Number of students: ${students.length}`);

      const fields = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      for (const field of Object.keys(fields)) {
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
