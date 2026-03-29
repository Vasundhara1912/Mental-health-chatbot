import { useState } from "react";
import ChatWindow from "./ChatWindow";
import "./App.css";

export default function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: "bot",
      text: "Hi there 👋 I'm your Mental Health Companion. How are you feeling today? Feel free to share anything on your mind.",
      emotion: null,
      tip: null,
      emoji: "🤖",
      color: "#8b5cf6",
    },
  ]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (userText) => {
    if (!userText.trim()) return;

    // Add user message
    const userMsg = { id: Date.now(), sender: "user", text: userText };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      if (!res.ok) throw new Error("Server error");
      const data = await res.json();

      const botMsg = {
        id: Date.now() + 1,
        sender: "bot",
        text: data.message,
        emotion: data.emotion,
        tip: data.tip,
        emoji: data.emoji,
        color: data.color,
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: "bot",
          text: "Sorry, I'm having trouble connecting right now. Please make sure the backend is running on port 5000.",
          emotion: null,
          tip: null,
          emoji: "⚠️",
          color: "#ef4444",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <span className="header-icon">🧠</span>
          <div>
            <h1>Mental Health Companion</h1>
            <p>A safe space to share how you feel</p>
          </div>
        </div>
      </header>
      <ChatWindow messages={messages} loading={loading} onSend={sendMessage} />
    </div>
  );
}
