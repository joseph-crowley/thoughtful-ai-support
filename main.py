from chat import chat


def main():
    print("Thoughtful AI Solution GPT\n---\n")
    system = "You are a friendly and helpful chatbot. Answer the user's questions about Thoughtful AI's products and services. If the question is not about Thoughtful AI, Do not attach a relevant query, just respond with a friendly message."
    while True:
        user = input("\n---\nYou: ")
        solution_response = chat(system, user)


        print(f"\n\n---\nGPT: {solution_response.conversational_agent_response}\n")

        if solution_response.most_relevant_query:
            print(f"\n---\nFrom our FAQ:\n- {solution_response.most_relevant_query.question}\n- {solution_response.most_relevant_query.answer}\n")
            system = solution_response.most_relevant_query

        print("\n"+("-"*50) + "\n")

if __name__ == "__main__":
    main()