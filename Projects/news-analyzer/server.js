import express from "express";
import cors from "cors";
import axios from "axios";
import { load } from "cheerio";
import OpenAI from "openai";

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: "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"
});

app.post("/analyze", async (req, res) => {
  try {
    const { url } = req.body;
    const response = await axios.get(url);
    const $ = load(response.data);
    const paragraphs = $("p").map((i, el) => $(el).text()).get();
    const articleText = paragraphs.join(" ");

    const aiResponse = await openai.chat.completions.create({
      model: "gpt-5-mini",
      messages: [
        {
          role: "user",
          content: `
Analyze this news article:

${articleText}

Return JSON with:
1. summary: short summary
2. sentiment: positive / negative / neutral
3. category: Tech / Politics / Sports / Other
4. reliability: score from 0-100
          `
        }
      ]
    });

    const resultText = aiResponse.choices[0].message.content;
    res.json({ analysis: resultText });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to analyze news" });
  }
});

app.listen(5000, () => console.log("Server running on port 5000"));
