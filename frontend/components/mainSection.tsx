"use client";

import { useEffect, useState } from "react";
import DefaultUi from "./defaultUi";
import { FileText, Send, ChevronRight, ChevronDown } from "lucide-react";
import { Input } from "./ui/input";
import { Spinner } from "./ui/spinner";

type Source = {
  text: string;
  metadata: {
    filename: string;
    page_number: number;
    chunk_index: number;
  };
};

type Message = {
  query: string;
  answer: string;
  sources: Source[];
};

const MainSection = ({
  selectedDocument,
  setSelectedDocument,
}: {
  selectedDocument: string;
  setSelectedDocument: React.Dispatch<React.SetStateAction<string>>;
}) => {
  const [mainScreen, setMainScreen] = useState(true);
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [openSources, setOpenSources] = useState<number[]>([]);

  const toggleSources = (messageIndex: number) => {
    setOpenSources((prev) =>
      prev.includes(messageIndex)
        ? prev.filter((i) => i !== messageIndex)
        : [...prev, messageIndex],
    );
  };

  const getAnswer = async (question: string) => {
    if (!question.trim()) return;

    setError("");
    setQuery("");

    const newMessage: Message = {
      query: question,
      answer: "",
      sources: [],
    };

    setMessages((prev) => [...prev, newMessage]);

    const messageIndex = messages.length;

    setLoading(true);

    try {
      const request = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            query: question,
            filename: selectedDocument || null,
          }),
        },
      );

      if (!request.ok) {
        const errorData = await request.json()
        console.log(errorData)
        throw new Error(errorData.detail || "Failed to get a response from the server");
      }

      const response = await request.json();

      setMessages((prev) =>
        prev.map((item, index) =>
          index === messageIndex
            ? {
                ...item,
                answer: response.answer,
                sources: response.sources ?? [],
              }
            : item,
        ),
      );
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "An unexpected error occurred",
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!mainScreen && query.trim()) {
      getAnswer(query);
    }
  }, [mainScreen]);

  return (
    <div className="w-full">
      {mainScreen && (
        <DefaultUi
          setMainScreen={setMainScreen}
          query={query}
          setQuery={setQuery}
          setSelectedDocument={setSelectedDocument}
        />
      )}

      {!mainScreen && (
        <div className="w-[90%] mx-auto pb-32">
          <div className="w-full mt-12 space-y-6">
            {messages.map((item, index) => (
              <div key={index}>
                {/* user message */}
                <div className="flex justify-end">
                  <div className="bg-secondary px-4 py-2 rounded-md max-w-[60%] wrap-break-words">
                    {item.query}
                  </div>
                </div>

                {/* agent  answer */}
                <div className="flex justify-start mt-2">
                  <div className="px-4 py-4 rounded-md max-w-[80%] wrap-break-words">
                    {item.answer}

                    {item.sources?.length > 0 && (
                      <div className="mt-4">
                        <button
                          onClick={() => toggleSources(index)}
                          className="flex items-center gap-2 px-3 py-2 rounded-md border bg-secondary/70 hover:bg-secondary transition-colors"
                        >
                          <span className="text-xs   font-medium">
                            {item.sources.length} source
                            {item.sources.length > 1 ? "s" : ""}
                          </span>
                          {openSources.includes(index) ? (
                            <ChevronDown className="h-4 w-4" />
                          ) : (
                            <ChevronRight className="h-4 w-4" />
                          )}
                        </button>

                        {openSources.includes(index) && (
                          <div className="mt-3 space-y-3">
                            {item.sources.map((source, sourceIndex) => (
                              <div
                                key={sourceIndex}
                                className="rounded-md bg-secondary p-3 border"
                              >
                                <div className="flex items-center gap-2">
                                  <FileText className="text-indigo-500 h-4 w-4" />
                                  <p className="font-semibold">
                                    {source.metadata.filename}
                                  </p>
                                </div>

                                <div className="flex items-center gap-2 my-2">
                                  <div className="text-xs px-2 py-1 border rounded-sm bg-indigo-50 border-indigo-300">
                                    Page {source.metadata.page_number}
                                  </div>

                                  <div className="text-xs px-2 py-1 border rounded-sm border-indigo-300">
                                    Chunk {source.metadata.chunk_index + 1}
                                  </div>
                                </div>

                                <div className="bg-primary/10 p-2 rounded-md text-sm border-l-2 border-l-indigo-300 whitespace-pre-wrap">
                                  {source.text}
                                </div>
                              </div>
                            ))}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}

            {error && (
              <div className="bg-red-100 text-red-600 p-3 rounded-md w-fit">
                {error}
              </div>
            )}

            {loading && (
              <div className="flex justify-start">
                <Spinner />
              </div>
            )}
          </div>

          {/* Input */}
          <div className=" rounded-md fixed bottom-5 left-1/2 -translate-x-1/2 w-[70%]   z-50">
            <div className="w-full max-w-3xl bg-white">
              <div className="relative">
                <Input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter" && query.trim()) {
                      getAnswer(query);
                    }
                  }}
                  onDragOver={(e) => e.preventDefault()}
                  onDrop={(e) => {
                    e.preventDefault();
                    const docName = e.dataTransfer.getData("document");
                    setSelectedDocument(docName);
                    setQuery((prev) =>
                      prev.includes(docName) ? prev : prev + `@${docName}`,
                    );
                  }}
                  placeholder="Ask anything about your documents..."
                  className="h-14 rounded-md pr-14 text-base shadow-sm border-border/60 focus-visible:ring-1 focus-visible:border-ring/20"
                />
                <button
                  type="button"
                  disabled={!query.trim() || loading}
                  onClick={() => getAnswer(query)}
                  className="absolute right-2 top-1/2 -translate-y-1/2 flex h-10 w-10 items-center justify-center rounded-md bg-secondary disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <Send className="h-4 w-4 text-primary/70" />
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainSection;
