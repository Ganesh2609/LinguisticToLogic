import streamlit as st

st.set_page_config(page_title="Linguistic to Logic - Reviews and FAQs", page_icon=":anchor:", layout="wide")
st.markdown('<h1 style="text-align: center;">LINGUISTIC TO LOGIC - THE SQL CONVERTER (LTL-SQL)</h1>', unsafe_allow_html=True)
st.markdown('')
st.markdown('')

# Reviews Section
st.markdown('<h2>🙋Reviews</h2>', unsafe_allow_html=True)
st.markdown('<h3>What Our Users Say</h3>', unsafe_allow_html=True)

# Creating a columns layout for reviews
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://th.bing.com/th/id/OIP.74QCKUaoThEkKLbKbV2EMgHaH7?w=190&h=204&c=7&r=0&o=5&dpr=1.5&pid=1.7" alt="1st Customer" style="border-radius: 50%;height: 80px; width: 80px;">
        <h4>1st Customer</h4>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero.</p>
        <p>⭐⭐⭐⭐⭐</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://th.bing.com/th/id/OIP.mIXF4N-Z9_-ymJSZ1c6yQAHaHa?w=203&h=203&c=7&r=0&o=5&dpr=1.5&pid=1.7" alt="2nd Customer" style="border-radius: 50%;height: 80px; width: 80px;">
        <h4>2nd Customer</h4>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero.</p>
        <p>⭐⭐⭐☆☆</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://th.bing.com/th/id/OIP.hyLsJh3chqROf-s7RoNsEAHaHX?w=198&h=197&c=7&r=0&o=5&dpr=1.5&pid=1.7" alt="3rd Customer" style="border-radius: 50%;height: 80px; width: 80px;">
        <h4>3rd Customer</h4>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero.</p>
        <p>⭐⭐⭐⭐⭐</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://th.bing.com/th/id/OIP.8li1g3WASRlQCpV6X54VCQHaHa?w=200&h=200&c=7&r=0&o=5&dpr=1.5&pid=1.7" alt="4th Customer" style="border-radius: 50%;height: 80px; width: 80px;">
        <h4>4th Customer</h4>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero.</p>
        <p>⭐⭐⭐⭐⭐</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# FAQ Section
st.markdown('<h2>Frequently Asked Questions ⁉️</h2>', unsafe_allow_html=True)

with st.expander("1. How does the SQL Converter work?"):
    st.write("""
    The SQL Converter uses natural language processing to interpret user queries and convert them into SQL commands. Simply enter your command in plain English, and the tool will generate the appropriate SQL query for you.
    """)

with st.expander("2. What kind of SQL commands can the tool generate?"):
    st.write("""
    The tool can generate various SQL commands including `SELECT`, `INSERT`, `UPDATE`, and `DELETE` based on the natural language input. It supports both simple and complex queries.
    """)

with st.expander("3. Is the tool compatible with all SQL databases?"):
    st.write("""
    The tool is designed to work with standard SQL databases like MySQL, PostgreSQL, and SQLite. Compatibility with other databases may vary.
    """)

with st.expander("4. How can I get support or report a bug?"):
    st.write("""
    If you need support or want to report a bug, please contact us via email at [support@codesyndicate.com](mailto:support@codesyndicate.com). We are here to help!
    """)

with st.expander("5. Can I contribute to the project?"):
    st.write("""
    Absolutely! We welcome contributions from the community. You can contribute by submitting pull requests on our [GitHub repository](https://github.com/CodeSyndicate/LTL-SQL).
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Contact Us Section
st.markdown('<h2>📱Contact Us</h2>', unsafe_allow_html=True)
st.markdown("""
We would love to hear from you! Whether you have a question about our project, want to collaborate, or just want to say hi, feel free to reach out to us.

 **📨 Email:** 
  - Ganesh Sundhar S: [ganeshsundhar007@gmail.com](mailto:ganeshsundhar007@gmail.com)
  - Hari Krishnan N: [hariprabha1979@gmail.com](mailto:hariprabha1979@gmail.com)
  - Dhanush MC: [mcdhanush1122@outlook.com](mailto:mcdhanush1122@outlook.com)

 **📞 Phone:** 
  - Ganesh Sundhar S: [9677236828](tel:9677236828)
  - Hari Krishnan N: [6379266196](tel:6379266196)
  - Dhanush MC: [6383269837](tel:6383269837)
""")
