import streamlit as st
from services.db.init_db import init_db
from services.db.session import (
  get_active_sessions,
  delete_session,
  finish_session,
  create_session,
)
from services.db.player import get_players_by_session_id
from utils.format import format_datetime

st.title("🎮 Active Game Sessions")

if "go_to_session" in st.session_state:
  session_id = st.session_state.pop("go_to_session")
  st.markdown(
    f"""
    <meta http-equiv="refresh" content="0; url=/session_play?session_id={session_id}" />
    """,
    unsafe_allow_html=True
  )
  st.stop()

init_db()
sessions = get_active_sessions()

if "confirm_delete" not in st.session_state:
  st.session_state["confirm_delete"] = None
if "confirm_finish" not in st.session_state:
  st.session_state["confirm_finish"] = None
if "create_session_modal" not in st.session_state:
  st.session_state["create_session_modal"] = False


@st.dialog("Create New Session")
def open_create_session_dialog():
  st.markdown("Enter session name and up to 6 player names.")
  name = st.text_input("Session Name")
  player_names = [st.text_input(f"Player {i+1}") for i in range(6)]

  if st.button("Create"):
    valid_players = [p.strip() for p in player_names if p.strip()]
    if not name.strip():
      st.warning("Please enter a session name.")
    elif not valid_players:
      st.warning("Please enter at least one player.")
    else:
      create_session(name.strip(), valid_players)
      st.session_state["create_session_modal"] = False
      st.success("Session created successfully.")
      st.rerun()


@st.dialog("Confirm Deletion")
def confirm_deletion(session_id: int, session_name: str):
  st.warning(f"This will permanently delete the session '{session_name}'.")
  _, col_btn = st.columns([4, 1])
  with col_btn:
    if st.button("Delete"):
      delete_session(session_id)
      st.session_state["confirm_delete"] = None
      st.success("Session deleted.")
      st.rerun()


@st.dialog("Confirm Finish")
def confirm_finish(session_id: int, session_name: str):
  st.info(f"This will mark the session '{session_name}' as finished.")
  _, col_btn = st.columns([4, 1])
  with col_btn:
    if st.button("Finish"):
      finish_session(session_id)
      st.session_state["confirm_finish"] = None
      st.success("Session marked as finished.")
      st.rerun()


col_title, col_button = st.columns([5, 1])
with col_title:
  st.markdown("## 🕹️ Ongoing Games")
with col_button:
  if st.button("New Game"):
    open_create_session_dialog()

if not sessions:
  st.info("No active sessions available.")
else:
  for s in sessions:
    players = get_players_by_session_id(s.id)

    with st.container(border=True):
      st.markdown(f"### {s.name}")
      st.markdown(f"📅 Created at: `{format_datetime(s.created_at)}`")
      st.markdown(f"🔢 Current Level: `{s.actual_level}`")
      st.markdown(f"💰 Total Money: `{s.total_money}`")

      if players:
        player_labels = []
        for p in players:
          label = f"**{p.name}**" if p.is_host else p.name
          player_labels.append(label)
        st.markdown("👥 " + ", ".join(player_labels))

      col_spacer, col_view, col_finish, col_delete = st.columns([5, 1, 1, 1])
      with col_view:
        if st.button("View", key=f"view_{s.id}"):
          st.session_state["go_to_session"] = s.id
      with col_finish:
        if st.button("Finish", key=f"finish_btn_{s.id}"):
          st.session_state["confirm_finish"] = s.id
          confirm_finish(s.id, s.name)
      with col_delete:
        if st.button("Delete", key=f"delete_btn_{s.id}"):
          st.session_state["confirm_delete"] = s.id
          confirm_deletion(s.id, s.name)
