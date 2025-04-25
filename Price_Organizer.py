import streamlit as st

# Initialize session state for storing products
if "products" not in st.session_state:
    st.session_state.products = []

st.title("🛒 Product Management System")

# Add product
with st.expander("➕ Add Product"):
    product_name = st.text_input("Enter product name", key="add_name")
    min_price = st.number_input("Enter minimum price", min_value=0, step=1, key="add_min")
    max_price = st.number_input("Enter maximum price", min_value=0, step=1, key="add_max")
    
    if st.button("Add Product"):
        if not product_name:
            st.warning("Please enter a product name.")
        elif min_price > max_price:
            st.warning("Min price must be less than or equal to max price.")
        else:
            st.session_state.products.append({
                "Product": product_name,
                "Min_Price": min_price,
                "Max_Price": max_price
            })
            st.success(f"Product '{product_name}' added successfully!")

# View products
st.subheader("📦 Product List")
if not st.session_state.products:
    st.info("No products available.")
else:
    for idx, product in enumerate(st.session_state.products):
        st.write(f"**{product['Product']}** — Min Price: {product['Min_Price']}, Max Price: {product['Max_Price']}")
        if st.button(f"Remove '{product['Product']}'", key=f"remove_{idx}"):
            st.session_state.products.pop(idx)
            st.success(f"Product '{product['Product']}' removed.")
            st.experimental_rerun()

