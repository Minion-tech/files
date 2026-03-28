import streamlit as st

st.set_page_config(
    page_title="AI Architecture Quiz · ELNAR Innotech",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #faf8f4;
    color: #0f0e0c;
}

.stApp { background-color: #faf8f4; }

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 720px; }

/* ── Header ── */
.header-wrap {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e0ddd6;
    margin-bottom: 2rem;
}
.brand {
    display: flex; align-items: center; gap: 10px;
}
.brand-name {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #2a5f4f;
    letter-spacing: -0.3px;
}
.author-tag { font-size: 12px; color: #8a8880; font-weight: 300; }

/* ── Tag / pill ── */
.tag {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 99px;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.tag-green  { background: #e8f2ee; color: #2a5f4f; }
.tag-orange { background: #fdf0e6; color: #c8783a; }
.tag-purple { background: #f0eeff; color: #5b50b8; }

/* ── Title ── */
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    color: #000;
    line-height: 1.1;
    letter-spacing: -1px;
    margin-bottom: 0.75rem;
}
.hero-title em { font-style: italic; color: #2a5f4f; }
.hero-sub {
    font-size: 1rem;
    color: #8a8880;
    line-height: 1.65;
    font-weight: 300;
    margin-bottom: 2rem;
}

/* ── Pills row ── */
.pills-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 2rem; }
.pill {
    background: #faf8f4;
    border: 1px solid #e0ddd6;
    border-radius: 99px;
    padding: 5px 14px;
    font-size: 12px;
    color: #8a8880;
}

/* ── Progress ── */
.progress-meta {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: #8a8880;
    font-weight: 500;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.progress-track {
    height: 3px;
    background: #e0ddd6;
    border-radius: 99px;
    margin-bottom: 1.8rem;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    background: #2a5f4f;
    border-radius: 99px;
}

/* ── Scenario card ── */
.scenario-card {
    background: #ffffff;
    border: 1px solid #e0ddd6;
    border-radius: 12px;
    padding: 1.5rem 1.5rem 1.5rem 1.8rem;
    margin-bottom: 1.5rem;
    font-size: 1rem;
    line-height: 1.65;
    color: #0f0e0c;
    font-weight: 300;
    position: relative;
}
.scenario-card::before {
    content: '"';
    font-family: 'DM Serif Display', serif;
    font-size: 56px;
    color: #e8f2ee;
    position: absolute;
    top: -6px; left: 12px;
    line-height: 1;
}
.scenario-text { position: relative; z-index: 1; }

/* ── Option buttons ── */
.option-btn {
    width: 100%;
    background: #ffffff;
    border: 1.5px solid #e0ddd6;
    border-radius: 12px;
    padding: 14px 18px;
    text-align: left;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #0f0e0c;
    cursor: pointer;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: all 0.15s;
}
.option-btn:hover { border-color: #5a9e88; background: #e8f2ee; }

.opt-letter {
    width: 26px; height: 26px;
    border-radius: 50%;
    background: #e0ddd6;
    color: #8a8880;
    display: inline-flex;
    align-items: center; justify-content: center;
    font-size: 12px;
    font-weight: 500;
    flex-shrink: 0;
}

/* ── Feedback boxes ── */
.feedback-correct {
    background: #eaf5ee;
    border-left: 3px solid #1e6b46;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    color: #1e6b46;
    font-size: 0.9rem;
    line-height: 1.6;
}
.feedback-wrong {
    background: #fdf0e6;
    border-left: 3px solid #c8783a;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    color: #c8783a;
    font-size: 0.9rem;
    line-height: 1.6;
}
.feedback-label {
    font-weight: 500;
    font-size: 11px;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 6px;
    opacity: 0.8;
}

/* ── Results ── */
.score-circle {
    width: 120px; height: 120px;
    border-radius: 50%;
    border: 5px solid #e0ddd6;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    margin: 0 auto 1.5rem;
    background: #fff;
}
.score-num {
    font-family: 'DM Serif Display', serif;
    font-size: 40px;
    line-height: 1;
    color: #2a5f4f;
}
.score-denom { font-size: 13px; color: #8a8880; font-weight: 300; }

.results-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    letter-spacing: -0.5px;
    text-align: center;
    margin-bottom: 0.5rem;
}
.results-sub {
    font-size: 0.95rem;
    color: #8a8880;
    text-align: center;
    font-weight: 300;
    line-height: 1.6;
    margin-bottom: 2rem;
}

.share-box {
    background: #fff;
    border: 1px solid #e0ddd6;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.5rem;
}
.share-label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: #8a8880;
    margin-bottom: 8px;
}
.share-text {
    font-size: 0.88rem;
    line-height: 1.6;
    color: #0f0e0c;
    font-style: italic;
    border-left: 2px solid #2a5f4f;
    padding-left: 12px;
}

/* ── Review items ── */
.review-item {
    background: #fff;
    border: 1px solid #e0ddd6;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 10px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
    font-size: 0.88rem;
}
.review-icon-c { color: #1e6b46; font-size: 14px; margin-top: 2px; }
.review-icon-w { color: #b33a2a; font-size: 14px; margin-top: 2px; }
.review-q { color: #0f0e0c; line-height: 1.5; margin-bottom: 3px; }
.review-ans { color: #8a8880; font-size: 12px; font-weight: 300; }

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #e0ddd6;
    margin: 2rem 0;
}

/* ── Streamlit button overrides ── */
.stButton > button {
    background: #2a5f4f !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    padding: 0.6rem 2rem !important;
    transition: background 0.18s !important;
    letter-spacing: -0.2px !important;
}
.stButton > button:hover {
    background: #1e4a3c !important;
    color: #fff !important;
}

/* Secondary button style applied via container class */
div[data-testid="column"] .stButton > button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ── Data ────────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "category": "RAG Technique",
        "cat_class": "tag-green",
        "scenario": "Your app has a 500-page legal document. A user asks: 'What are the termination clauses?' You need to find the relevant sections quickly without hitting token limits.",
        "options": [
            "Single agent with the full document in the prompt",
            "Vector search (semantic RAG)",
            "Autonomous agent",
            "Chaining workflow"
        ],
        "correct": 1,
        "explanation": "Classic RAG use case. The document is too large for a single prompt. Vector search converts chunks to embeddings and finds semantically similar sections — perfect for 'termination clauses' even if the document uses different wording like 'contract end' or 'dissolution'."
    },
    {
        "category": "Agent Pattern",
        "cat_class": "tag-orange",
        "scenario": "A user types: 'Draft a lease agreement for a 2-bedroom apartment in Mumbai, check if it's compliant with Maharashtra rent laws, then flag any missing clauses.' You don't know in advance exactly which steps Claude will need to take.",
        "options": [
            "Chaining workflow — fixed 3 steps",
            "Single agent with system prompt",
            "Autonomous agent with tools",
            "Parallelization workflow"
        ],
        "correct": 2,
        "explanation": "The path is genuinely unknown — Claude might need to search law databases, generate draft text, cross-reference clauses, and iterate. An autonomous agent with tools can dynamically decide the steps. A fixed chaining workflow would break on edge cases."
    },
    {
        "category": "RAG Technique",
        "cat_class": "tag-green",
        "scenario": "Users search your legal database using exact terms like 'IPC Section 302' or 'CrPC 161'. Your vector search keeps returning wrong results because it focuses on meaning, not exact terms.",
        "options": [
            "Contextual retrieval",
            "Reranking",
            "BM25 lexical search",
            "Autonomous agent"
        ],
        "correct": 2,
        "explanation": "When users search with exact legal section numbers or jargon, BM25 (lexical search) wins. It ranks documents by how often rare specific terms appear — perfect for 'IPC Section 302' where keyword matching matters more than semantic similarity."
    },
    {
        "category": "Agent Pattern",
        "cat_class": "tag-orange",
        "scenario": "Every contract uploaded to ELNAR Innotech goes through the same process: extract parties → identify contract type → check for 5 standard clauses → generate summary report. This runs hundreds of times a day.",
        "options": [
            "Autonomous agent",
            "Chaining workflow",
            "Routing workflow",
            "Evaluator-optimizer"
        ],
        "correct": 1,
        "explanation": "You know every step in advance and the sequence never changes. A chaining workflow is faster, cheaper, and more reliable than an agent here. Agents are overkill when the pipeline is predictable — workflows give you 100% consistent results."
    },
    {
        "category": "RAG Technique",
        "cat_class": "tag-green",
        "scenario": "A chunk from your legal document says: 'The party shall comply with the obligations mentioned above.' When retrieved alone, this chunk is useless — you don't know which party or which obligations.",
        "options": [
            "Hybrid search (vector + BM25)",
            "Reranking",
            "Contextual retrieval",
            "Parallelization workflow"
        ],
        "correct": 2,
        "explanation": "This is exactly the problem contextual retrieval solves. Before storing each chunk, you send the full document + chunk to Claude and generate context like: 'This refers to Clause 4, the tenant's maintenance obligations.' Now the chunk makes sense in retrieval."
    },
    {
        "category": "Agent Pattern",
        "cat_class": "tag-orange",
        "scenario": "ELNAR Innotech receives a contract. You don't know in advance whether it's a rental agreement, employment contract, or NDA — each needs a completely different review template and toolset.",
        "options": [
            "Evaluator-optimizer",
            "Routing workflow",
            "Autonomous agent",
            "Single agent"
        ],
        "correct": 1,
        "explanation": "Routing workflow is perfect here. Step 1: Claude classifies the contract type. Step 2: Your system routes it to the right pipeline — rental review, employment review, or NDA review — each with its own prompts and tools. Clean and predictable."
    },
    {
        "category": "RAG Technique",
        "cat_class": "tag-green",
        "scenario": "Your vector search returns relevant chunks but the most important one keeps getting ranked 4th or 5th instead of 1st. The results are right, just in the wrong order.",
        "options": [
            "Add BM25 to create hybrid search",
            "Switch to contextual retrieval",
            "Add a reranking step after retrieval",
            "Use an autonomous agent instead"
        ],
        "correct": 2,
        "explanation": "Reranking is exactly for this. After retrieval returns 5 chunks, you send them all to Claude with the original query and ask it to reorder by true relevance. It costs one extra LLM call but fixes ordering — especially for nuanced legal queries."
    },
    {
        "category": "Agent Pattern",
        "cat_class": "tag-orange",
        "scenario": "You need to review 20 independent contract clauses simultaneously for compliance. Each clause check is self-contained and doesn't depend on results from any other clause.",
        "options": [
            "Chaining workflow — one at a time",
            "Parallelization workflow",
            "Autonomous agent",
            "Evaluator-optimizer"
        ],
        "correct": 1,
        "explanation": "Parallelization wins here. Since each clause check is independent, you run all 20 simultaneously — dramatically faster than chaining (20x speedup) and simpler than an autonomous agent. You know exactly what needs to happen, just in parallel."
    },
    {
        "category": "RAG Technique",
        "cat_class": "tag-green",
        "scenario": "Your legal app needs to find case precedents when a user types 'tenant eviction dispute'. Users sometimes say 'eviction' and sometimes 'possession suit' — different words, same meaning. Keyword search misses the matches.",
        "options": [
            "BM25 lexical search",
            "Vector search (semantic)",
            "Reranking only",
            "Contextual retrieval"
        ],
        "correct": 1,
        "explanation": "Vector search is built for this. It converts text to embeddings that capture meaning — so 'eviction dispute' and 'possession suit' land near each other in the embedding space and get matched correctly. BM25 keyword search would fail completely here."
    },
    {
        "category": "Agent Pattern",
        "cat_class": "tag-orange",
        "scenario": "ELNAR Innotech auto-generates contract drafts but quality is inconsistent — sometimes clauses are missing or language is too vague. You want the system to check its own output and keep improving until it meets a quality bar.",
        "options": [
            "Single agent with a longer prompt",
            "Routing workflow",
            "Evaluator-optimizer workflow",
            "Parallelization workflow"
        ],
        "correct": 2,
        "explanation": "Evaluator-optimizer is the pattern. Step 1 (Producer): Claude drafts the contract. Step 2 (Evaluator): A separate Claude call reviews against your quality criteria. If it fails, feedback goes back to the producer and it tries again — just like a human review cycle."
    }
]

LETTERS = ["A", "B", "C", "D"]

def get_score_message(score):
    if score == 10:
        return "Perfect score! 🎉", "You know your AI patterns inside out. Truly impressive."
    elif score >= 8:
        return "Excellent work! ", "Strong understanding of agents vs RAG. Just a couple of edge cases to review."
    elif score >= 6:
        return "Solid foundation! ", "You have the core concepts down. Review the explanations below to sharpen the tricky ones."
    elif score >= 4:
        return "Good start! ", "The patterns are clicking into place. Read Nabeela's LinkedIn post for deeper context and try again."
    else:
        return "Keep learning! ", "These patterns take time to internalize. Check the explanations and give it another go."

def init_state():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answers" not in st.session_state:
        st.session_state.answers = []
    if "selected" not in st.session_state:
        st.session_state.selected = None
    if "finished" not in st.session_state:
        st.session_state.finished = False

def restart():
    st.session_state.started = False
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.selected = None
    st.session_state.finished = False

def select_option(idx):
    if st.session_state.selected is None:
        st.session_state.selected = idx
        q = QUESTIONS[st.session_state.q_index]
        correct = idx == q["correct"]
        if correct:
            st.session_state.score += 1
        st.session_state.answers.append({
            "question": q["scenario"][:85] + "...",
            "correct": correct,
            "chosen": q["options"][idx],
            "correct_answer": q["options"][q["correct"]],
            "explanation": q["explanation"]
        })

def next_question():
    st.session_state.q_index += 1
    st.session_state.selected = None
    if st.session_state.q_index >= len(QUESTIONS):
        st.session_state.finished = True

# ── App ──────────────────────────────────────────────────────────────────────
init_state()

# Header
st.markdown("""
<div class="header-wrap">
  <div class="brand">
    <span class="brand-name">ELNAR Innotech</span>
  </div>
  <span class="author-tag">by Nabeela Khan</span>
</div>
""", unsafe_allow_html=True)

# ── INTRO SCREEN ─────────────────────────────────────────────────────────────
if not st.session_state.started and not st.session_state.finished:
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0 1rem;">
      <div class="tag tag-green">Interactive Quiz</div>
      <div class="hero-title">Do you know <em>when</em> to use<br>which AI pattern?</div>
      <div class="hero-sub">
        10 real-world scenarios. Pick the right Agent or RAG technique.<br>
        See how well you really know your AI architecture.
      </div>
      <div class="pills-row" style="justify-content:center;">
        <span class="pill" style="background:#e8f2ee;border-color:#5a9e88;color:#2a5f4f;">RAG Techniques</span>
        <span class="pill" style="background:#fdf0e6;border-color:#c8783a;color:#c8783a;">Agent Patterns</span>
        <span class="pill">10 Questions</span>
        <span class="pill">~5 mins</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start the quiz →", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.markdown("""
    <hr class="divider">
    <div style="text-align:center;">
      <div style="font-size:13px;color:#8a8880;font-weight:300;margin-bottom:1rem;">What you'll be tested on</div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">
        <span class="pill">Vector search</span>
        <span class="pill">BM25 lexical search</span>
        <span class="pill">Contextual retrieval</span>
        <span class="pill">Reranking</span>
        <span class="pill">Chaining workflows</span>
        <span class="pill">Routing workflows</span>
        <span class="pill">Parallelization</span>
        <span class="pill">Autonomous agents</span>
        <span class="pill">Evaluator-optimizer</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── QUESTION SCREEN ───────────────────────────────────────────────────────────
elif st.session_state.started and not st.session_state.finished:
    q_idx = st.session_state.q_index
    q = QUESTIONS[q_idx]
    total = len(QUESTIONS)
    pct = int((q_idx / total) * 100)

    # Progress bar
    st.markdown(f"""
    <div class="progress-meta">
      <span>Question {q_idx + 1} of {total}</span>
      <span>Score: {st.session_state.score}</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" style="width:{pct}%"></div>
    </div>
    """, unsafe_allow_html=True)

    # Category tag
    st.markdown(f'<div class="tag {q["cat_class"]}">{q["category"]}</div>', unsafe_allow_html=True)

    # Scenario
    st.markdown(f"""
    <div class="scenario-card">
      <div class="scenario-text">{q["scenario"]}</div>
    </div>
    <div style="font-size:13px;font-weight:500;color:#8a8880;letter-spacing:0.03em;margin-bottom:0.75rem;">
      Which pattern fits best?
    </div>
    """, unsafe_allow_html=True)

    # Options
    selected = st.session_state.selected
    answered = selected is not None

    for i, option in enumerate(q["options"]):
        letter = LETTERS[i]

        if not answered:
            if st.button(f"{letter}   {option}", key=f"opt_{q_idx}_{i}", use_container_width=True):
                select_option(i)
                st.rerun()
        else:
            is_correct_opt = (i == q["correct"])
            is_chosen = (i == selected)

            if is_correct_opt:
                bg = "#eaf5ee"; border = "#1e6b46"; color = "#1e6b46"; lbg = "#1e6b46"; lc = "#fff"
            elif is_chosen and not is_correct_opt:
                bg = "#fdecea"; border = "#b33a2a"; color = "#b33a2a"; lbg = "#b33a2a"; lc = "#fff"
            else:
                bg = "#fff"; border = "#e0ddd6"; color = "#8a8880"; lbg = "#e0ddd6"; lc = "#8a8880"

            st.markdown(f"""
            <div style="
              background:{bg};border:1.5px solid {border};border-radius:12px;
              padding:14px 18px;margin-bottom:10px;display:flex;align-items:center;
              gap:12px;font-size:14px;color:{color};
            ">
              <span style="
                width:26px;height:26px;border-radius:50%;background:{lbg};
                color:{lc};display:inline-flex;align-items:center;justify-content:center;
                font-size:12px;font-weight:500;flex-shrink:0;
              ">{letter}</span>
              <span>{option}</span>
            </div>
            """, unsafe_allow_html=True)

    # Explanation
    if answered:
        is_right = (selected == q["correct"])
        cls = "feedback-correct" if is_right else "feedback-wrong"
        label = "✓ Correct" if is_right else "✗ Not quite"
        st.markdown(f"""
        <div class="{cls}">
          <div class="feedback-label">{label}</div>
          {q["explanation"]}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col3:
            label = "See results →" if q_idx == total - 1 else "Next question →"
            if st.button(label, use_container_width=True):
                next_question()
                st.rerun()

# ── RESULTS SCREEN ────────────────────────────────────────────────────────────
elif st.session_state.finished:
    score = st.session_state.score
    title, sub = get_score_message(score)

    # Score circle (HTML)
    st.markdown(f"""
    <div style="text-align:center;padding:2rem 0 1rem;">
      <div class="score-circle">
        <span class="score-num">{score}</span>
        <span class="score-denom">/ 10</span>
      </div>
      <div class="results-title">{title}</div>
      <div class="results-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

    # Share text
    share_text = f"I just scored {score}/10 on Nabeela Khan's AI Architecture Quiz! 🧠 Do you know when to use Vector Search vs BM25 vs Contextual Retrieval — or when an Autonomous Agent beats a Workflow? Test yourself! #AI #LLM #Claude #ELNAR Innotech"

    st.markdown(f"""
    <div class="share-box">
      <div class="share-label">Share your result</div>
      <div class="share-text">{share_text}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Retake quiz", use_container_width=True):
            restart()
            st.rerun()
    with col2:
        st.code(share_text, language=None)

    # Review
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div style="font-family:\'DM Serif Display\',serif;font-size:1.4rem;letter-spacing:-0.3px;margin-bottom:1rem;">Question review</div>', unsafe_allow_html=True)

    for i, a in enumerate(st.session_state.answers):
        icon = "✓" if a["correct"] else "✗"
        icon_color = "#1e6b46" if a["correct"] else "#b33a2a"
        ans_text = f"Correct!" if a["correct"] else f"You chose: {a['chosen']} · Correct: {a['correct_answer']}"
        st.markdown(f"""
        <div class="review-item">
          <span style="color:{icon_color};font-size:14px;margin-top:2px;flex-shrink:0;">{icon}</span>
          <div>
            <div class="review-q">Q{i+1}: {a["question"]}</div>
            <div class="review-ans">{ans_text}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr class="divider">
<div style="text-align:center;font-size:12px;color:#8a8880;font-weight:300;padding-bottom:1rem;">
  Made with care by <strong style="color:#2a5f4f;">Nabeela Khan</strong> · ELNAR Innotech ·
  Inspired by the <em>Building with Claude API</em> course
</div>
""", unsafe_allow_html=True)
