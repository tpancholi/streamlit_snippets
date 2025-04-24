import streamlit as st
import pandas as pd

# Initialize the session state variable if it doesn't exist
if "rust_vote" not in st.session_state:
	st.session_state.rust_vote = 0
# Initialize the session state variable if it doesn't exist
if "go_vote" not in st.session_state:
	st.session_state.go_vote = 0


def add_rust():
	st.session_state.rust_vote += 1


def add_go():
	st.session_state.go_vote += 1


with st.container():
	st.title("Voting Application")
	col1, col2 = st.columns(2)
	with col1:
		st.header("Rust")
		st.image(
			"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.weetechsolution.com%2Fwp-content%2Fuploads%2F2023%2F08%2FRust-Programming-Language-Introduction-Documentation.jpg&f=1&nofb=1&ipt=168fcba927d67a694e9013bb3de0927041834ebbaea2f03c77275409e70a4c64",
			width=424,
		)
		st.button(
			"Vote Rust", on_click=add_rust, type="primary", key="rust_vote_button"
		)
	with col2:
		st.header("Go")
		st.image(
			"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fcontent%2Fimages%2Fsize%2Fw2000%2F2021%2F10%2Fgolang.png&f=1&nofb=1&ipt=d6d38e6d566d1b4de930820ad82a7c393ed944a5e4f1c7cb57927e1eb32e4ec7",
			width=424,
		)
		st.button("Vote Go", on_click=add_go, type="primary", key="go_vote_button")

	votes_df = pd.DataFrame(
		{
			"Language": ["Rust", "Go"],
			"Votes": [st.session_state.rust_vote, st.session_state.go_vote],
		}
	)
	st.subheader("Live Voting Results")
	st.bar_chart(votes_df.set_index("Language"))
