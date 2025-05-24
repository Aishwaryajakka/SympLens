const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());

// Routes
app.get('/', (req, res) => {
  res.send('SymLens backend is live');
});

// Example route for symptom processing
app.post('/api/render', (req, res) => {
  const { description } = req.body;
  // Connect to AI module here (placeholder)
  res.json({ image: "base64-encoded-image-placeholder", prompt: description });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
