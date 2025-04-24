import streamlit as st

st.title("Payment Page")
st.subheader("Powered by Streamlit with ❤️")
product_cost = 2355
st.write(f"The product cost is {product_cost} INR")
quantity = st.number_input("How many units do you require?", min_value=1, max_value=10,step=1)
total_cost = product_cost * quantity
if quantity:
    st.write(f"Your total bill is {total_cost} INR")

place_of_delivery = st.radio("Please select delivery place:", ["Home", "Office"])
if place_of_delivery:
    st.write(f"You have selected delivery to be at {place_of_delivery}")

tip_value = st.slider("Tip Value", min_value=10, max_value=100, value=20, step=10)
if tip_value:
    st.write(f"Your total tip is {tip_value} INR")
st.write(f"Your total bill is {total_cost + tip_value} INR")

payment_method = st.selectbox("Please select payment method", ["Credit Card", "Debit Card", "UPI"])

if payment_method == "Credit Card":
    card_details = st.text_input("Enter your credit card details", max_chars=19, placeholder="1111111111111111")
    cvv = st.text_input("Enter your CVV number", type="password", placeholder="999")

    if card_details and cvv:
        st.write(f"Your credit card details is: {card_details} and  CVV: {cvv}")
elif payment_method == "Debit Card":
    card_details = st.text_input("Enter your credit card details", max_chars=19, placeholder="1111111111111111")
    cvv = st.text_input("Enter your CVV number", type="password", placeholder="999")
    if card_details and cvv:
        st.write(f"Your Debit card details is: {card_details} and  CVV: {cvv}")
elif payment_method == "UPI":
    upi_number = st.text_input("Enter your UPI number", placeholder="user@icici", max_chars=50)
    if upi_number:
        st.write(f"Your UPI number is: {upi_number}")
