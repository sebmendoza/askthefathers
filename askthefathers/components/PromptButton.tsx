import { Dispatch, SetStateAction, useState } from "react";

interface QueryResponse {
  response: string;
}

type PromptButtonProps = {
  query: string;
  setResponseText: Dispatch<SetStateAction<string>>;
};
function PromptButton({ query, setResponseText }: PromptButtonProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleClick = async () => {
    const endpoint = "http://localhost:8000/retrieve";
    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: query }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to fetch");
      }

      const data: QueryResponse = await response.json();
      console.log(data);
      setResponseText(data.response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button
      onClick={handleClick}
      disabled={isLoading}
      className={`border rounded py-2 px-6 my-2 transition-all ${
        isLoading
          ? "bg-gray-200 text-gray-500 cursor-not-allowed"
          : "border-blue-200 hover:border-transparent hover:bg-blue-200 hover:text-white text-blue-400"
      }`}
    >
      {isLoading ? "Sending..." : "Send"}
    </button>
  );
}

export default PromptButton;
