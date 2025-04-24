import streamlit as st

st.title("Language Picker")
st.subheader("Choose a language from dropdown")
st.text("You can select 1 or more languages from dropdown")
st.write("App is powered by Streamlit with ❤️")
chosen_list = st.multiselect(
	"What are your favourite languages",
	options=["Rust", "Python", "Go", "Javascript", "Typescript"],
	placeholder="Choose a language from dropdown",
)
st.write("You have selected following languages:")
if len(chosen_list) == 0:
	st.write("No items selected yet. 🥺")
else:
	for item in chosen_list:
		st.markdown(f"- {item}", unsafe_allow_html=True)
