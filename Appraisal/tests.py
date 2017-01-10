from selenium import webdriver

browser = webdriver.Firefox()
# checks out home page
browser.get("http://localhost:8000")

# sees word hostel on home page
assert "Django" in browser.title

# registers
# about us
# checks available hostels
# checks available rooms
# books a room
# makes payment
# checks bookings made
# verifies name in list
# contact us


browser.quit()
