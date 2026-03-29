const EMOTION_LABELS = {
  happy:   "Feeling Happy",
  sad:     "Feeling Sad",
  anxious: "Feeling Anxious",
  angry:   "Feeling Angry",
  neutral: "Feeling Neutral",
};

export default function MoodBadge({ emotion, emoji, color }) {
  const label = EMOTION_LABELS[emotion] || emotion;

  return (
    <div
      className="mood-badge"
      style={{
        borderColor: color,
        color: color,
        background: `${color}18`, // 10% opacity tint
      }}
    >
      <span className="mood-emoji">{emoji}</span>
      <span className="mood-label">Detected mood: <strong>{label}</strong></span>
    </div>
  );
}
