import streamlit as st
from services.db.session import get_session_full_data
from utils.format import format_datetime

session_id = st.query_params["session_id"]
if session_id is None:
    st.error("No session selected.")
    st.stop()

session = get_session_full_data(int(session_id))
if not session:
    st.error("Session not found.")
    st.stop()

st.set_page_config(page_title="Session Play")


st.markdown(f"📅 Created at: `{format_datetime(session.created_at)}`")
st.markdown(f"🔢 Current Level: `{session.actual_level}`")
st.markdown(f"💰 Total Money: `{session.total_money}`")
st.divider()

st.markdown("### 💼 Level Info")
st.markdown(f"- Leftover from previous level: `{session.previous_remaining_money}`")
st.markdown(f"- Collected this level: `{session.collected_money}`")
st.markdown(f"- Total available: `{session.total_available}`")

st.subheader("👥 Player States")
for p in session.players:
    with st.container(border=True):
        st.markdown(f"### {'**' + p.name + '** (Host)' if p.is_host else p.name}")
        if p.level_state:
            st.markdown(f"- 💵 Previous: `{p.level_state.previous_remaining}`")
            st.markdown(f"- 📤 Donated: `{p.level_state.total_donated}`")
            st.markdown(f"- 📥 Received: `{p.level_state.total_received}`")
            st.markdown(f"- 💼 Post-donation: `{p.level_state.post_donation_balance}`")
            st.markdown(f"- 🧮 Final: `{p.level_state.final_balance}`")
        else:
            st.info("No data yet for this level.")
