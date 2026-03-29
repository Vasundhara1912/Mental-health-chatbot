import { useState, useRef, useEffect } from "react";
import MoodBadge from "./MoodBadge";

export default function ChatWindow({ messages, loading, onSend }) {
  const [input, setInput] = useState("");
  const bottomRef = useRef(null);

  // Auto-scroll to latest message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="chat-window">
      {/* Message List */}
      <div className="message-list">
        {messages.map((msg) => (
          <div key={msg.id} className={`message-row ${msg.sender}`}>
            {msg.sender === "bot" && (
              <div className="avatar" style={{ background: msg.color || "#8b5cf6" }}>
                {msg.emoji || "🤖"}
              </div>
            )}
            <div className="bubble-group">
              <div className={`bubble ${msg.sender}`}>
                {msg.text}
              </div>
              {/* Mood badge (only for bot messages with a detected emotion) */}
              {msg.sender === "bot" && msg.emotion && (
                <MoodBadge emotion={msg.emotion} emoji={msg.emoji} color={msg.color} />
              )}
              {/* Relaxation tip card */}
              {msg.sender === "bot" && msg.tip && (
                <div className="tip-card">
                  <span className="tip-label">💡 Tip for you</span>
                  <p>{msg.tip}</p>
                </div>
              )}
            </div>
            {msg.sender === "user" && (
              <div className="avatar user-avatar">🙋</div>
            )}
          </div>
        ))}

        {/* Typing indicator */}
        {loading && (
          <div className="message-row bot">
            <div className="avatar" style={{ background: "#8b5cf6" }}>🤖</div>
            <div className="bubble bot typing">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input Bar */}
      <form className="input-bar" onSubmit={handleSubmit}>
        <textarea
          className="chat-input"
          placeholder="Share how you're feeling today..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          rows={1}
          disabled={loading}
        />
        <button
          type="submit"
          className="send-btn"
          disabled={loading || !input.trim()}
          aria-label="Send message"
        >
          ➤
        </button>
      </form>
      <p className="disclaimer">
        This is an AI companion, not a substitute for professional mental health care.
        If you are in crisis, please contact a counselor or helpline.
      </p>
    </div>
  );
}
