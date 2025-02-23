"use client";
import PromptButton from "@/components/PromptButton";
import { useState, ChangeEvent } from "react";

export default function Home() {
  const [responseText, setResponseText] = useState<string>("No Data");
  const [query, setQuery] = useState<string>("");

  const handleTextChange = (e: ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };
  const handleClear = () => {
    setResponseText("");
  };

  return (
    <div className="flex items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <div className="flex flex-col gap-4 w-full">
        <h3 className="w-full flex items-center justify-center text-center font-semibold">askthefathers.com</h3>
        <div>
          <input
            type="text"
            value={query}
            onChange={handleTextChange}
            placeholder="Type here"
            className="rounded border border-blue-200 focus:outline-none py-2 px-4 w-full"
          ></input>
          <PromptButton setResponseText={setResponseText} query={query} />
          <button className="rounded border border-blue-200 focus:outline-none py-2 px-4 ml-2" onClick={handleClear}>
            Clear
          </button>
          <h3 className="text-xl font-medium">Response</h3>
          <p className={`border ${responseText ? "border-blue-400" : ""}  flex-grow p-2 shadow-md`}>{responseText}</p>
        </div>
      </div>
    </div>
  );
}
