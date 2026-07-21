def get_response(user):

    user = user.lower()

    if user == "exit":
        return "Thank you for visiting. Goodbye!"

    elif "hello" in user or "hi" in user:
        return "Hello! Welcome to our Customer Service."

    elif "how are you" in user:
        return "I am fine. How can I help you today?"

    elif "order" in user:
        return "Please provide your Order ID."

    elif "refund" in user:
        return "Refunds are processed within 5-7 business days."

    elif "return" in user:
        return "You can return your product within 7 days."

    elif "shipping" in user or "delivery" in user:
        return "Delivery usually takes 3-5 business days."

    elif "payment" in user:
        return "We accept UPI, Credit Card, Debit Card and Net Banking."

    elif "contact" in user:
        return "Email: support@example.com"

    elif "working hours" in user or "hours" in user:
        return "Monday to Saturday: 9 AM - 6 PM."

    elif "thank" in user:
        return "You're welcome!"

    else:
        return "Sorry, I didn't understand your question."