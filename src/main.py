import streamlit as st
import importlib
import pathlib

st.set_page_config(page_title="Game Manager", layout="wide")

st.sidebar.title("📂 Pages")

pages_path = pathlib.Path(__file__).parent / "pages"
page_files = [p.stem for p in pages_path.glob("*.py") if not p.name.startswith("__")]

page_names = {name.replace("_", " ").title(): name for name in sorted(page_files)}
selection = st.sidebar.radio("Navigate", list(page_names.keys()))

selected_module = f"pages.{page_names[selection]}"
module = importlib.import_module(selected_module)

if hasattr(module, "app"):
  module.app()
else:
  st.error(f"Page {selected_module} has no app() function.")
