import gradio as gr
from playwright.sync_api import sync_playwright

# Function to fetch the Mars countdown using Playwright
def get_mars_countdown():
    try:
        # Use Playwright to automate the browser
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)  # Launch the Chromium browser
            page = browser.new_page()
            page.goto("https://marscountdown.org")  # Navigate to the page

            # Wait for the countdown element to appear
            page.wait_for_selector("#countdown")  # Wait for the #countdown element to load

            # Extract the countdown text from the element with id 'countdown'
            countdown_text = page.inner_text("#countdown").strip()

            # Close the browser
            browser.close()

            return f"Countdown: {countdown_text}"

    except Exception as e:
        return f"Error: {str(e)}"

# Define the Gradio interface
def countdown_interface():
    return get_mars_countdown()

# Create the Gradio interface
iface = gr.Interface(fn=countdown_interface, inputs=[], outputs="text", live=True, title="Mars Countdown", description="Fetch the countdown for the Mars launch")

# Launch the Gradio interface
iface.launch()
