import qr

# Data to be encoded
data = "Hello, World!"

# Create a QR code object
qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")
