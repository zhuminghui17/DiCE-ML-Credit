import joblib


def predict(data):
    # Load the trained model
    exp = joblib.load("exp.sav")

    # Generate counterfactuals based on the input data
    e1 = exp.generate_counterfactuals(data, total_CFs=5, desired_class="opposite")

    # Convert the counterfactuals to JSON
    counterfactual = e1.cf_examples_list[0].final_cfs_df.to_json(orient="records")

    # Create a comprehensive prompt with background information for OpenAI's API
    prompt = f"""Task: Generate personalized hotel advertising emails using DiCE model counterfactuals.

            Background: We are using the DiCE model to understand why potential customers might cancel their hotel bookings. The model provides counterfactual suggestions indicating what could have been changed in their booking details to prevent cancellation.

            Based on the following original booking details:

            {data.to_json(orient='records')}

            And considering these counterfactual suggestions:

            {counterfactual}

            Your task is to: 1) first summarize original booking details shortly. 2) analyze the counterfactual, pick the most useful one and and create short, compelling and personalized advertising emails which focus on one point. These emails should address the points raised in the counterfactual analysis and offer incentives or changes that could convince the customer to retain their booking. The goal is to reduce booking cancellations and enhance customer satisfaction.
            Remember to construct your response with markdown syntax and provide justification.
            """

    return prompt
