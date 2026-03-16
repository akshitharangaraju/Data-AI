export default function ChatUI({
  messages,
  prompt,
  loading,
  onPromptChange,
  onSubmit,
  result
}) {

  return (

    <section className="flex h-[80vh] flex-col rounded-3xl border border-white/10 bg-white/5 shadow-panel backdrop-blur">

      <div className="border-b border-white/10 px-6 py-5">

        <h2 className="text-xl font-semibold text-white">Chat Interface</h2>

        <p className="text-sm text-slate-300">
          Ask the agent team to research, code, and explain.
        </p>

      </div>

      <div className="flex-1 space-y-4 overflow-y-auto px-6 py-5">

        {messages.map((message) => (

          <div
            key={message.id}
            className={`max-w-3xl rounded-2xl px-4 py-3 text-sm leading-6 ${
              message.role === "user"
                ? "ml-auto bg-signal text-slate-950"
                : "bg-slate-900/80 text-slate-100"
            }`}
          >

            <div className="mb-1 text-xs uppercase tracking-[0.2em] text-slate-300">

              {message.role === "user" ? "You" : "Platform"}

            </div>

            <div className="whitespace-pre-wrap">{message.content}</div>

          </div>

        ))}

        {/* IMAGE RESULTS */}

        {result?.images && (

          <div className="grid grid-cols-3 gap-4">

            {result.images.map((img, index) => (

              <img
                key={index}
                src={img}
                alt="result"
                className="rounded-xl"
              />

            ))}

          </div>

        )}

      </div>

      <form onSubmit={onSubmit} className="border-t border-white/10 p-4 flex gap-3">

        <input
          value={prompt}
          onChange={onPromptChange}
          placeholder="Ask a question..."
          className="flex-1 rounded-xl bg-slate-900 px-4 py-2 text-white"
        />

        <button
          type="submit"
          disabled={loading}
          className="rounded-xl bg-cyan-500 px-4 py-2 text-black"
        >
          {loading ? "Thinking..." : "Send"}
        </button>

      </form>

    </section>

  );
}