import streamlit as st
from datetime import datetime
import uuid

from services.storage import load_sessions, save_session, soft_delete_session, init_db
from models.session import Session
from models.player import Player


def app():
    st.title("📋 Game Sessions")

    init_db()

    st.subheader("📑 Existing Sessions")
    sessions = load_sessions()
    print("sessions", sessions)

    if not sessions:
        st.info("No sessions found.")
    else:
        for s in sessions:
            with st.container(border=True):
                col1, col2 = st.columns([5, 1])

                with col1:
                    st.markdown(f"### 🎮 {s.name}")
                    st.markdown(f"🕓 Created: `{s.created_at}`")
                    st.markdown(f"💰 Total Money: `{s.total_money}`")
                    st.markdown("👥 Players:")
                    for p in s.players:
                        prefix = "⭐ **Host**: " if p.is_host else "👤 "
                        st.markdown(f"{prefix}{p.name}")

                with col2:
                    delete_key = f"delete_{s.id}"
                    if st.button("🗑️", key=delete_key):
                        st.session_state["confirm_delete"] = s.id

                if st.session_state.get("confirm_delete") == s.id:
                    with st.expander(
                        f"🛑 Confirm deletion of '{s.name}'", expanded=True
                    ):
                        st.warning("This will permanently mark the session as deleted.")
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button("❌ Cancel"):
                                st.session_state["confirm_delete"] = None
                        with col_b:
                            if st.button("✅ Confirm Delete"):
                                soft_delete_session(s.id)
                                st.success("Session deleted.")

    st.subheader("➕ Create New Session")
    with st.form("new_session_form"):
        name = st.text_input("Session Name")

        st.markdown("Enter up to 6 player names:")
        player_names = [st.text_input(f"Player {i+1}") for i in range(6)]

        submitted = st.form_submit_button("Create Session")

        if submitted and name.strip():
            players = [
                Player(name=p.strip(), money=0.0, items=[], is_host=(i == 0))
                for i, p in enumerate(player_names)
                if p.strip()
            ]

            if not players:
                st.warning("Please provide at least one player.")
            else:
                new_session = Session(
                    id=str(uuid.uuid4())[:8],
                    name=name.strip(),
                    created_at=datetime.now().isoformat(timespec="seconds"),
                    round=1,
                    total_money=0.0,
                    players=players,
                    loans=[],
                )
                save_session(new_session)
                st.success("Session created!")


app()
