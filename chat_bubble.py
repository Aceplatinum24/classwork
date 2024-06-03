from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
width, height = 400, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define the parameters for the chat bubble
x, y = 50, 50
width, height = 300, 100
radius = 20
color = "lightblue"

# Draw the chat bubble
draw.rectangle((x, y, x+width, y+height), fill=color)
draw.polygon([(x+width, y+height), (x+width+radius, y+height), (x+width, y+height+radius)], fill=color)
draw.polygon([(x, y+height), (x-radius, y+height), (x, y+height+radius)], fill=color)

# Add text inside the chat bubble
text = "Hello, how are you?"
font = ImageFont.truetype("arial.ttf", 16)
text_width, text_height = draw.textsize(text, font=font)
text_x = x + (width - text_width) / 2
text_y = y + (height - text_height) / 2
draw.text((text_x, text_y), text, fill="black", font=font)

# Save the image
image.save("chat_bubble.png")
