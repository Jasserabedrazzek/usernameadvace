import streamlit as st
import socket
import qrcode

# Get the hostname
hostname = socket.gethostname()

# Display the hostname in Streamlit
st.write("Hostname:", hostname)

# Generate a QR code for the page URL
qr = qrcode.QRCode()
qr.add_data(st.url)
qr.make()

# Get the QR code image as SVG
qr_image = qr.make_image(image_factory=qrcode.image.svg.SvgImage)

# Display the QR code in Streamlit
st.image(qr_image)
