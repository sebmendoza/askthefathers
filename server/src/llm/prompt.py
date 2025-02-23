import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def hit_gemini(prompt) -> str:

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text


class RAGPromptGenerator:
    """
    A class to generate prompts for Large Language Models using RAG results
    """

    def __init__(self):
        self.base_template = """You are a helpful AI assistant tasked with answering questions using provided context and information. Your responses should seamlessly integrate the retrieved information while remaining natural and conversational.

CONTEXT:
Below are relevant excerpts from reliable sources that should inform your response. These excerpts have been automatically retrieved based on their relevance to the user's query:

{context}

USER QUERY:
{query}

INSTRUCTIONS:
1. Carefully analyze both the user's query and the provided context
2. Formulate a response that:
   - Directly addresses the user's question
   - Accurately incorporates relevant information from the context
   - Maintains a natural, conversational tone
   - Cites specific information when appropriate
   - Acknowledges any limitations in the provided context
   - Remains objective and factual
3. If the context doesn't fully address the user's query:
   - Be transparent about what information is not covered
   - Provide a response based on what is known from the context
   - Avoid making assumptions beyond the provided information

Please provide your response in a clear, well-structured format that best serves the user's needs. Your goal is to be helpful, accurate, and direct while making optimal use of the retrieved context.

Remember:
- Stay within the scope of the provided context
- Maintain appropriate confidence levels
- Be clear about what information comes from the context versus general knowledge
- Address any ambiguities in the user's query if necessary
- Format your response to maximize readability and understanding"""

    def format_rag_results(self, results: list) -> str:
        """
        Format RAG results into a string suitable for the prompt.

        Args:
            results (list): List of RAG results/excerpts

        Returns:
            str: Formatted context string
        """
        if not results:
            return "No relevant context available."

        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(f"[{i}] {result.strip()}")

        return "\n\n".join(formatted_results)

    def generate_prompt(self, query: str, rag_results: list) -> str:
        """
        Generate a complete prompt combining the user query and RAG results.

        Args:
            query (str): User's question or query
            rag_results (list): List of relevant excerpts from RAG

        Returns:
            str: Complete formatted prompt
        """
        context = self.format_rag_results(rag_results)
        return self.base_template.format(
            context=context,
            query=query
        )
