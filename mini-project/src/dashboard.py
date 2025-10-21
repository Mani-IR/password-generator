'''
Mani Ajorloo
'''

import streamlit as st
# import streamlit.components.v1 as components
# import json
import io
import qrcode
from password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinGenerator,password_strength,save_password_to_file


st.set_page_config(page_title="Password Generator", layout="centered")


st.image('./images/1_kKrBYYaPTaSTOlOIfsC-6w11.png')
st.title(":zap: Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Pin Code':
    length = st.slider("Select PIN Length",4,32)
    generator = PinGenerator(length)

elif option == 'Random Password':
    length = st.slider("Select Password Length",8,100)
    include_numbers = st.checkbox("Include Numbers", value=True)
    include_symbols = st.toggle("Include Symbols")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

elif option == 'Memorable Password':
    num_of_words = st.slider("Number of Words",2,10, value=3)
    separator = st.text_input("Separator", value='-')
    capitalize = st.checkbox("Capitalize Words", value=False)
    generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)

else:  
    num_of_words = st.slider("Number of Words", 2, 10, value=3)
    separator = st.text_input("Separator", value='-')
    capitalize = st.checkbox("Capitalize Words", value=False)
    generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)


password = generator.generate()
st.write(fr'your generated password is : ``` {password} ``` ')
st.code(password, language="text")
# ------------------------
#   ذخیره پسورد در فایل
# ------------------------
save_password_to_file(password, filename="passwords.txt")


# ------------------------
#    سطح امنیت پسورد
# ------------------------
strength = password_strength(password)

label = strength["label"]
score = strength["score"]

progress_val = min(max(score / 6.0, 0.0), 1.0)
st.markdown(f"**Strength:** {label}")
st.progress(progress_val)

# ------------------------
#      ساخت QR code
# ------------------------
st.markdown("---")
st.markdown("**QR Code** (scan to paste password on your phone):")

qr_img = qrcode.make(password)
buf = io.BytesIO()
qr_img.save(buf, format="PNG")
buf.seek(0)

st.image(buf, width=200)

st.download_button(
    label="Download QR image",
    data=buf.getvalue(),
    file_name="password_qr.png",
    mime="image/png"
)




















# import streamlit as st
# import io
# import qrcode
# from password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinGenerator, password_strength

# # Set page config as the first Streamlit command
# st.set_page_config(page_title="Password Generator", layout="centered")

# # Initialize session state
# if 'password_history' not in st.session_state:
#     st.session_state.password_history = []

# if 'theme' not in st.session_state:
#     st.session_state.theme = 'light'

# # Theme toggle in sidebar
# st.sidebar.title("Settings")
# dark_mode = st.sidebar.toggle("Dark Mode", value=(st.session_state.theme == 'dark'))

# if dark_mode:
#     st.session_state.theme = 'dark'
# else:
#     st.session_state.theme = 'light'

# # Apply theme via CSS
# if st.session_state.theme == 'dark':
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #121212;
#         color: white;
#     }
#     .stSlider label, .stCheckbox label, .stToggle label, .stRadio label, .stTextInput label {
#         color: white;
#     }
#     .stProgress > div > div > div > div {
#         background-color: #4CAF50;
#     }
#     </style>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: white;
#         color: black;
#     }
#     .stSlider label, .stCheckbox label, .stToggle label, .stRadio label, .stTextInput label {
#         color: black;
#     }
#     .stProgress > div > div > div > div {
#         background-color: #4CAF50;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Display password history in sidebar
# st.sidebar.title("Password History")
# if st.session_state.password_history:
#     for idx, p in enumerate(st.session_state.password_history):
#         st.sidebar.code(p, language="text")
#     st.sidebar.write(f"Showing {len(st.session_state.password_history)} of max 8 passwords")
# else:
#     st.sidebar.write("No passwords generated yet.")

# # Main app
# st.image('./images/1_kKrBYYaPTaSTOlOIfsC-6w11.png')
# st.title(":zap: Password Generator")

# option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

# if option == 'Pin Code':
#     length = st.slider("Select PIN Length", 4, 32)
#     generator = PinGenerator(length)

# elif option == 'Random Password':
#     length = st.slider("Select Password Length", 7, 100)
#     include_numbers = st.checkbox("Include Numbers", value=True)
#     include_symbols = st.toggle("Include Symbols")
#     generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

# elif option == 'Memorable Password':
#     num_of_words = st.slider("Number of Words", 2, 10, value=3)
#     separator = st.text_input("Separator", value='-')
#     capitalize = st.checkbox("Capitalize Words", value=False)
#     generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)

# # Generate button to trigger password generation
# if st.button("Generate Password"):
#     password = generator.generate()
#     # Add to history, keep only the last 8 passwords
#     st.session_state.password_history.append(password)  # Add new password first
#     if len(st.session_state.password_history) > 5:  # Check if exceeds 8
#         st.session_state.password_history.pop(0)  # Remove the oldest password
    
#     st.write(f"Your generated password is: `{password}`")
#     st.code(password, language="text")

#     # Password strength
#     strength = password_strength(password)
#     label = strength["label"]
#     score = strength["score"]
#     progress_val = min(max(score / 6.0, 0.0), 1.0)
#     st.markdown(f"**Strength:** {label}")
#     st.progress(progress_val)

#     # QR Code
#     st.markdown("---")
#     st.markdown("**QR Code** (scan to paste password on your phone):")
#     qr_img = qrcode.make(password)
#     buf = io.BytesIO()
#     qr_img.save(buf, format="PNG")
#     buf.seek(0)
#     st.image(buf, width=200)

#     st.download_button(
#         label="Download QR image",
#         data=buf.getvalue(),
#         file_name="password_qr.png",
#         mime="image/png"
#     )







































































































































































































































































































































































































































































































































