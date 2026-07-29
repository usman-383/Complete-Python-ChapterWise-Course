import pyautogui
import time
import pyperclip

# Step 1: Click on the icon chrome icon
pyautogui.moveTo(589, 1061, duration=0.5)
pyautogui.click()

# Step 2: Wait for the app to load/respond
time.sleep(2)

# Step 3: Click and drag to select text
pyautogui.moveTo(689, 231, duration=0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1856, 899, duration=1)
pyautogui.mouseUp()

# Step 4: Copy selected text to clipboard
pyautogui.hotkey('ctrl', 'c')

# Step 5: Wait briefly for clipboard to update
time.sleep(0.5)

# Step 6: Store clipboard content into a variable
selected_text = pyperclip.paste()

# Print to verify (optional)
print("Captured text:", selected_text)
