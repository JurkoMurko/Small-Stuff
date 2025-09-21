const express = require('express');
const app = express();
app.listen(5500, () => console.log("lisening at 5500"));
app.use(express.static('public'));