import random
import time
import streamlit as st

st.set_page_config(page_title="Valentine for Nivi 💘", page_icon="💘", layout="centered")

# -------------------------
# Premium CSS + floating hearts animation
# -------------------------
st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(255, 0, 122, 0.20), transparent 45%),
                    radial-gradient(circle at 80% 30%, rgba(255, 180, 0, 0.18), transparent 45%),
                    radial-gradient(circle at 35% 90%, rgba(140, 70, 255, 0.18), transparent 45%),
                    linear-gradient(135deg, #0b0b12 0%, #0f0f1c 45%, #0b0b12 100%);
        color: #fff;
      }

      .wrap { max-width: 780px; margin: 0 auto; }

      .glass {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 20px 60px rgba(0,0,0,0.35);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 22px;
        padding: 28px 26px 20px 26px;
        overflow: hidden;
      }

      .title {
        font-size: 46px;
        font-weight: 900;
        line-height: 1.05;
        margin: 0 0 10px 0;
        letter-spacing: -0.8px;
        text-align: center;
      }

      .subtitle {
        font-size: 16px;
        opacity: 0.82;
        margin: 0 0 12px 0;
        text-align: center;
      }

      .divider {
        height: 1px;
        width: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
        margin: 14px 0 18px 0;
      }

      /* Buttons */
      div.stButton > button {
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.16) !important;
        background: rgba(255,255,255,0.08) !important;
        color: white !important;
        padding: 0.85rem 1rem !important;
        font-weight: 800 !important;
        transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
      }
      div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        background: rgba(255,255,255,0.12) !important;
      }

      .yesGlow div.stButton > button {
        background: linear-gradient(135deg, rgba(255,0,122,0.45), rgba(255,180,0,0.22)) !important;
        border: 1px solid rgba(255,255,255,0.24) !important;
      }
      .yesGlow div.stButton > button:hover {
        box-shadow: 0 0 0 6px rgba(255,0,122,0.14), 0 18px 40px rgba(0,0,0,0.45);
      }

      .tiny { font-size: 12px; opacity: 0.65; margin-top: 12px; text-align: center; }

      /* Floating hearts */
      .hearts {
        position: fixed;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
      }
      .heart {
        position: absolute;
        bottom: -40px;
        font-size: 18px;
        opacity: 0.0;
        animation: floatUp linear infinite;
        filter: drop-shadow(0 8px 10px rgba(0,0,0,0.4));
      }
      @keyframes floatUp {
        0% { transform: translateY(0) translateX(0) rotate(0deg); opacity: 0.0; }
        10% { opacity: 0.55; }
        60% { opacity: 0.45; }
        100% { transform: translateY(-110vh) translateX(40px) rotate(18deg); opacity: 0.0; }
      }

      .block-container { position: relative; z-index: 2; }
    </style>

    <div class="hearts">
      <div class="heart" style="left: 8%;  animation-duration: 9s;  animation-delay: 0s;">💗</div>
      <div class="heart" style="left: 18%; animation-duration: 12s; animation-delay: 1s;">💖</div>
      <div class="heart" style="left: 28%; animation-duration: 10s; animation-delay: 2s;">💘</div>
      <div class="heart" style="left: 42%; animation-duration: 13s; animation-delay: 0.5s;">💝</div>
      <div class="heart" style="left: 55%; animation-duration: 11s; animation-delay: 1.8s;">💞</div>
      <div class="heart" style="left: 68%; animation-duration: 14s; animation-delay: 0.2s;">💓</div>
      <div class="heart" style="left: 78%; animation-duration: 10s; animation-delay: 1.1s;">💕</div>
      <div class="heart" style="left: 90%; animation-duration: 12s; animation-delay: 2.4s;">💗</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# State
# -------------------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "no_level" not in st.session_state:
    st.session_state.no_level = 0
if "no_spot" not in st.session_state:
    st.session_state.no_spot = random.randint(1, 3)
if "no_label" not in st.session_state:
    st.session_state.no_label = "❌ No"
if "timestamp" not in st.session_state:
    st.session_state.timestamp = None

# -------------------------
# UI
# -------------------------
st.markdown('<div class="wrap"><div class="glass">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">Will you be my Valentine, Nivi?</div>
    <div class="subtitle">Choose wisely 😌💘</div>
    <div class="divider"></div>
    """,
    unsafe_allow_html=True,
)

if st.session_state.accepted:
    st.balloons()

    # ✅ Dancing GIF (place dance.gif in the same folder as app.py)
    st.image("dance.gif", caption="Nivi said YES 💃🕺💘", use_container_width=True)

    if st.session_state.timestamp is None:
        st.session_state.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    st.success("You've a surprise date Tonight, Accept your gifts  💞")
    st.info(f"Accepted at: {st.session_state.timestamp}  — screenshot this 😄")

    st.write("")
    if st.button("🔁 Reset", use_container_width=True):
        for k in ["accepted", "no_level", "no_spot", "no_label", "timestamp"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()

else:
    cols = st.columns(4)

    with cols[0]:
        st.markdown('<div class="yesGlow">', unsafe_allow_html=True)
        if st.button("✅ Yes", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    labels = [
        "❌ No",
        "❌ No (Pakka?)",
        "❌ No (don’t do me like that 😭)",
        "❌ No (this button is cursed)",
        "❌ No (Acchaaa?)",
        "❌ No (enda Mairey)",
    ]

    no_col_index = st.session_state.no_spot  # 1..3
    with cols[no_col_index]:
        if st.button(st.session_state.no_label, use_container_width=True):
            st.session_state.no_level = min(st.session_state.no_level + 1, len(labels) - 1)
            st.session_state.no_label = labels[st.session_state.no_level]

            # Move the "No" to a different column
            choices = [1, 2, 3]
            choices.remove(no_col_index)
            st.session_state.no_spot = random.choice(choices)

            st.toast("💨 Nope button ran away.", icon="💘")
            st.rerun()

    st.markdown(
        f'<div class="tiny">No-button dodge level: {st.session_state.no_level}/{len(labels)-1}</div>',
        unsafe_allow_html=True,
    )

st.markdown("</div></div>", unsafe_allow_html=True)
