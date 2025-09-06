import React, { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeNews = async () => {
    if (!url) return alert("Please enter a news URL");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await res.json();
      setResult(JSON.parse(data.analysis));
    } catch (err) {
      console.error(err);
      alert("Error analyzing news");
    }

    setLoading(false);
  };

  const getSentimentEmoji = (sentiment) => {
    if (sentiment === "positive") return "😊";
    if (sentiment === "neutral") return "😐";
    if (sentiment === "negative") return "😡";
    return "";
  };

  const getCategoryColor = (category) => {
    switch (category) {
      case "Tech":
        return "bg-blue-200 text-blue-800";
      case "Politics":
        return "bg-red-200 text-red-800";
      case "Sports":
        return "bg-green-200 text-green-800";
      default:
        return "bg-gray-200 text-gray-800";
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6">📰 News Analyzer</h1>

      <input
        type="text"
        placeholder="Paste news URL here..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="border p-3 w-full max-w-xl mb-4 rounded"
      />

      <button
        onClick={analyzeNews}
        className="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600 mb-6"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div className="bg-white p-6 rounded shadow w-full max-w-xl space-y-4">
          <h2 className="text-xl font-bold mb-2">Analysis Result:</h2>

          <div>
            <strong>Summary:</strong>
            <p className="mt-1">{result.summary}</p>
          </div>

          <div className="flex items-center space-x-2">
            <strong>Sentiment:</strong>
            <span
              className={`px-2 py-1 rounded ${
                result.sentiment === "positive"
                  ? "bg-green-200 text-green-800"
                  : result.sentiment === "neutral"
                  ? "bg-yellow-200 text-yellow-800"
                  : "bg-red-200 text-red-800"
              }`}
            >
              {getSentimentEmoji(result.sentiment)} {result.sentiment}
            </span>
          </div>

          <div className="flex items-center space-x-2">
            <strong>Category:</strong>
            <span className={`px-2 py-1 rounded ${getCategoryColor(result.category)}`}>
              {result.category}
            </span>
          </div>

          <div>
            <strong>Reliability:</strong>
            <div className="w-full bg-gray-200 rounded h-4 mt-1">
              <div
                className="h-4 rounded bg-blue-500"
                style={{ width: `${result.reliability || 0}%` }}
              />
            </div>
            <span>{result.reliability || 0}%</span>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
