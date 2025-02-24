import gradio as gr

# Function to calculate the average price of eggs
def calculate_average_price(prices):
    try:
        # Convert input string into a list of prices (assuming the input is comma-separated)
        price_list = [float(price.strip()) for price in prices.split(',')]
        
        if not price_list:
            return "No valid prices entered."
        
        # Calculate the average
        average_price = sum(price_list) / len(price_list)
        return f"The average price of a dozen eggs in Northern Virginia is: ${average_price:.2f}"
    
    except ValueError:
        return "Invalid input. Please enter prices separated by commas (e.g., 2.50, 2.80, 3.00)."

# Gradio interface to accept user input
iface = gr.Interface(
    fn=calculate_average_price,
    inputs=gr.Textbox(lines=2, placeholder="Enter egg prices (comma separated)..."),
    outputs="text",
    title="Average Price of Eggs in Northern Virginia",
    description="Enter the prices of a dozen eggs in Northern Virginia (comma separated), and the agent will calculate the average price."
)

iface.launch()
