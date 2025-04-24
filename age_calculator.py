import streamlit as st
from datetime import datetime, timedelta
from dateutil import relativedelta

today_date = datetime.now()
max_age = datetime.date(today_date - timedelta(days=365 * 100))

st.title("Age Calculator")
user_name = st.text_input("Please enter your name")
user_dob = st.date_input("Please select your Date of Birth", min_value=max_age)

diff = relativedelta.relativedelta(today_date, user_dob)

if user_name != "" and user_dob != "":
	st.write(
		f"{user_name} you selected  {user_dob.strftime('%B %d, %Y')} as your date of birth"
	)
	st.write(
		f"{user_name} you are {diff.years} years, {diff.months} months and {diff.days} days old as of {today_date.strftime('%B %d, %Y')}"
	)
else:
	st.warning("Please Enter your name as well as Date of Birth")
