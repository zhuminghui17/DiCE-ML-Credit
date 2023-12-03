import gradio as gr
import numpy as np

# # Dummy model function: replace with your actual model prediction logic
# def predict(Gender, Age, Debt, Married, BankCustomer, Industry, Ethnicity, YearsEmployed, PriorDefault, Employed, CreditScore, DriversLicense, Citizen, ZipCode, Income):
#     # Here you would process the inputs and use your pretrained model to make a prediction
#     # For demonstration, I'm just generating random results and converting them to strings
#     random_results = np.random.rand(1, 5).flatten()  # Generate random numbers
#     results_as_strings = [f"Result {i+1}: {result:.2f}" for i, result in enumerate(random_results)]
#     return results_as_strings

# Dummy model function: replace with your actual model prediction logic
def predict(Gender, Age):
    random_results = np.random.rand(1, 5).flatten()  # Generate random numbers
    # Convert the results to a list of lists (each inner list is a row)
    results_as_table = [list(random_results)]
    return results_as_table


# Define Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Radio(['m', 'f']),
        'text'
    ],
    outputs=gr.outputs.Dataframe(type="pandas"),
    title="Credit Card Approval Prediction"
)

if __name__ == "__main__":
    demo.launch(show_api=False)
